# git snapshot
%global snapshot 1
%if 0%{?snapshot}
	%global commit		fb4c839d34fb1354be1f9d96abf021aeff6395b5
	%global commitdate	20180416
	%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%endif

Summary:	A lightweight utility to display and launch system utilies
Name:		lx-control-center
Version:	0.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://lxde.sourceforge.net/
#Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
Source0:	https://github.com/lxde/%{name}/archive/%{?snapshot:%{commit}}%{!?snapshot:%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz
Patch0:		lx-control-center-switch_lxde_to_gtk3.patch
BuildRequires:	desktop-file-utils
BuildRequires:	python%{pyver}dist(pygobject)
BuildRequires:	python%{pyver}dist(python-distutils-extra)
BuildRequires:	python%{pyver}dist(setuptools)

Requires:	python%{pyver}dist(pygobject)

Buildarch:  noarch

%description
Lightweight utility to display and launch system utilies, like configuration
programs.

%files
%{_bindir}/%{name}
%{python3_sitelib}/LXControlCenter
%{python3_sitelib}/lx_control_center-*.*-info/
#{_datadir}/applications/*.desktop
%{_mandir}/man1/%{name}.1.*

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}

%build
%py_build
%py_build build_i18n
#py_build build_help
#py_build build_icons

%install
%py_install

# manual
install -dm 0755 %{buildroot}%{_mandir}/man1/
install -pm 0644 data/man/%{name}.1 %{buildroot}%{_mandir}/man1/

# .desktop
#install -dm 0755 %{buildroot}%{_mandir}/man1/
#install -pm 0644 data/man/%{name}.1 %{buildroot}%{_mandir}/man1/
#desktop-file-install \
#	--delete-original \
#	--remove-key=NotShowIn \
#	--add-only-show-in=LXDE \
#	--set-icon=preferences-desktop-keyboard \
#	--dir %{buildroot}%{_datadir}/applications \
#	./data/%{name}.desktop.in

