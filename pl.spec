%define		xpce_version 6.2.6
Summary:	SWI Prolog Language
Summary(pl):	Jêzyk SWI Prolog
Name:		pl
Version:	5.2.6
Release:	1.1
License:	GPL
Group:		Development/Languages
Source0:	http://www.swi.psy.uva.nl/cgi-bin/nph-download/SWI-Prolog/%{name}-%{version}.tar.gz
# Source0-md5:	a2bf7e48979758bdba488f1680a3a8d8
Patch0:		%{name}-smp.patch
URL:		http://www.swi-prolog.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel >= 4.2
BuildRequires:	unixODBC-devel
Obsoletes:	swi-prolog
Obsoletes:	swi-pl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISO/Edinburgh-style Prolog compiler including modules, autoload,
libraries, Garbage-collector, stack-expandor, C/C++-interface,
GNU-readline interface, very fast compiler. Including packages clib
(Unix process control and sockets), cpp (C++ interface), sgml (reading
XML/SGML), sgml/RDF (reading RDF into triples) and XPCE (Graphics UI
toolkit, integrated editor (Emacs-clone) and source-level debugger).

%description -l pl
Kompilator jêzyka PROLOG w stylu Edinburgh wraz z modu³ami,
bibliotekami, garbage collectorrem, interfejsem C, interfejsami do GNU
readline, GNU Emacsa i X11 przy u¿yciu XPCE.

%package -n xpce
Summary:	XPCE - GUI Toolkit for (SWI-)Prolog
License:	Distributable, free for demo-, evaluation- and personal use
Group:		Development/Languages
URL:		http://www.swi.psy.uva.nl/projects/xpce/
Requires:	%{name} = %{version}

%description -n xpce
Graphical User Interface (GUI) toolkit for Prolog and other
dynamically typed languages. Provides Object Oriented programming to
Prolog as well as a high-level portable GUI toolkit for (SWI-)Prolog.
Also available for Quintus and SICStus Prolog.

%description -n xpce -l pl
Zestaw Graficzny Interfejsu U¿ytkownika (GUI) dla Prologa i innych
dynamicznie wpisywanych jêzyków. Udostêpnia objektowo zorientowane
programowanie dla Prologa jak tak¿e jako wysoko dostêpny przeno¶ny
zestaw GUI dla (SWI-)Prologa. Dostêpne tak¿e dla Quintus i SICStus
Prolog.

%prep
%setup -q
%patch0 -p0

%build
cd src
	%{__aclocal}
	%{__autoconf}
	%configure
	%{__make}
%ifnarch alpha
	%{__make} check
%endif
cd ..

cd packages
	cd xpce/src
		%{__aclocal}
		%{__autoconf}
		%configure
		%{__make}
	cd ../..

for i in clib cpp odbc table sgml semweb http sgml/RDF; do
	cd $i
	%{__aclocal}
	%{__autoconf}
	%configure
	%{__make}
	cd ..
done
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

%{__make} install -C src \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

install -d $RPM_BUILD_ROOT%{_libdir}/pl-%{version}/doc

for i in clib cpp odbc table sgml semweb http sgml/RDF xpce/src; do
	PATH=$RPM_BUILD_ROOT%{_bindir}:$PATH \
	%{__make} rpm-install -C packages/$i \
		PLBASE=$RPM_BUILD_ROOT%{_libdir}/pl-%{version} \
		prefix=$RPM_BUILD_ROOT%{_prefix} \
		bindir=$RPM_BUILD_ROOT%{_bindir} \
		mandir=$RPM_BUILD_ROOT%{_mandir}/man1
done

# why are manpages installed twice?
rm -rf $RPM_BUILD_ROOT%{_libdir}/pl-%{version}/man

mv -f $RPM_BUILD_ROOT%{_libdir}/pl-%{version}/library/MANUAL .
mv -f $RPM_BUILD_ROOT%{_mandir}/man3/readline.{3,3pl}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* LSM ChangeLog PORTING MANUAL
%doc dotfiles/dot*
%attr(755,root,root)%{_bindir}/pl*
%dir %{_libdir}/pl-%{version}
%attr(755,root,root)%{_libdir}/pl-%{version}/bin
%{_libdir}/pl-%{version}/boot*
%{_libdir}/pl-%{version}/lib*
%{_libdir}/pl-%{version}/include
%{_libdir}/pl-%{version}/do*
%{_libdir}/pl-%{version}/runtime
%{_libdir}/pl-%{version}/swipl
%{_mandir}/man?/pl*
%{_mandir}/man?/readline*

%files -n xpce
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/xpce*
%attr(755,root,root)%{_libdir}/%{name}-%{version}/xpce-%{xpce_version}/bin/*/*
%attr(755,root,root)%{_libdir}/%{name}-%{version}/xpce-%{xpce_version}/lib/*/*
%{_libdir}/%{name}-%{version}/xpce-%{xpce_version}/appl-help
%{_libdir}/%{name}-%{version}/xpce-%{xpce_version}/bitmaps
%{_libdir}/%{name}-%{version}/xpce-%{xpce_version}/include
%{_libdir}/%{name}-%{version}/xpce-%{xpce_version}/man
%{_libdir}/%{name}-%{version}/xpce-%{xpce_version}/pl
%{_libdir}/%{name}-%{version}/xpce-%{xpce_version}/prolog
%{_mandir}/man?/xpce*
