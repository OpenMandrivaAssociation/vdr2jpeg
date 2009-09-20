
%define name	vdr2jpeg
%define version	0.1.1
%define rel	2

Summary:	Grab JPEG images of VDR recordings
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	LGPL
URL:		http://xxv.berlios.de/content/blogcategory/20/42/
Source:		http://prdownload.berlios.de/xxv/vdr2jpeg-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	ffmpeg-devel >= 0.4.9-0.pre1.20060309

%description
This is a simple c++ program to grab jpeg images from
VDR-Recordings. It's based on vdrsync.pl and ffmain, and was
designed as a little study to enhance xxv.

%prep
%setup -q

%build
export LIBS="%ldflags"
%make CXXFLAGS="%optflags" STRIP=/bin/true

%install
rm -rf %{buildroot}

install -D -m755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc HISTORY LIESMICH README
%{_bindir}/%{name}

