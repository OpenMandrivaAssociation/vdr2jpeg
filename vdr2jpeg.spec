
%define name	vdr2jpeg
%define version	0.1.0
%define rel	1

Summary:	Grab JPEG images of VDR recordings
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	LGPL
URL:		http://xxv.berlios.de/content/blogcategory/20/42/
Source:		http://prdownload.berlios.de/xxv/vdr2jpeg-%{version}.tgz
Patch0:		vdr2jpeg-0.1.0-gcc4.3.patch
Patch1:		vdr2jpeg-0.1.0-ffmpeg-new-header-location.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	ffmpeg-devel >= 0.4.9-0.pre1.20060309

%description
This is a simple c++ program to grab jpeg images from
VDR-Recordings. It's based on vdrsync.pl and ffmain, and was
designed as a little study to enhance xxv.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%make CXXFLAGS="%optflags -Wl,--as-needed -Wl,--no-undefined"

%install
rm -rf %{buildroot}

install -D -m755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc HISTORY LIESMICH README
%{_bindir}/%{name}

