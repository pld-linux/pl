Summary:	SWI Prolog Language
Summary(pl):	Jêzyk SWI Prolog
Name:		pl
Version:	3.4.2
Release:	4
License:	GPL
Group:		Development/Languages
Source0:	ftp://metalab.unc.edu/pub/Linux/devel/lang/prolog/swi/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-readline.patch
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel >= 4.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Edinburgh-style Prolog compiler including modules, autoload,
libraries, Garbage-collector, stack-expandor, C-interface,
GNU-readline and GNU-Emacs interface, very fast compiler, X11
interface using XPCE (info: ftp swi.psy.uva.nl:/pub/xpce)

%description -l pl 
Kompilator jêzyka PROLOG w stylu Edinburgh wraz z modu³ami,
bibliotekami, garbage collectorrem, interfejsem C, interfejsami
do GNU readline, GNU Emacsa i X11 przy u¿yciu XPCE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cd src
aclocal
autoconf
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

cd src 
%{__make} install install-bins install-arch install-libs \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

(cd $RPM_BUILD_ROOT%{_bindir} ;\
rm -f * ;\
ln -s %{_libdir}/pl-%{version}/bin/%{_target_cpu}-linux/pl pl ;\
ln -s %{_libdir}/pl-%{version}/bin/%{_target_cpu}-linux/pl-bite pl-bite ;\
ln -s %{_libdir}/pl-%{version}/bin/%{_target_cpu}-linux/plld plld ;\
ln -s %{_libdir}/pl-%{version}/bin/%{_target_cpu}-linux/plrc plrc )

mv $RPM_BUILD_ROOT/%{_libdir}/pl-%{version}/library/MANUAL .

gzip -9nf README* LSM ChangeLog PORTING MANUAL

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*.gz LSM.gz ChangeLog.gz PORTING.gz MANUAL.gz
%attr(755,root,root)%{_bindir}/pl
%attr(755,root,root)%{_bindir}/pl-bite
%attr(755,root,root)%{_bindir}/plld
%attr(755,root,root)%{_bindir}/plrc
%{_libdir}/pl-%{version}/
%{_mandir}/man1/*.1*
