Summary:	SWI Prolog Language
Summary(pl):	SWI Prolog
Name:		pl
Version:	3.2.6
Release:	1
Copyright:	SWI Licence
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Source:		ftp://sunsite.unc.edu/pub/Linux/devel/prolog/%name-%version.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Edinburgh-style Prolog compiler including modules, autoload, libraries, 
Garbage-collector, stack-expandor, C-interface, GNU-readline and GNU-Emacs 
interface, very fast compiler, X11 interface using XPCE 
(info: ftp swi.psy.uva.nl:/pub/xpce)

%description -l pl 
Kompilator PROLOGu.

%prep
%setup -q

%build
cd src
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT

cd src
make prefix=$RPM_BUILD_ROOT/usr install
make prefix=$RPM_BUILD_ROOT/usr install-bins
make prefix=$RPM_BUILD_ROOT/usr install-arch
make prefix=$RPM_BUILD_ROOT/usr install-libs

#install -d $RPM_BUILD_ROOT/usr
#install -d $RPM_BUILD_ROOT%{_bindir}
#install -d $RPM_BUILD_ROOT%{_libdir}/pl-%version
#install -d $RPM_BUILD_ROOT%{_mandir}

#cd src
#make prefix=$RPM_BUILD_ROOT/usr install
cd $RPM_BUILD_ROOT%{_bindir}
rm -f *
ln -s %{_libdir}/pl-%version/bin/i686-linux/chpl chpl
ln -s %{_libdir}/pl-%version/bin/i686-linux/pl pl
ln -s %{_libdir}/pl-%version/bin/i686-linux/pl-bite pl-bite
ln -s %{_libdir}/pl-%version/bin/i686-linux/plld plld

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

cd $RPM_BUILD_DIR/%name-%version
gzip -9nf README* LICENSE LSM ChangeLog PORTING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*.gz LICENSE.gz LSM.gz ChangeLog.gz PORTING.gz
%attr(755,root,root)%{_bindir}/pl
%attr(755,root,root)%{_bindir}/chpl
%attr(755,root,root)%{_bindir}/plld
%attr(755,root,root)%{_bindir}/pl-bite
%{_libdir}/pl-%version/
%{_mandir}/man1/*.gz

%changelog
* Tue May  4 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [3.2.6-1]
- upgradeing to version 3.2.6,
- added gziped man pages and information.

* Tue Sep 22 1998 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- upgradeing from 2.9.10 to 3.1.0.

* Mon Sep 21 1998 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- adding %defattr in %files.

* Thu Aug 13 1998 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- Build RPM.
