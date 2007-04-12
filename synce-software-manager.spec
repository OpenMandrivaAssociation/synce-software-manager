%define name	synce-software-manager
%define version	0.9.0
%define release	1mdk

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

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%name): needs="x11" \
section="More Applications/Communications" \
title="Synce-software-manager" longtitle="Software manager for WinCE devices" command="%{name}" icon="communications_section.png"
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
%{_menudir}/%name

%Changelog
* Mon Jan 13 2004 Austin Acton <austin@mandrake.org> 0.9.0-1mdk
- adapt spec from Nicolas Lécureuil <neoclust@zarb.org>
- add menu entry

