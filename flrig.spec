Name:		flrig
URL:		http://www.w1hjk.com
License:	GPL
Group:		Communications
Version:	1.3.08
Release:	1
Summary:	Transceiver control program for Amateur Radio use
Source0:	http://www.w1hkj.com/downloads/flrig/%{name}-%{version}.tar.gz
BuildRequires:	gcc-c++ gcc make libx11-devel fltk-devel libxmlrpc-c-devel libpng-devel libjpeg-devel

%description
Flrig is a transceiver control program designed to be used either stand
alone or as an adjunct to fldigi. The user interface changes to accommodate
the degree of CAT support available for the transceiver in use.
The back end control code for each transceiver is unique to flrig.
No additional libraries or definition files are required.

Authors:
--------
W1HKJ    -   w1hkj@w1hkj.com

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/flrig.desktop
%{_datadir}/pixmaps/flrig.xpm
