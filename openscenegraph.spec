%define	srcname	OpenSceneGraph

Summary:	A C++ scene graph API on OpenGL for real time graphics
Name:		openscenegraph
Version:	2.8.2
Release:	%mkrel 4
License:	LGPLv2+ with exceptions
Group:		System/Libraries
Source0:	http://www.openscenegraph.org/downloads/developer_releases/%{srcname}-%{version}.zip
Patch1:		OpenSceneGraph-2.6.1-linkage.patch
URL:		http://www.openscenegraph.org/
Provides:	OpenSceneGraph = %{version}-%{release}
Obsoletes:	OpenSceneGraph < 2.8.0-2
BuildRequires:	png-devel tiff-devel ungif-devel jpeg-devel jasper-devel
BuildRequires:	gdal-devel freetype2-devel mesaglut-devel libxine-devel
BuildRequires:	curl-devel gtk+2-devel gtkglext-devel librsvg-devel
BuildRequires:	wxgtku2.8-devel
BuildRequires:	libpoppler-glib-devel
BuildRequires:	cmake
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Open Scene Graph is a cross-platform C++/OpenGL library for the real-time 
visualization. Uses range from visual simulation, scientific modeling, virtual 
reality through to games.  Open Scene Graph employs good practices in software
engineering through the use of standard C++, STL and generic programming, and
design patterns.  Open Scene Graph strives for high performance and quality in
graphics rendering, portability, and extensibility.

%files
%defattr(-,root,root,-)
%doc AUTHORS.txt ChangeLog LICENSE.txt NEWS.txt README.txt
%doc doc/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/osgPlugins-%{version}

#------------------------------------------------------------------

%package devel
Summary:	Development package for %name
Group:		Development/C++
Provides:	OpenSceneGraph-devel = %{version}-%{release}
Obsoletes:	OpenSceneGraph-devel < 2.8.0-2
Requires:	%{name} = %{version}

%description devel
This package contains development files for %name

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/openscenegraph.pc
%{_libdir}/pkgconfig/openthreads.pc

#------------------------------------------------------------------

%prep
%setup -q -n %{srcname}-%{version}
%patch1 -p0

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std -C build

%clean
%{__rm} -rf %{buildroot}
