%global  kf_version 6.6.0

Name:		kf6-kquickcharts
Summary:	A QtQuick module providing high-performance charts
Version:	6.6.0
Release:	0%{?dist}
License:	BSD-2-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}

Source0:    %{name}-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:	clang
BuildRequires:  kf6-extra-cmake-modules >= %{kf_version}
BuildRequires:  kf6-rpm-macros
BuildRequires:	qt6-qtdeclarative-devel
BuildRequires:	qt6-qtshadertools-devel
BuildRequires:	make
BuildRequires:	pkgconfig(xkbcommon)

%description
The Quick Charts module provides a set of charts that can be used from QtQuick
applications. They are intended to be used for both simple display of data as
well as continuous display of high-volume data (often referred to as plotters).
The charts use a system called distance fields for their accelerated rendering,
which provides ways of using the GPU for rendering 2D shapes without loss of
quality.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/kquickcharts.*
%{_kf6_qmldir}/org/kde/quickcharts/
%{_libdir}/libQuickCharts.so.*
%{_libdir}/libQuickChartsControls.so*

%files devel
%{_kf6_libdir}/cmake/KF6QuickCharts/
%{_libdir}/libQuickCharts.so
%{_libdir}/libQuickChartsControls.so
