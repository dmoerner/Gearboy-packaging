Name:		Gearboy
Version:	2.3.1	
Release:	1%{?dist}
Summary:	Game Boy and Game Boy Color emulator

# Gearboy is licensed under GPLv3+. Code in src/audio is licensed
# under LGPLv2+ or MIT. Since these are GPLv3+ compatible licenses,
# the whole project is licensed under GPLv3+.
License:	GPLv3+
URL:		https://github.com/drhelius/Gearboy

# Upstream git tags are the only instance where "Gearboy" is stylized
# without initial capitalization.
Source0:	https://github.com/drhelius/Gearboy/archive/gearboy-%{version}/Gearboy-%{version}.tar.gz
Patch0:		Gearboy-use-system-miniz.patch

BuildRequires:	gcc-c++
BuildRequires:	qt5-devel
BuildRequires:	freeglut-devel
BuildRequires:	SDL2-devel
BuildRequires:	glew-devel
BuildRequires:	miniz-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib

%description
Gearboy is a Nintendo Game Boy and Game Boy Color emulator written in
C++. The emulator prioritizes readable, simple source code and high
compatibility across a variety of platforms and architectures. Gearboy
features highly accurate CPU emulation, instruction timing, and memory
timing. It also includes memory bank controllers, accurate LCD
controller emulation, mix frames, sound emulation, and compressed ROM
support.


%prep
%autosetup -p1 -n Gearboy-gearboy-%{version}


%build
%qmake_qt5 platforms/linux/Gearboy/Gearboy.pro -o platforms/linux/Gearboy/Makefile
%make_build -C platforms/linux/Gearboy


%install
mkdir -p %{buildroot}/%{_bindir}
install -p platforms/linux/Gearboy/Gearboy %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man6
cp -p platforms/linux/Gearboy/Gearboy.6 %{buildroot}/%{_mandir}/man6
mkdir -p %{buildroot}/%{_datadir}/appdata
cp -p platforms/linux/Gearboy/Gearboy.appdata.xml %{buildroot}/%{_datadir}/appdata
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications platforms/linux/Gearboy/Gearboy.desktop


%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%files
%{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/appdata/*
%{_datadir}/applications/*
%license LICENSE
%doc README.md


%changelog
* Sat Jan 14 2017 Daniel Moerner <dmoerner@gmail.com> - 2.3.1-1
- New upstream release. Includes several merged fixes aimed at
  packaging for Fedora.

* Thu Jan 12 2017 Daniel Moerner <dmoerner@gmail.com> - 2.3-1
- Initial packaging.

