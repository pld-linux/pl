Summary:	SWI Prolog Language
Summary(pl):	SWI Prolog
Name:		pl
Version:	3.4.0
Release:	1
Copyright:	SWI Licence
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Source0:	ftp://metalab.unc.edu/pub/Linux/devel/lang/prolog/swi/BETA/%name-%version.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Edinburgh-style Prolog compiler including modules, autoload,
libraries, Garbage-collector, stack-expandor, C-interface,
GNU-readline and GNU-Emacs interface, very fast compiler, X11
interface using XPCE (info: ftp swi.psy.uva.nl:/pub/xpce)

%description -l pl 
Kompilator PROLOGu.

%prep
%setup -q

%build
cd src
LDFLAGS="-s" ; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

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

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README* LICENSE LSM ChangeLog PORTING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*.gz LICENSE.gz LSM.gz ChangeLog.gz PORTING.gz
%attr(755,root,root)%{_bindir}/pl
%attr(755,root,root)%{_bindir}/pl-bite
%attr(755,root,root)%{_bindir}/plld
%attr(755,root,root)%{_bindir}/plrc
%{_libdir}/pl-%{version}/
%{_mandir}/man1/*
