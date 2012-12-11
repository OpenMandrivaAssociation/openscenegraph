%define	srcname	OpenSceneGraph

Summary:	A C++ scene graph API on OpenGL for real time graphics
Name:		openscenegraph
Version:	3.0.1
Release:	2
License:	LGPLv2+ with exceptions
Group:		System/Libraries
URL:		http://www.openscenegraph.org/
Source0:	http://www.openscenegraph.org/downloads/developer_releases/%{srcname}-%{version}.zip
Patch0:		OpenSceneGraph-3.0.1-xine1.2.patch
Patch2:		OpenSceneGraph-2.8.3-ffmpeg.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(libpng)
BuildRequires:	tiff-devel
BuildRequires:	ungif-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(jasper)
BuildRequires:	gdal-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libxine)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkglext-1.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	wxgtku2.8-devel
BuildRequires:	itk-devel
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	ffmpeg0.7-devel
Provides:	OpenSceneGraph = %{version}-%{release}
Obsoletes:	OpenSceneGraph < 2.8.0-2

%description
The Open Scene Graph is a cross-platform C++/OpenGL library for the real-time 
visualization. Uses range from visual simulation, scientific modeling, virtual 
reality through to games.  Open Scene Graph employs good practices in software
engineering through the use of standard C++, STL and generic programming, and
design patterns.  Open Scene Graph strives for high performance and quality in
graphics rendering, portability, and extensibility.

%files
%doc AUTHORS.txt ChangeLog LICENSE.txt NEWS.txt README.txt
%doc doc/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/osgPlugins-%{version}

#------------------------------------------------------------------

%package devel
Summary:	Development package for %{name}
Group:		Development/C++
Provides:	OpenSceneGraph-devel = %{version}-%{release}
Obsoletes:	OpenSceneGraph-devel < 2.8.0-2
Requires:	%{name} = %{version}

%description devel
This package contains development files for %{name}

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#------------------------------------------------------------------

%prep
%setup -qn %{srcname}-%{version}
%patch0 -p0
%patch2 -p0

%build
CFLAGS="%{optflags} -pthread"
CXXFLAGS="%{optflags} -pthread"
%cmake
%make VERBOSE=TRUE

%install
%makeinstall_std -C build

%changelog
* Mon Sep 19 2011 Andrey Bondrov <abondrov@mandriva.org> 3.0.1-1
+ Revision: 700386
- More BuildRequires
- New version: 3.0.1

* Wed Jun 15 2011 Funda Wang <fwang@mandriva.org> 2.8.5-1
+ Revision: 685221
- new version 2.8.5
- New version 2.8.3

* Thu Dec 30 2010 Funda Wang <fwang@mandriva.org> 2.8.2-5mdv2011.0
+ Revision: 626157
- rebuild for new poppler

* Sat Jan 16 2010 Funda Wang <fwang@mandriva.org> 2.8.2-4mdv2011.0
+ Revision: 492261
- rebuild for new libjpeg v8

* Thu Oct 01 2009 Funda Wang <fwang@mandriva.org> 2.8.2-3mdv2010.0
+ Revision: 451968
- rebuild

* Sun Aug 23 2009 Funda Wang <fwang@mandriva.org> 2.8.2-2mdv2010.0
+ Revision: 419812
- rebuild for new libjpeg v7

  + Florent Monnier <blue_prawn@mandriva.org>
    - corrected a typo

* Mon Aug 03 2009 Frederik Himpe <fhimpe@mandriva.org> 2.8.2-1mdv2010.0
+ Revision: 408550
- update to new version 2.8.2

* Wed Jun 03 2009 Frederik Himpe <fhimpe@mandriva.org> 2.8.1-1mdv2010.0
+ Revision: 382538
- Update to new version 2.8.1

* Tue May 19 2009 Götz Waschk <waschk@mandriva.org> 2.8.0-3mdv2010.0
+ Revision: 377494
- rebuild for new poppler

* Sun Mar 01 2009 Frederik Himpe <fhimpe@mandriva.org> 2.8.0-2mdv2009.1
+ Revision: 346426
- Rename to lower case openscenegraph
- Add libpoppler-glib-devel BuildRequires
- Define CMAKE_BUILD_TYPE=Release, otherwise the library names get a
  d suffix which are not found by other applications linking to OSG

* Sat Feb 28 2009 Frederik Himpe <fhimpe@mandriva.org> 2.8.0-1mdv2009.1
+ Revision: 346183
- Update to new version 2.8.0
- Remove Werror=format-scurity patch: integrated upstream
- used %%{buildroot} macro in SPEC file instead of $RPM_BUILD_ROOT

* Sun Feb 01 2009 Funda Wang <fwang@mandriva.org> 2.6.1-2mdv2009.1
+ Revision: 336057
- add more BRs

* Sat Jan 31 2009 Funda Wang <fwang@mandriva.org> 2.6.1-1mdv2009.1
+ Revision: 335875
- New version 2.6.1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix mesaglu-devel BR
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel
    - import OpenSceneGraph

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

