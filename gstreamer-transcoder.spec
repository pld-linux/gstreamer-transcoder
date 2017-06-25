Summary:	High level API to do media transcoding with GStreamer
Summary(pl.UTF-8):	Wysokopoziomowe API do przekodowywania multimediów przy użyciu GSteamera
Name:		gstreamer-transcoder
Version:	1.12.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/pitivi/gst-transcoder/releases
Source0:	https://github.com/pitivi/gst-transcoder/archive/%{version}/gst-transcoder-%{version}.tar.gz
# Source0-md5:	5845018d8000eda8f5aadcb4b75fc46b
URL:		https://github.com/pitivi/gst-transcoder
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gobject-introspection-devel
BuildRequires:	gstreamer-devel >= 1.12.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.12.0
BuildRequires:	gtk-doc
BuildRequires:	meson >= 0.36.0
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
High level API to do media transcoding with GStreamer.

%description -l pl.UTF-8
Wysokopoziomowe API do przekodowywania multimediów przy użyciu
GSteamera.

%package devel
Summary:	Header files for gst-transcoder library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gst-transcoder
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer-devel >= 1.12.0
Requires:	gstreamer-plugins-base-devel >= 1.12.0

%description devel
Header files for gst-transcoder library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gst-transcoder.

%package apidocs
Summary:	API documentation for gst-transcoder library
Summary(pl.UTF-8):	Dokumentacja API biblioteki gst-transcoder
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for gst-transcoder library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gst-transcoder.

%prep
%setup -q -n gst-transcoder-%{version}

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags} %{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
meson build \
	--buildtype=plain \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

ninja -C build -v

%install
rm -rf $RPM_BUILD_ROOT

DESTDIR=$RPM_BUILD_ROOT \
ninja -C build -v install

install -d $RPM_BUILD_ROOT%{_gtkdocdir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/* $RPM_BUILD_ROOT%{_gtkdocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gst-transcoder-1.0
%attr(755,root,root) %{_libdir}/libgsttranscoder-1.0.so.0
%{_libdir}/girepository-1.0/GstTranscoder-1.0.typelib
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libgsttranscode.so
# XXX: shared dir
%dir %{_datadir}/gstreamer-1.0
%{_datadir}/gstreamer-1.0/encoding-profiles

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgsttranscoder-1.0.so
%{_includedir}/gstreamer-1.0/gst/transcoder
%{_datadir}/gir-1.0/GstTranscoder-1.0.gir
%{_pkgconfigdir}/gst-transcoder-1.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gstreamer-transcoder
