#
# TODO
# - package jpl
# - maybe separate packages to miscelious packages?
%define		xpce_version 6.6.64
Summary:	SWI Prolog Language
Summary(pl.UTF-8):	Język SWI Prolog
Name:		pl
Version:	5.6.64
Release:	3
License:	GPL
Group:		Development/Languages
Source0:	http://gollem.science.uva.nl/cgi-bin/nph-download/SWI-Prolog/%{name}-%{version}.tar.gz
# Source0-md5:	2f06f64007fdac076a277ee4a8c53274
URL:		http://www.swi-prolog.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel >= 4.2
BuildRequires:	unixODBC-devel
BuildRequires:	gmp-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	jdk
Obsoletes:	swi-pl
Obsoletes:	swi-prolog
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISO/Edinburgh-style Prolog compiler including modules, autoload,
libraries, Garbage-collector, stack-expandor, C/C++-interface,
GNU-readline interface, very fast compiler. Including packages clib
(Unix process control and sockets), cpp (C++ interface), sgml (reading
XML/SGML), sgml/RDF (reading RDF into triples) and XPCE (Graphics UI
toolkit, integrated editor (Emacs-clone) and source-level debugger).

%description -l pl.UTF-8
Kompilator języka PROLOG w stylu Edinburgh wraz z modułami,
bibliotekami, garbage collectorrem, interfejsem C, interfejsami do GNU
readline, GNU Emacsa i X11 przy użyciu XPCE.

%package -n xpce
Summary:	XPCE - GUI Toolkit for (SWI-)Prolog
License:	Distributable, free for demo-, evaluation- and personal use
Group:		Development/Languages
URL:		http://www.swi.psy.uva.nl/projects/xpce/
Requires:	%{name} = %{version}-%{release}

%description -n xpce
Graphical User Interface (GUI) toolkit for Prolog and other
dynamically typed languages. Provides Object Oriented programming to
Prolog as well as a high-level portable GUI toolkit for (SWI-)Prolog.
Also available for Quintus and SICStus Prolog.

%description -n xpce -l pl.UTF-8
Zestaw Graficzny Interfejsu Użytkownika (GUI) dla Prologa i innych
dynamicznie wpisywanych języków. Udostępnia obiektowo zorientowane
programowanie dla Prologa jak także jako wysoko dostępny przenośny
zestaw GUI dla (SWI-)Prologa. Dostępne także dla Quintus i SICStus
Prolog.

%prep
%setup -q
sed -e "s@mkdir@mkdir -p@g" -i packages/xpce/src/Makefile.in

%build
cd src
	cp -f /usr/share/automake/config.sub .
	%{__aclocal}
	%{__autoconf}
	%configure
	%{__make}
	%{__make} check
cd ..

# the packages are written in Prolog itself
PATH="$(pwd)/src:$PATH"; export PATH

cd packages
wd=`pwd`
for i in xpce/src clib cpp odbc table sgml semweb http sgml/RDF chr clpqr nlp ssl pldoc plunit zlib; do
	cd $i
	cp -f /usr/share/automake/config.sub .
	%{__aclocal}
	%{__autoconf}
	%configure
	%{__make}
	cd $wd
done
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -C src \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/pl-%{version}/doc

for i in clib cpp odbc table sgml semweb http sgml/RDF xpce/src chr clpqr nlp ssl pldoc plunit zlib; do
	PATH=$RPM_BUILD_ROOT%{_bindir}:$PATH \
	%{__make} rpm-install -C packages/$i \
		PLBASE=$RPM_BUILD_ROOT%{_libdir}/pl-%{version} \
		prefix=$RPM_BUILD_ROOT%{_prefix} \
		bindir=$RPM_BUILD_ROOT%{_bindir} \
		mandir=$RPM_BUILD_ROOT%{_mandir}/man1
done

# why are manpages installed twice?
#rm -rf $RPM_BUILD_ROOT%{_libdir}/pl-%{version}/man

#mv -f $RPM_BUILD_ROOT%{_mandir}/man3/readline.{3,3pl}

%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%doc README* LSM ChangeLog PORTING
%doc dotfiles/dot*
%attr(755,root,root) %{_bindir}/pl*
%dir %{_libdir}/pl-%{version}
%attr(755,root,root) %{_libdir}/pl-%{version}/bin
%{_libdir}/pl-%{version}/boot*
%{_libdir}/pl-%{version}/lib*
%{_libdir}/pl-%{version}/include
%{_libdir}/pl-%{version}/do*
%{_libdir}/pl-%{version}/swipl
%{_libdir}/pl-%{version}/*.rc
%{_pkgconfigdir}/pl.pc
%{_mandir}/man?/pl*
#%{_mandir}/man?/readline*

%files -n xpce
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xpce*
%dir %{_libdir}/%{name}-%{version}/xpce-%{xpce_version}
%attr(755,root,root) %{_libdir}/%{name}-%{version}/xpce-%{xpce_version}/bin
%attr(755,root,root) %{_libdir}/%{name}-%{version}/xpce-%{xpce_version}/lib
%{_libdir}/%{name}-%{version}/xpce-%{xpce_version}/appl-help
%{_libdir}/%{name}-%{version}/xpce-%{xpce_version}/bitmaps
%{_libdir}/%{name}-%{version}/xpce-%{xpce_version}/include
%{_libdir}/%{name}-%{version}/xpce-%{xpce_version}/man
%{_libdir}/%{name}-%{version}/xpce-%{xpce_version}/pl
%{_libdir}/%{name}-%{version}/xpce-%{xpce_version}/prolog
#%{_mandir}/man?/xpce*
