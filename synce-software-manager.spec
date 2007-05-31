%define name	synce-software-manager
%define version	0.9.0
%define release	%mkrel 2

Summary: 	SynCE: Software manager for GNOME 2
Name: 		%{name}
Version: 	0.9.0
Release: 	%{release}
License: 	MIT LGPL
Group: 		Communications
Source: 	%{name}-%{version}.tar.bz2
URL: 		http://synce.sourceforge.net/
Buildroot: 	%{_tmppath}/%{name}-%{version}-%{release}-root

Requires: 	synce >= 0.9.0
BuildRequires: 	synce-devel >= 0.9.0
BuildRequires:	gtk2-devel libgnomeui2-devel

%description
Graphical tool for installing and removing software on a Windows CE device.

%prep
%setup -q

%build
%configure2_5x --with-libsynce=$RPM_BUILD_ROOT%{_prefix} --with-librapi2=$RPM_BUILD_ROOT%{_prefix}
%make

%install
rm -fr %buildroot
%makeinstall
%find_lang %name

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
cat > $RPM_BUILD_ROOT/%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Synce-software-manager
Comment=Software manager for WinCE devices
Exec=%_bindir/%{name}
Icon=communications_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Office-Communications-Phone;Network;Telephony;
EOF
%clean
rm -fr %buildroot

%post
%update_menus

%postun
%clean_menus

%files -f %name.lang
%defattr(-,root,root)
%doc COPYING ChangeLog
%{_bindir}/*
%{_datadir}/synce/synce_software_manager.glade
%{_datadir}/applications/mandriva-%{name}.desktop
