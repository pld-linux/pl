Summary:	SWI Prolog Language
Summary(pl):	Jêzyk SWI Prolog
Name:		pl
Version:	5.2.6
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.swi.psy.uva.nl/cgi-bin/nph-download/SWI-Prolog/%{name}-%{version}.tar.gz
# Source0-md5:	a2bf7e48979758bdba488f1680a3a8d8
Patch0:		%{name}-smp.patch
URL:		http://www.swi-prolog.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel >= 4.2
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
install -d $RPM_BUILD_ROOT%{_prefix}

%{__make} install -C src \
        prefix=$RPM_BUILD_ROOT%{_prefix} \
        bindir=$RPM_BUILD_ROOT%{_bindir} \
        mandir=$RPM_BUILD_ROOT%{_mandir}

install -d $RPM_BUILD_ROOT%{_libdir}/pl-%{version}/doc

PATH=$RPM_BUILD_ROOT%{_bindir}:$PATH \
%{__make} install -C packages \
        PLBASE=$RPM_BUILD_ROOT%{_libdir}/pl-%{version} \
        prefix=$RPM_BUILD_ROOT%{_prefix} \
        bindir=$RPM_BUILD_ROOT%{_bindir} \
        mandir=$RPM_BUILD_ROOT%{_mandir}/man1

# why are manpages installed twice?
rm -rf $RPM_BUILD_ROOT%{_libdir}/pl-%{version}/man

mv -f $RPM_BUILD_ROOT/%{_libdir}/pl-%{version}/library/MANUAL .
mv -f $RPM_BUILD_ROOT/%{_mandir}/man3/readline.{3,3pl}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* LSM ChangeLog PORTING MANUAL
%doc dotfiles/dot*
%attr(755,root,root)%{_bindir}/*
%dir %{_libdir}/pl-%{version}
%attr(755,root,root)%{_libdir}/pl-%{version}/bin
%{_libdir}/pl-%{version}/boot*
%{_libdir}/pl-%{version}/lib*
%{_libdir}/pl-%{version}/include
%{_libdir}/pl-%{version}/do*
%{_libdir}/pl-%{version}/runtime
%{_libdir}/pl-%{version}/swipl
%{_mandir}/man?/*
