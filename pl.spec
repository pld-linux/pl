#
# TODO
# 	- maybe separate other prolog packages to rpm subpackages
#
# Conditional build:
%bcond_without	java		# don't build with java bindings (So far, JPL only works with Sun Java and IBM Java)
#

%ifnarch %{x8664} i586 i686 pentium3 pentium4 athlon 
%undefine	with_java
%endif

%define		xpce_version 6.6.66
Summary:	SWI Prolog Language
Summary(pl.UTF-8):	Język SWI Prolog
Name:		pl
Version:	5.8.3
Release:	1
License:	LGPL/GPL
Group:		Development/Languages
Source0:	http://www.swi-prolog.org/download/stable/src/%{name}-%{version}.tar.gz
# Source0-md5:	faeb7ade8da9832f113e6748ba6cab03
Patch0:		%{name}-clib-configure.patch
URL:		http://www.swi-prolog.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gmp-devel
%{?with_java:BuildRequires:	java-sun}
BuildRequires:	libjpeg-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel >= 4.2
BuildRequires:	unixODBC-devel
BuildRequires:	uriparser-devel
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
BuildRequires:	zlib-devel
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

%package jpl
Summary:	Dynamic, bidirectional interface between SWI-Prolog and Java
Summary(pl.UTF-8):	Dynamiczny, dwukierunkowy interfejs pomiędzy SWI-Prologiem a Javą
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	java-sun

%description jpl
JPL 3.x is a dynamic, bidirectional interface between SWI-Prolog 5.2.0 or
later and Java 2 runtimes (see JPL 3.x Objectives). It offers two APIs:
  * Java API (Java-calls-Prolog): this interface comprises public Java
    classes which support:
       + constructing Java representations of Prolog terms and queries
       + calling queries within SWI-Prolog engines
       + retrieving (as Java representations of Prolog terms) any bindings
         created by a call
  * Prolog API (Prolog-calls-Java): this interface comprises Prolog library
    predicates which support:
       + creating instances (objects) of Java classes (built-in and
         user-defined)
       + calling methods of Java objects (and static methods of classes),
         perhaps returning values or object references
       + getting and setting the values of fields of Java objects and
         classes

Calls to the two APIs can be nested, e.g. Java code can call Prolog
predicates which call Java methods which call Prolog predicates etc.

%description jpl -l pl.UTF-8
JPL 3.x to dynamiczny, dwukierunkowy interfejs pomiędzy SWI-Prologiem
5.2.0 i późniejszymi a środowiskami uruchomieniowymi Javy 2 (więcej w
dokumencie JPL 3.x Objectives). Oferuje dwa API:
  - API Javy (wywołania Prologu z Javy) - ten interfejs obejmuje klasy
    publiczne Javy obsługujące:
    - tworzenie reprezentacji wyrażeń i zapytań Prologu w Javie
    - wywoływanie zapytań wewnątrz silników SWI-Prologu
    - odtwarzanie (jako reprezentacji wyrażeń Prologu w Javie)
      wszelkich dowiązań utworzonych przez wywołanie
  - API Prologu (wywołania Javy z Prologu) - ten interfejs obejmuje
    predykaty biblioteki Prologu obsługującą:
    - tworzenie instancji (obiektów) klas Javy (wbudowanych i
      zdefiniowanych przez użytkownika)
    - wywołania metod obiektów (i statycznych metod klas) Javy, także
      zwracających wartości lub referencje do obiektów
    - pobieranie i ustawianie wartości pól obiektów i klas Javy

Wywołania obu API mogą być zagnieżdżane, np. kod w Javie może wywołać
predykaty Prologu wywołujące metody Javy, które wywołują predykaty
Prologu itd.

%package xpce
Summary:	XPCE - GUI Toolkit for (SWI-)Prolog
Summary(pl.UTF-8):	XPCE - toolkit graficzny dla (SWI-)Prologu
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Obsoletes:	xpce

%description xpce
Graphical User Interface (GUI) toolkit for Prolog and other
dynamically typed languages. Provides Object Oriented programming to
Prolog as well as a high-level portable GUI toolkit for (SWI-)Prolog.
Also available for Quintus and SICStus Prolog.

%description xpce -l pl.UTF-8
Zestaw Graficzny Interfejsu Użytkownika (GUI) dla Prologu i innych
dynamicznie wpisywanych języków. Udostępnia obiektowo zorientowane
programowanie dla Prologu jak także jako wysoko dostępny przenośny
zestaw GUI dla (SWI-)Prologu. Dostępne także dla Quintus i SICStus
Prolog.

%prep
%setup -q
%patch0 -p1

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
LD_LIBRARY_PATH="$(pwd)/lib/%{_target_cpu}-linux"; export LD_LIBRARY_PATH

cd packages
wd=`pwd`
for i in xpce/src chr clib clpqr cpp cppproxy db http inclpr %{?with_java:jpl} mp nlp odbc pldoc plunit semweb sgml sgml/RDF ssl table uri zlib; do
	cd $i
	cp -f /usr/share/automake/config.sub .
	%{__aclocal}
	%{__autoconf}
	%{__autoheader} || :
	%configure
	%{__make}
	cd $wd
done
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install -C src \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/pl-%{version}/doc

LD_LIBRARY_PATH="$RPM_BUILD_ROOT%{_libdir}/pl-%{version}/lib/%{_target_cpu}-linux"; export LD_LIBRARY_PATH

for i in xpce/src chr clib clpqr cpp cppproxy db http inclpr %{?with_java:jpl} mp nlp odbc pldoc plunit semweb sgml sgml/RDF ssl table uri zlib; do
	PATH=$RPM_BUILD_ROOT%{_bindir}:$PATH \
	%{__make} -j1 install -C packages/$i \
		PLBASE=$RPM_BUILD_ROOT%{_libdir}/pl-%{version} \
		prefix=$RPM_BUILD_ROOT%{_prefix} \
		bindir=$RPM_BUILD_ROOT%{_bindir} \
		mandir=$RPM_BUILD_ROOT%{_mandir}/man1
done

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
%dir %{_libdir}/pl-%{version}/lib
%dir %{_libdir}/pl-%{version}/lib/*-linux
%attr(755,root,root) %{_libdir}/pl-%{version}/lib/*-linux/*.so*
%{_libdir}/pl-%{version}/lib/*-linux/*.a
%{_libdir}/pl-%{version}/library
%if %{with java}
%exclude %{_libdir}/pl-%{version}/lib/*-linux/libjpl.so
%exclude %{_libdir}/pl-%{version}/library/jpl.pl
%endif
%{_libdir}/pl-%{version}/include
%{_libdir}/pl-%{version}/do*
%{_libdir}/pl-%{version}/swipl
%{_libdir}/pl-%{version}/*.rc
%{_pkgconfigdir}/pl.pc
%{_mandir}/man?/pl*

%files xpce
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

%if %{with java}
%files jpl
%defattr(644,root,root,755)
%{_libdir}/pl-%{version}/lib/jpl.jar
%attr(755,root,root) %{_libdir}/pl-%{version}/lib/*-linux/libjpl.so
%{_libdir}/pl-%{version}/library/jpl.pl
%endif
