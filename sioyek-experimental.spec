Name:       sioyek-experimental

%global __brp_check_rpaths %{nil}
%global latest_git_commit 8ee4038fd3ab28d3efaabf896287c44573ddf814
%global shortened_git_commit %(c=%{latest_git_commit}; echo ${c:0:7})

Version:    3.0.0+git%{shortened_git_commit}
Release:    4%?dist
Summary:    PDF viewer with a focus on textbooks and research papers, experimental version
Url:        https://github.com/ahrm/sioyek
Source0:    sioyek-%{latest_git_commit}.tar.gz
License:    GPL-3.0-or-later
Packager:   Donavan Campbell <vncvltvred@proton.me>

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtbase-static
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: qt6-qt3d-devel
BuildRequires: qt6-qtspeech-devel
BuildRequires: qt6-qtsvg-devel
BuildRequires: mesa-libGL-devel
BuildRequires: glfw-devel
BuildRequires: mupdf-devel
BuildRequires: zlib-ng-compat-devel
BuildRequires: sqlite-devel

%description
Sioyek is a PDF viewer with a focus on textbooks and research papers, experimental version

%prep
%autosetup -n sioyek-%{latest_git_commit}

%build
# Allows papirus-icons to replace the icon
sed -i 's/^Icon=.*/Icon=sioyek/' resources/sioyek.desktop

%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/etc/sioyek
mkdir -p %{buildroot}/usr/share/sioyek
mkdir -p %{buildroot}/usr/share/applications
mkdir -p %{buildroot}/usr/share/pixmaps

install -m 755 -p redhat-linux-build/sioyek %{buildroot}%{_bindir}
install -m 644 -p pdf_viewer/prefs.config %{buildroot}%{_sysconfdir}/sioyek
install -m 644 -p pdf_viewer/keys.config %{buildroot}%{_sysconfdir}/sioyek
install -m 644 -p resources/sioyek.desktop %{buildroot}%{_datadir}/applications
install -m 644 -p resources/sioyek-icon-linux.png %{buildroot}%{_datadir}/pixmaps/sioyek.png
install -m 644 -p tutorial.pdf %{buildroot}%{_datadir}/sioyek

cp -r pdf_viewer/shaders %{buildroot}/usr/share/sioyek

%files
%{_bindir}/sioyek
%config(noreplace) %{_sysconfdir}/sioyek/prefs.config
%config(noreplace) %{_sysconfdir}/sioyek/keys.config
%{_datadir}/sioyek/tutorial.pdf
%{_datadir}/sioyek/shaders/*.fragment
%{_datadir}/sioyek/shaders/*.vertex
%{_datadir}/applications/sioyek.desktop
%{_datadir}/pixmaps/sioyek.png

%changelog
* Fri Feb 28 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0-git986af1e-4
- Cleanup build and file section

* Wed Feb 26 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0-git986af1e-3
- Fix icon not being able to be replaced by papirus-icons

* Tue Feb 25 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0-git986af1e-2
- Fix missing icon

* Fri Feb 21 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0-git986af1e-1
- First release and initial testing
