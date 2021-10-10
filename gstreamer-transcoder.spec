# NOTE: since 1.18.0 it's merged into gstreamer-plugins-bad.spec
%define         gst_ver         1.16.0
%define         gstpb_ver       1.16.0
Summary:	High level API to do media transcoding with GStreamer
Summary(pl.UTF-8):	Wysokopoziomowe API do przekodowywania multimediów przy użyciu GSteamera
Name:		gstreamer-transcoder
Version:	1.16.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/pitivi/gst-transcoder/releases
Source0:	https://github.com/pitivi/gst-transcoder/archive/%{version}/gst-transcoder-%{version}.tar.gz
# Source0-md5:	dbad5b5431958078a6aceba0fa808bbd
URL:		https://github.com/pitivi/gst-transcoder
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gobject-introspection-devel
BuildRequires:	gstreamer-devel >= %{gst_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gstpb_ver}
BuildRequires:	gtk-doc
BuildRequires:	meson >= 0.36.0
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
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
Requires:	gstreamer-devel >= %{gst_ver}
Requires:	gstreamer-plugins-base-devel >= %{gstpb_ver}

%description devel
Header files for gst-transcoder library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gst-transcoder.

%package apidocs
Summary:	API documentation for gst-transcoder library
Summary(pl.UTF-8):	Dokumentacja API biblioteki gst-transcoder
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for gst-transcoder library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gst-transcoder.

%prep
%setup -q -n gst-transcoder-%{version}

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
