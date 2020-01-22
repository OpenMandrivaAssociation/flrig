Name:		flrig
Version:	1.3.49
Release:	1
Summary:	Transceiver control program for Amateur Radio use
License:	GPLv2+
Group:		Communications/Radio
URL:		http://www.w1hkj.com/flrig-help/
Source0:	http://sourceforge.net/projects/fldigi/files/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	fltk-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xmlrpc)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)

BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(alsa)


%description
Flrig is a transceiver control program designed to be used either stand
alone or as an adjunct to fldigi. The user interface changes to accommodate
the degree of CAT support available for the transceiver in use.
The back end control code for each transceiver is unique to flrig.
No additional libraries or definition files are required.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
