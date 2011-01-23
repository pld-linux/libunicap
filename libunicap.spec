Summary:	Library to access differend kinds of video capturing devices
Summary(pl.UTF-8):	Biblioteka dostępu do różnych urządzeń przechwytujących obraz
Name:		libunicap
Version:	0.9.12
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: http://unicap-imaging.org/download.htm
Source0:	http://unicap-imaging.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	353657b4da519251d4cc6dee5a232391
URL:		http://unicap-imaging.org/
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	libraw1394-devel >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unicap is a library to access different kinds of (video) capture
devices.

Currently unicap provides support for IIDC cameras, Video4Linux,
Video4Linux2 and video-to-firewire converters.

%description -l pl.UTF-8
unicap to biblioteka dostępu do różnych rodzajów urządzeń
przechwytujących obraz.

Obecnie obsługuje kamery IIDC, Video4Linux, Video4Linux2 oraz
z interfejsem FireWire.

%package devel
Summary:	Header files for unicap library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki unicap
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for unicap library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki unicap.

%package static
Summary:	Static unicap library
Summary(pl.UTF-8):	Statyczna biblioteka unicap
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static unicap library.

%description static -l pl.UTF-8
Statyczna biblioteka unicap.

%package apidocs
Summary:	unicap API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki unicap
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API documentation for unicap library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki unicap.

%package -n udev-libunicap
Summary:	Udev rules for unicap-supported devices
Summary(pl.UTF-8):	Reguły udeva dla urządzeń obsługiwanych przez unicap
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	udev-core

%description -n udev-libunicap
Udev rules for unicap-supported devices.

%description -n udev-libunicap -l pl.UTF-8
Reguły udeva dla urządzeń obsługiwanych przez unicap.

%prep
%setup -q

%build
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/unicap2/cpi/lib*.{la,a}

%find_lang unicap

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f unicap.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libunicap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libunicap.so.2
%dir %{_libdir}/unicap2
%dir %{_libdir}/unicap2/cpi
%attr(755,root,root) %{_libdir}/unicap2/cpi/libdcam.so
%attr(755,root,root) %{_libdir}/unicap2/cpi/libeuvccam_cpi.so
%attr(755,root,root) %{_libdir}/unicap2/cpi/libv4l.so
%attr(755,root,root) %{_libdir}/unicap2/cpi/libv4l2cpi.so
%attr(755,root,root) %{_libdir}/unicap2/cpi/libvid21394.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libunicap.so
%{_libdir}/libunicap.la
%{_includedir}/unicap
%{_pkgconfigdir}/libunicap.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libunicap.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libunicap

%files -n udev-libunicap
%defattr(644,root,root,755)
/etc/udev/rules.d/50-euvccam.rules
