Summary:	SWI Prolog Language
Summary(pl):	Jêzyk SWI Prolog
Name:		pl
Version:	5.0.8
Release:	4
License:	GPL
Group:		Development/Languages
Source0:	http://www.swi.psy.uva.nl/cgi-bin/nph-download/SWI-Prolog/%{name}-%{version}.tar.gz
# Source0-md5:	85415533219db3d19d373736492de674
Patch0:		%{name}-smp.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel >= 4.2
URL:		http://www.swi-prolog.org/
Obsoletes:	swi-prolog
Obsoletes:	swi-pl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISO/Edinburgh-style Prolog compiler including modules, autoload, libraries,
Garbage-collector, stack-expandor, C/C++-interface, GNU-readline interface,
very fast compiler.  Including packages clib (Unix process control and
sockets), cpp (C++ interface), sgml (reading XML/SGML), sgml/RDF (reading RDF
into triples) and XPCE (Graphics UI toolkit, integrated editor (Emacs-clone)
and source-level debugger).

%description -l pl
Kompilator jêzyka PROLOG w stylu Edinburgh wraz z modu³ami,
bibliotekami, garbage collectorrem, interfejsem C, interfejsami do GNU
readline, GNU Emacsa i X11 przy u¿yciu XPCE.

%prep
%setup -q
%patch0 -p0

%build
cd src
	%{__aclocal}
	%{__autoconf}
	%configure
	%{__make}
	%{__make} check
cd ..

cd packages
	%{__aclocal}
	%{__autoconf}
	%configure
	%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/
cd src
make install \
        prefix=$RPM_BUILD_ROOT/usr \
        bindir=$RPM_BUILD_ROOT/usr/bin \
        mandir=$RPM_BUILD_ROOT%{_mandir}
cd ..
install -d $RPM_BUILD_ROOT/usr/lib/pl-%{version}/doc/

cd packages
  PATH=$RPM_BUILD_ROOT/usr/bin:$PATH make install \
        PLBASE=$RPM_BUILD_ROOT/usr/lib/pl-%{version} \
        prefix=$RPM_BUILD_ROOT/usr \
        bindir=$RPM_BUILD_ROOT/usr/bin \
        mandir=$RPM_BUILD_ROOT%{_mandir}/man1
cd ..

# why are manpages installed twice?
rm -rf $RPM_BUILD_ROOT/usr/lib/pl-%{version}/man

mv $RPM_BUILD_ROOT/%{_libdir}/pl-%{version}/library/MANUAL .

mv $RPM_BUILD_ROOT/%{_mandir}/man3/readline.{3,3pl}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* LSM ChangeLog PORTING MANUAL
%attr(755,root,root)%{_bindir}/*
%attr(755,root,root)%{_libdir}/pl-%{version}/bin
%{_libdir}/pl-%{version}/boot*
%{_libdir}/pl-%{version}/lib*
%{_libdir}/pl-%{version}/include
%{_libdir}/pl-%{version}/do*
%{_libdir}/pl-%{version}/runtime
%{_libdir}/pl-%{version}/swipl
%{_mandir}/man?/*
