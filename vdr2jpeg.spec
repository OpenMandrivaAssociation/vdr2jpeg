
%define name	vdr2jpeg
%define version	0.0.11
%define rel	1

Summary:	Grab JPEG images of VDR recordings
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	LGPL
URL:		http://www.deltab.de/vdr/vdr2jpeg.html
Source:		http://www.deltab.de/vdr/%name-%version.tgz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	ffmpeg-devel >= 0.4.9-0.pre1.20060309

%description
This is a simple c++ program to grab jpeg images from
VDR-Recordings. It's based on vdrsync.pl and ffmain, and was
designed as a little study to enhance xxv.

%prep
%setup -q

%build
%make CXXFLAGS="%optflags"

%install
rm -rf %{buildroot}

install -D -m755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc HISTORY LIESMICH README
%{_bindir}/%{name}


