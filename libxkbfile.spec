#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v3
# autospec commit: 750e50d
#
# Source0 file verified with key 0xCFDF148828C642A7 (alanc@freedesktop.org)
#
Name     : libxkbfile
Version  : 1.1.3
Release  : 17
URL      : https://www.x.org/releases/individual/lib/libxkbfile-1.1.3.tar.gz
Source0  : https://www.x.org/releases/individual/lib/libxkbfile-1.1.3.tar.gz
Source1  : https://www.x.org/releases/individual/lib/libxkbfile-1.1.3.tar.gz.sig
Summary  : The xkbfile Library
Group    : Development/Tools
License  : HPND
Requires: libxkbfile-lib = %{version}-%{release}
Requires: libxkbfile-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : pkgconfig(kbproto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xorg-macros)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libxkbfile - XKB file handling routines
---------------------------------------
libxkbfile is used by the X servers and utilities to parse the XKB
configuration data files.

%package dev
Summary: dev components for the libxkbfile package.
Group: Development
Requires: libxkbfile-lib = %{version}-%{release}
Provides: libxkbfile-devel = %{version}-%{release}
Requires: libxkbfile = %{version}-%{release}

%description dev
dev components for the libxkbfile package.


%package lib
Summary: lib components for the libxkbfile package.
Group: Libraries
Requires: libxkbfile-license = %{version}-%{release}

%description lib
lib components for the libxkbfile package.


%package license
Summary: license components for the libxkbfile package.
Group: Default

%description license
license components for the libxkbfile package.


%prep
%setup -q -n libxkbfile-1.1.3
cd %{_builddir}/libxkbfile-1.1.3
pushd ..
cp -a libxkbfile-1.1.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707156206
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707156206
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libxkbfile
cp %{_builddir}/libxkbfile-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libxkbfile/4f35a76dbcc982e002982b97c5d93f3d95c5e57f || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/XKBbells.h
/usr/include/X11/extensions/XKBconfig.h
/usr/include/X11/extensions/XKBfile.h
/usr/include/X11/extensions/XKBrules.h
/usr/include/X11/extensions/XKM.h
/usr/include/X11/extensions/XKMformat.h
/usr/lib64/libxkbfile.so
/usr/lib64/pkgconfig/xkbfile.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libxkbfile.so.1.0.2
/usr/lib64/libxkbfile.so.1
/usr/lib64/libxkbfile.so.1.0.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libxkbfile/4f35a76dbcc982e002982b97c5d93f3d95c5e57f
