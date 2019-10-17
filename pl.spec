#
# TODO
#	- maybe separate other prolog packages to rpm subpackages
#
# Conditional build:
%bcond_without	java		# Java bindings (so far, JPL only works with Sun Java and IBM Java)
%bcond_without	tests		# make check
#

%ifnarch %{x8664} i586 i686 pentium3 pentium4 athlon
%undefine	with_java
%endif

# packages use SWI-Prolog own linker which doesn't understand -gdwarf* and
# some -march= options passed to it by gcc
# No poin in building debug packages without debug info
%define		_enable_debug_packages	0

Summary:	SWI Prolog Language
Summary(pl.UTF-8):	Język SWI Prolog
Name:		pl
Version:	7.2.3
Release:	4
License:	LGPL v2.1+
Group:		Development/Languages
#Source0Download: http://www.swi-prolog.org/download/stable
Source0:	http://www.swi-prolog.org/download/stable/src/swi%{name}-%{version}.tar.gz
# Source0-md5:	67c182f18310f115b49f1e2195499e0c
Patch0:		%{name}-clib-configure.patch
Patch1:		%{name}-xpce-install.patch
Patch2:		%{name}-format.patch
Patch3:		%{name}-jni.patch
URL:		http://www.swi-prolog.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gmp-devel >= 4.2.0
%{?with_java:BuildRequires:	jdk}
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
Requires:	gmp >= 4.2.0
Obsoletes:	swi-pl
Obsoletes:	swi-prolog
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_chrpath		1

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
Requires:	jdk

%description jpl
JPL 3.x is a dynamic, bidirectional interface between SWI-Prolog 5.2.0
or later and Java 2 runtimes (see JPL 3.x Objectives). It offers two
APIs:
 * Java API (Java-calls-Prolog): this interface comprises public Java
   classes which support:
    + constructing Java representations of Prolog terms and queries
    + calling queries within SWI-Prolog engines
    + retrieving (as Java representations of Prolog terms) any
      bindings created by a call
 * Prolog API (Prolog-calls-Java): this interface comprises Prolog
   library predicates which support:
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
%setup -q -n swi%{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{__mv} src/Tests/core/test_d_break.pl{,disabled}

%build
# packages use SWI-Prolog own linker which doesn't understand -gdwarf* and
# some -march= options passed to it by gcc
CFLAGS=$(echo %{rpmcflags} | sed 's|-march=[^ ]*||')
export CFLAGS

cd src
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure \
	PLARCH=%{_target_platform}
%{__make}
cd ..

# the packages are written in Prolog itself
PATH="$(pwd)/src:$PATH"; export PATH
LD_LIBRARY_PATH="$(pwd)/lib/%{_target_platform}"; export LD_LIBRARY_PATH
export CLASSPATH=.

cd packages
wd=`pwd`
# see packages/configure for default packages list and their order
for i in clib cpp odbc table xpce/src sgml RDF semweb http chr \
		clpqr nlp ssl tipc pldoc plunit %{?with_java:jpl} \
		zlib protobufs PDT utf8proc archive pengines cql \
		inclpr ; do
	cd $i
	cp -f /usr/share/automake/config.sub .
	%{__aclocal}
	%{__autoconf}
	grep -q AC_CONFIG_HEADER configure.in && %{__autoheader}
	# ac_cv_prog_uudecode_base64=no is a hack to compile Test.class instead of
	# using included one which fails with Sun/Oracle JDK 1.6 [needed for jpl]
	%configure \
		ac_cv_prog_uudecode_base64=no
	%{__make}
	cd $wd
done
cd ..

%{?with_tests:%{__make} -C src check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install -C src \
	DESTDIR=$RPM_BUILD_ROOT

LD_LIBRARY_PATH="$RPM_BUILD_ROOT%{_libdir}/swipl-%{version}/lib/%{_target_platform}"; export LD_LIBRARY_PATH

for i in clib cpp odbc table xpce/src sgml RDF semweb http chr \
		clpqr nlp ssl tipc pldoc plunit %{?with_java:jpl} \
		zlib protobufs PDT utf8proc archive pengines cql \
		inclpr ; do
	PATH=$RPM_BUILD_ROOT%{_bindir}:$PATH \
	%{__make} -j1 install -C packages/$i \
		PLBASE=$RPM_BUILD_ROOT%{_libdir}/swipl-%{version} \
		prefix=$RPM_BUILD_ROOT%{_prefix} \
		bindir=$RPM_BUILD_ROOT%{_bindir} \
		mandir=$RPM_BUILD_ROOT%{_mandir}/man1
done

# packaged as doc
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/swipl-%{version}/{customize,xpce/{COPYING,README}}
# no need to package
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/swipl-%{version}/demo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ReleaseNotes/relnotes-* customize
%attr(755,root,root) %{_bindir}/swipl*
%dir %{_libdir}/swipl-%{version}
%{_libdir}/swipl-%{version}/Makefile
%attr(755,root,root) %{_libdir}/swipl-%{version}/bin
%{_libdir}/swipl-%{version}/boot*
%dir %{_libdir}/swipl-%{version}/lib
%dir %{_libdir}/swipl-%{version}/lib/%{_target_platform}
%attr(755,root,root) %{_libdir}/swipl-%{version}/lib/%{_target_platform}/*.so*
%{_libdir}/swipl-%{version}/lib/%{_target_platform}/*.a
%{_libdir}/swipl-%{version}/library
%if %{with java}
%exclude %{_libdir}/swipl-%{version}/lib/%{_target_platform}/libjpl.so
%exclude %{_libdir}/swipl-%{version}/library/jpl.pl
%endif
%{_libdir}/swipl-%{version}/include
%{_libdir}/swipl-%{version}/do*
%{_libdir}/swipl-%{version}/*.rc
%{_libdir}/swipl-%{version}/swipl.home
%{_pkgconfigdir}/swipl.pc
%{_mandir}/man1/swipl*.1*

%files xpce
%defattr(644,root,root,755)
%doc packages/xpce/{EXTENDING,INFO,README,README.CXX,README.customise}
%attr(755,root,root) %{_bindir}/xpce-client
%dir %{_libdir}/swipl-%{version}/xpce
%{_libdir}/swipl-%{version}/xpce/Defaults*
%attr(755,root,root) %{_libdir}/swipl-%{version}/xpce/bin
%{_libdir}/swipl-%{version}/xpce/appl-help
%{_libdir}/swipl-%{version}/xpce/bitmaps
%{_libdir}/swipl-%{version}/xpce/man
%{_libdir}/swipl-%{version}/xpce/pl
%{_libdir}/swipl-%{version}/xpce/prolog

%if %{with java}
%files jpl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/swipl-%{version}/lib/%{_target_platform}/libjpl.so
%{_libdir}/swipl-%{version}/lib/jpl.jar
%{_libdir}/swipl-%{version}/library/jpl.pl
%endif
