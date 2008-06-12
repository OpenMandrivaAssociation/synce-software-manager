%define name	synce-software-manager
%define version	0.9.0
%define release	%mkrel 3

Summary: 	SynCE: Software manager for GNOME 2
Name: 		%{name}
Version: 	0.9.0
Release: 	%{release}
License: 	MIT LGPL
Group: 		Communications
Source: 	%{name}-%{version}.tar.bz2
URL: 		http://synce.sourceforge.net/
Buildroot: 	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: 	libsynce-devel >= 0.9.0
BuildRequires:	gtk2-devel libgnomeui2-devel libglade2.0-devel
BuildRequires:	librapi-devel

%description
Graphical tool for installing and removing software on a Windows CE device.

%prep
%setup -q

%build
%configure2_5x --disable-static --with-librapi2-include=%{_includedir} \
--with-librapi2-lib=%{_libdir}
%make

%install
rm -fr %buildroot
%makeinstall
%find_lang %name

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
cat > $RPM_BUILD_ROOT/%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
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

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc COPYING ChangeLog
%{_bindir}/*
%{_datadir}/synce/synce_software_manager.glade
%{_datadir}/applications/mandriva-%{name}.desktop
