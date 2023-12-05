%global optflags %{optflags} -Wno-register

%define	srcname	OpenSceneGraph
%define	common_major 161

Summary:	A C++ scene graph API on OpenGL for real time graphics
Name:		openscenegraph
Version:	3.6.5
Release:	16
License:	LGPLv2+ with exceptions
Group:		System/Libraries
Url:		http://www.openscenegraph.org/
Source0:	https://github.com/openscenegraph/OpenSceneGraph/archive/%{srcname}-%{version}.tar.gz
Patch0:		osg-boost-1.78.patch
Patch1:		osg-3.6.5-opencascade-7.6.0.patch
# https://github.com/openscenegraph/OpenSceneGraph/issues/1111
Patch2:		https://patch-diff.githubusercontent.com/raw/openscenegraph/OpenSceneGraph/pull/951.patch
Patch3:		https://patch-diff.githubusercontent.com/raw/openscenegraph/OpenSceneGraph/pull/1246.patch

BuildConflicts:	pkgconfig(libavcodec)
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	gdal-devel
BuildRequires:	jpeg-devel
BuildRequires:	tiff-devel
BuildRequires:	ungif-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	ilmbase-devel >= 3.0
BuildRequires:	pkgconfig(libxine)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)
Provides:	OpenSceneGraph = %{EVRD}
Requires:	%{name}-plugins = %{EVRD}

%description
The Open Scene Graph is a cross-platform C++/OpenGL library for the real-time 
visualization. Uses range from visual simulation, scientific modeling, virtual 
reality through to games.  Open Scene Graph employs good practices in software
engineering through the use of standard C++, STL and generic programming, and
design patterns.  Open Scene Graph strives for high performance and quality in
graphics rendering, portability, and extensibility.

%files
%doc AUTHORS.txt ChangeLog LICENSE.txt NEWS.txt README.md
%doc doc/*
%{_bindir}/*

#----------------------------------------------------------------------------

%package plugins
Summary:	OpenSceneGraph plugins
Group:		System/Libraries

%description plugins
OpenSceneGraph plugins.

%files plugins
%{_libdir}/osgPlugins-%{version}

#----------------------------------------------------------------------------

%define OpenThreads_major 21
%define OpenThreads_version 3.3.1
%define oldlibOpenThreads %mklibname OpenThreads 21
%define libOpenThreads %mklibname OpenThreads

%package -n %{libOpenThreads}
Summary:	OpenSceneGraph shared library
Group:		System/Libraries
%rename %{oldlibOpenThreads}

%description -n %{libOpenThreads}
OpenSceneGraph shared library.

%files -n %{libOpenThreads}
%{_libdir}/libOpenThreads.so.%{OpenThreads_major}
%{_libdir}/libOpenThreads.so.%{OpenThreads_version}

#----------------------------------------------------------------------------

%define devOpenThreads %mklibname OpenThreads -d

%package -n %{devOpenThreads}
Summary:	OpenSceneGraph development files
Group:		Development/C++
Requires:	%{libOpenThreads} = %{EVRD}
Conflicts:	openscenegraph-devel < 3.2.0

%description -n %{devOpenThreads}
OpenSceneGraph development files.

%files -n %{devOpenThreads}
%{_includedir}/OpenThreads
%{_libdir}/libOpenThreads.so
%{_libdir}/pkgconfig/openthreads.pc

#----------------------------------------------------------------------------

%define osg_major %{common_major}
%define oldlibosg %mklibname osg 161
%define libosg %mklibname osg

%package -n %{libosg}
Summary:	OpenSceneGraph shared library
Group:		System/Libraries
%rename %{oldlibosg}

%description -n %{libosg}
OpenSceneGraph shared library.

%files -n %{libosg}
%{_libdir}/libosg.so.%{osg_major}
%{_libdir}/libosg.so.%{version}

#----------------------------------------------------------------------------

%define devosg %mklibname osg -d

%package -n %{devosg}
Summary:	OpenSceneGraph development files
Group:		Development/C++
Requires:	%{libosg} = %{EVRD}
Conflicts:	openscenegraph-devel < 3.2.0

%description -n %{devosg}
OpenSceneGraph development files.

%files -n %{devosg}
%{_includedir}/osg
%{_libdir}/libosg.so
%{_libdir}/pkgconfig/openscenegraph-osg.pc

#----------------------------------------------------------------------------

%define osgAnimation_major %{common_major}
%define oldlibosgAnimation %mklibname osgAnimation 161
%define libosgAnimation %mklibname osgAnimation

%package -n %{libosgAnimation}
Summary:	OpenSceneGraph shared library
Group:		System/Libraries
%rename %{oldlibosgAnimation}

%description -n %{libosgAnimation}
OpenSceneGraph shared library.

%files -n %{libosgAnimation}
%{_libdir}/libosgAnimation.so.%{osgAnimation_major}
%{_libdir}/libosgAnimation.so.%{version}

#----------------------------------------------------------------------------

%define devosgAnimation %mklibname osgAnimation -d

%package -n %{devosgAnimation}
Summary:	OpenSceneGraph development files
Group:		Development/C++
Requires:	%{libosgAnimation} = %{EVRD}
Conflicts:	openscenegraph-devel < 3.2.0

%description -n %{devosgAnimation}
OpenSceneGraph development files.

%files -n %{devosgAnimation}
%{_includedir}/osgAnimation
%{_libdir}/libosgAnimation.so
%{_libdir}/pkgconfig/openscenegraph-osgAnimation.pc

#----------------------------------------------------------------------------

%define osgDB_major %{common_major}
%define oldlibosgDB %mklibname osgDB 161
%define libosgDB %mklibname osgDB

%package -n %{libosgDB}
Summary:	OpenSceneGraph shared library
Group:		System/Libraries
%rename %{oldlibosgDB}

%description -n %{libosgDB}
OpenSceneGraph shared library.

%files -n %{libosgDB}
%{_libdir}/libosgDB.so.%{osgDB_major}
%{_libdir}/libosgDB.so.%{version}

#----------------------------------------------------------------------------

%define devosgDB %mklibname osgDB -d

%package -n %{devosgDB}
Summary:	OpenSceneGraph development files
Group:		Development/C++
Requires:	%{libosgDB} = %{EVRD}
Conflicts:	openscenegraph-devel < 3.2.0

%description -n %{devosgDB}
OpenSceneGraph development files.

%files -n %{devosgDB}
%{_includedir}/osgDB
%{_libdir}/libosgDB.so
%{_libdir}/pkgconfig/openscenegraph-osgDB.pc

#----------------------------------------------------------------------------

%define osgFX_major %{common_major}
%define oldlibosgFX %mklibname osgFX 161
%define libosgFX %mklibname osgFX

%package -n %{libosgFX}
Summary:	OpenSceneGraph shared library
Group:		System/Libraries
%rename %{oldlibosgFX}

%description -n %{libosgFX}
OpenSceneGraph shared library.

%files -n %{libosgFX}
%{_libdir}/libosgFX.so.%{osgFX_major}
%{_libdir}/libosgFX.so.%{version}

#----------------------------------------------------------------------------

%define devosgFX %mklibname osgFX -d

%package -n %{devosgFX}
Summary:	OpenSceneGraph development files
Group:		Development/C++
Requires:	%{libosgFX} = %{EVRD}
Conflicts:	openscenegraph-devel < 3.2.0

%description -n %{devosgFX}
OpenSceneGraph development files.

%files -n %{devosgFX}
%{_includedir}/osgFX
%{_libdir}/libosgFX.so
%{_libdir}/pkgconfig/openscenegraph-osgFX.pc

#----------------------------------------------------------------------------

%define osgGA_major %{common_major}
%define oldlibosgGA %mklibname osgGA 161
%define libosgGA %mklibname osgGA

%package -n %{libosgGA}
Summary:	OpenSceneGraph shared library
Group:		System/Libraries
%rename %{oldlibosgGA}

%description -n %{libosgGA}
OpenSceneGraph shared library.

%files -n %{libosgGA}
%{_libdir}/libosgGA.so.%{osgGA_major}
%{_libdir}/libosgGA.so.%{version}

#----------------------------------------------------------------------------

%define devosgGA %mklibname osgGA -d

%package -n %{devosgGA}
Summary:	OpenSceneGraph development files
Group:		Development/C++
Requires:	%{libosgGA} = %{EVRD}
Conflicts:	openscenegraph-devel < 3.2.0

%description -n %{devosgGA}
OpenSceneGraph development files.

%files -n %{devosgGA}
%{_includedir}/osgGA
%{_libdir}/libosgGA.so
%{_libdir}/pkgconfig/openscenegraph-osgGA.pc

#----------------------------------------------------------------------------

%define osgManipulator_major %{common_major}
%define oldlibosgManipulator %mklibname osgManipulator 161
%define libosgManipulator %mklibname osgManipulator

%package -n %{libosgManipulator}
Summary:	OpenSceneGraph shared library
Group:		System/Libraries
%rename %{oldlibosgManipulator}

%description -n %{libosgManipulator}
OpenSceneGraph shared library.

%files -n %{libosgManipulator}
%{_libdir}/libosgManipulator.so.%{osgManipulator_major}
%{_libdir}/libosgManipulator.so.%{version}

#----------------------------------------------------------------------------

%define devosgManipulator %mklibname osgManipulator -d

%package -n %{devosgManipulator}
Summary:	OpenSceneGraph development files
Group:		Development/C++
Requires:	%{libosgManipulator} = %{EVRD}
Conflicts:	openscenegraph-devel < 3.2.0

%description -n %{devosgManipulator}
OpenSceneGraph development files.

%files -n %{devosgManipulator}
%{_includedir}/osgManipulator
%{_libdir}/libosgManipulator.so
%{_libdir}/pkgconfig/openscenegraph-osgManipulator.pc

#----------------------------------------------------------------------------

%define osgParticle_major %{common_major}
%define oldlibosgParticle %mklibname osgParticle 161
%define libosgParticle %mklibname osgParticle

%package -n %{libosgParticle}
Summary:	OpenSceneGraph shared library
Group:		System/Libraries
%rename %{oldlibosgParticle}

%description -n %{libosgParticle}
OpenSceneGraph shared library.

%files -n %{libosgParticle}
%{_libdir}/libosgParticle.so.%{osgParticle_major}
%{_libdir}/libosgParticle.so.%{version}

#----------------------------------------------------------------------------

%define devosgParticle %mklibname osgParticle -d

%package -n %{devosgParticle}
Summary:	OpenSceneGraph development files
Group:		Development/C++
Requires:	%{libosgParticle} = %{EVRD}
Conflicts:	openscenegraph-devel < 3.2.0

%description -n %{devosgParticle}
OpenSceneGraph development files.

%files -n %{devosgParticle}
%{_includedir}/osgParticle
%{_libdir}/libosgParticle.so
%{_libdir}/pkgconfig/openscenegraph-osgParticle.pc

#----------------------------------------------------------------------------

%define osgPresentation_major %{common_major}
%define oldlibosgPresentation %mklibname osgPresentation 161
%define libosgPresentation %mklibname osgPresentation

%package -n %{libosgPresentation}
Summary:	OpenSceneGraph shared library
Group:		System/Libraries
%rename %{oldlibosgPresentation}

%description -n %{libosgPresentation}
OpenSceneGraph shared library.

%files -n %{libosgPresentation}
%{_libdir}/libosgPresentation.so.%{osgPresentation_major}
%{_libdir}/libosgPresentation.so.%{version}

#----------------------------------------------------------------------------

%define devosgPresentation %mklibname osgPresentation -d

%package -n %{devosgPresentation}
Summary:	OpenSceneGraph development files
Group:		Development/C++
Requires:	%{libosgPresentation} = %{EVRD}
Conflicts:	openscenegraph-devel < 3.2.0

%description -n %{devosgPresentation}
OpenSceneGraph development files.

%files -n %{devosgPresentation}
%{_includedir}/osgPresentation
%{_libdir}/libosgPresentation.so

#----------------------------------------------------------------------------

%define osgShadow_major %{common_major}
%define oldlibosgShadow %mklibname osgShadow 161
%define libosgShadow %mklibname osgShadow

%package -n %{libosgShadow}
Summary:	OpenSceneGraph shared library
Group:		System/Libraries
%rename %{oldlibosgShadow}

%description -n %{libosgShadow}
OpenSceneGraph shared library.

%files -n %{libosgShadow}
%{_libdir}/libosgShadow.so.%{osgShadow_major}
%{_libdir}/libosgShadow.so.%{version}

#----------------------------------------------------------------------------

%define devosgShadow %mklibname osgShadow -d

%package -n %{devosgShadow}
Summary:	OpenSceneGraph development files
Group:		Development/C++
Requires:	%{libosgShadow} = %{EVRD}
Conflicts:	openscenegraph-devel < 3.2.0

%description -n %{devosgShadow}
OpenSceneGraph development files.

%files -n %{devosgShadow}
%{_includedir}/osgShadow
%{_libdir}/libosgShadow.so
%{_libdir}/pkgconfig/openscenegraph-osgShadow.pc

#----------------------------------------------------------------------------

%define osgSim_major %{common_major}
%define oldlibosgSim %mklibname osgSim 161
%define libosgSim %mklibname osgSim

%package -n %{libosgSim}
Summary:	OpenSceneGraph shared library
Group:		System/Libraries
%rename %{oldlibosgSim}

%description -n %{libosgSim}
OpenSceneGraph shared library.

%files -n %{libosgSim}
%{_libdir}/libosgSim.so.%{osgSim_major}
%{_libdir}/libosgSim.so.%{version}

#----------------------------------------------------------------------------

%define devosgSim %mklibname osgSim -d

%package -n %{devosgSim}
Summary:	OpenSceneGraph development files
Group:		Development/C++
Requires:	%{libosgSim} = %{EVRD}
Conflicts:	openscenegraph-devel < 3.2.0

%description -n %{devosgSim}
OpenSceneGraph development files.

%files -n %{devosgSim}
%{_includedir}/osgSim
%{_libdir}/libosgSim.so
%{_libdir}/pkgconfig/openscenegraph-osgSim.pc

#----------------------------------------------------------------------------

%define osgTerrain_major %{common_major}
%define oldlibosgTerrain %mklibname osgTerrain 161
%define libosgTerrain %mklibname osgTerrain

%package -n %{libosgTerrain}
Summary:	OpenSceneGraph shared library
Group:		System/Libraries
%rename %{oldlibosgTerrain}

%description -n %{libosgTerrain}
OpenSceneGraph shared library.

%files -n %{libosgTerrain}
%{_libdir}/libosgTerrain.so.%{osgTerrain_major}
%{_libdir}/libosgTerrain.so.%{version}

#----------------------------------------------------------------------------

%define devosgTerrain %mklibname osgTerrain -d

%package -n %{devosgTerrain}
Summary:	OpenSceneGraph development files
Group:		Development/C++
Requires:	%{libosgTerrain} = %{EVRD}
Conflicts:	openscenegraph-devel < 3.2.0

%description -n %{devosgTerrain}
OpenSceneGraph development files.

%files -n %{devosgTerrain}
%{_includedir}/osgTerrain
%{_libdir}/libosgTerrain.so
%{_libdir}/pkgconfig/openscenegraph-osgTerrain.pc

#----------------------------------------------------------------------------

%define osgText_major %{common_major}
%define oldlibosgText %mklibname osgText 161
%define libosgText %mklibname osgText

%package -n %{libosgText}
Summary:	OpenSceneGraph shared library
Group:		System/Libraries
%rename %{oldlibosgText}

%description -n %{libosgText}
OpenSceneGraph shared library.

%files -n %{libosgText}
%{_libdir}/libosgText.so.%{osgText_major}
%{_libdir}/libosgText.so.%{version}

#----------------------------------------------------------------------------

%define devosgText %mklibname osgText -d

%package -n %{devosgText}
Summary:	OpenSceneGraph development files
Group:		Development/C++
Requires:	%{libosgText} = %{EVRD}
Conflicts:	openscenegraph-devel < 3.2.0

%description -n %{devosgText}
OpenSceneGraph development files.

%files -n %{devosgText}
%{_includedir}/osgText
%{_libdir}/libosgText.so
%{_libdir}/pkgconfig/openscenegraph-osgText.pc

#----------------------------------------------------------------------------

%define osgUI_major %{common_major}
%define oldlibosgUI %mklibname osgUI 161
%define libosgUI %mklibname osgUI

%package -n %{libosgUI}
Summary:        OpenSceneGraph shared library
Group:          System/Libraries
%rename %{oldlibosgUI}

%description -n %{libosgUI}
OpenSceneGraph shared library.

%files -n %{libosgUI}
%{_libdir}/libosgUI.so.%{osgUI_major}
%{_libdir}/libosgUI.so.%{version}

#----------------------------------------------------------------------------

%define devosgUI %mklibname osgUI -d

%package -n %{devosgUI}
Summary:        OpenSceneGraph development files
Group:          Development/C++
Requires:       %{libosgUI} = %{EVRD}
Conflicts:      openscenegraph-devel < 3.2.0

%description -n %{devosgUI}
OpenSceneGraph development files.

%files -n %{devosgUI}
%{_includedir}/osgUI
%{_libdir}/libosgUI.so

#----------------------------------------------------------------------------

%define osgUtil_major %{common_major}
%define oldlibosgUtil %mklibname osgUtil 161
%define libosgUtil %mklibname osgUtil

%package -n %{libosgUtil}
Summary:	OpenSceneGraph shared library
Group:		System/Libraries
%rename %{oldlibosgUtil}

%description -n %{libosgUtil}
OpenSceneGraph shared library.

%files -n %{libosgUtil}
%{_libdir}/libosgUtil.so.%{osgUtil_major}
%{_libdir}/libosgUtil.so.%{version}

#----------------------------------------------------------------------------

%define devosgUtil %mklibname osgUtil -d

%package -n %{devosgUtil}
Summary:	OpenSceneGraph development files
Group:		Development/C++
Requires:	%{libosgUtil} = %{EVRD}
Conflicts:	openscenegraph-devel < 3.2.0

%description -n %{devosgUtil}
OpenSceneGraph development files.

%files -n %{devosgUtil}
%{_includedir}/osgUtil
%{_libdir}/libosgUtil.so
%{_libdir}/pkgconfig/openscenegraph-osgUtil.pc

#----------------------------------------------------------------------------

%define osgViewer_major %{common_major}
%define oldlibosgViewer %mklibname osgViewer 161
%define libosgViewer %mklibname osgViewer

%package -n %{libosgViewer}
Summary:	OpenSceneGraph shared library
Group:		System/Libraries
%rename %{oldlibosgViewer}

%description -n %{libosgViewer}
OpenSceneGraph shared library.

%files -n %{libosgViewer}
%{_libdir}/libosgViewer.so.%{osgViewer_major}
%{_libdir}/libosgViewer.so.%{version}

#----------------------------------------------------------------------------

%define devosgViewer %mklibname osgViewer -d

%package -n %{devosgViewer}
Summary:	OpenSceneGraph development files
Group:		Development/C++
Requires:	%{libosgViewer} = %{EVRD}
Conflicts:	openscenegraph-devel < 3.2.0

%description -n %{devosgViewer}
OpenSceneGraph development files.

%files -n %{devosgViewer}
%{_includedir}/osgViewer
%{_libdir}/libosgViewer.so
%{_libdir}/pkgconfig/openscenegraph-osgViewer.pc

#----------------------------------------------------------------------------

%define osgVolume_major %{common_major}
%define oldlibosgVolume %mklibname osgVolume 161
%define libosgVolume %mklibname osgVolume

%package -n %{libosgVolume}
Summary:	OpenSceneGraph shared library
Group:		System/Libraries
%rename %{oldlibosgVolume}

%description -n %{libosgVolume}
OpenSceneGraph shared library.

%files -n %{libosgVolume}
%{_libdir}/libosgVolume.so.%{osgVolume_major}
%{_libdir}/libosgVolume.so.%{version}

#----------------------------------------------------------------------------

%define devosgVolume %mklibname osgVolume -d

%package -n %{devosgVolume}
Summary:	OpenSceneGraph development files
Group:		Development/C++
Requires:	%{libosgVolume} = %{EVRD}
Conflicts:	openscenegraph-devel < 3.2.0

%description -n %{devosgVolume}
OpenSceneGraph development files.

%files -n %{devosgVolume}
%{_includedir}/osgVolume
%{_libdir}/libosgVolume.so
%{_libdir}/pkgconfig/openscenegraph-osgVolume.pc

#----------------------------------------------------------------------------

%define osgWidget_major %{common_major}
%define oldlibosgWidget %mklibname osgWidget 161
%define libosgWidget %mklibname osgWidget

%package -n %{libosgWidget}
Summary:	OpenSceneGraph shared library
Group:		System/Libraries
%rename %{oldlibosgWidget}

%description -n %{libosgWidget}
OpenSceneGraph shared library.

%files -n %{libosgWidget}
%{_libdir}/libosgWidget.so.%{osgWidget_major}
%{_libdir}/libosgWidget.so.%{version}

#----------------------------------------------------------------------------

%define devosgWidget %mklibname osgWidget -d

%package -n %{devosgWidget}
Summary:	OpenSceneGraph development files
Group:		Development/C++
Requires:	%{libosgWidget} = %{EVRD}
Conflicts:	openscenegraph-devel < 3.2.0

%description -n %{devosgWidget}
OpenSceneGraph development files.

%files -n %{devosgWidget}
%{_includedir}/osgWidget
%{_libdir}/libosgWidget.so
%{_libdir}/pkgconfig/openscenegraph-osgWidget.pc

#----------------------------------------------------------------------------

%package devel
Summary:	Development package for %{name}
Group:		Development/C++
Provides:	OpenSceneGraph-devel = %{EVRD}
Requires:	%{devOpenThreads} = %{EVRD}
Requires:	%{devosg} = %{EVRD}
Requires:	%{devosgAnimation} = %{EVRD}
Requires:	%{devosgDB} = %{EVRD}
Requires:	%{devosgFX} = %{EVRD}
Requires:	%{devosgGA} = %{EVRD}
Requires:	%{devosgManipulator} = %{EVRD}
Requires:	%{devosgParticle} = %{EVRD}
Requires:	%{devosgPresentation} = %{EVRD}
Requires:	%{devosgShadow} = %{EVRD}
Requires:	%{devosgSim} = %{EVRD}
Requires:	%{devosgTerrain} = %{EVRD}
Requires:	%{devosgText} = %{EVRD}
Requires:	%{devosgUI} = %{EVRD}
Requires:	%{devosgUtil} = %{EVRD}
Requires:	%{devosgViewer} = %{EVRD}
Requires:	%{devosgVolume} = %{EVRD}
Requires:	%{devosgWidget} = %{EVRD}

%description devel
This package contains development files for %{name}

%files devel
%{_libdir}/pkgconfig/openscenegraph.pc

#----------------------------------------------------------------------------

%prep
%setup -qn %{srcname}-%{srcname}-%{version}
%autopatch -p1

%build
#CFLAGS="%{optflags} -pthread"
#CXXFLAGS="%{optflags} -pthread"
%cmake \
%ifarch aarch64 %{x86_64} riscv64 ppc64 ppc64le
	-DLIB_POSTFIX=64 \
%endif
	-DCMAKE_RELWITHDEBINFO_POSTFIX="" \
	-G Ninja

VERBOSE=true %ninja_build

%install
%ninja_install -C build
