%define         latest_git_commit 3172c42a565381b72fffb390e444f65ff988aa61
%define         shortened_git_commit %(c=%{latest_git_commit}; echo ${c:0:7})

Name:           sioyek-experimental
Version:        3.0.0+git%{shortened_git_commit}
Release:        1%?dist
Summary:        PDF viewer with a focus on textbooks and research papers, experimental version
Url:            https://github.com/ahrm/sioyek
Source0:        https://github.com/ahrm/sioyek/archive/%{latest_git_commit}/sioyek-%{latest_git_commit}.tar.gz
Patch1:         https://github.com/dangbroitsdon/sioyek-experimental-ci/cmake.patch
License:        GPL-3.0-or-later

BuildRequires:  qt6-qtbase-devel qt6-qtbase-static qt6-qtdeclarative-devel qt6-qt3d-devel qt6-qtspeech-devel qt6-qtsvg-devel mesa-libGL-devel glfw-devel mupdf-devel zlib-ng-compat-devel sqlite-devel

%description
PDF viewer with a focus on textbooks and research papers.

%prep
%autosetup -p1 -n sioyek-%{latest_git_commit}

%build
# Allows papirus-icons to replace the icon
sed -i 's/^Icon=.*/Icon=sioyek/' resources/sioyek.desktop

%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
install -Dm 755 -p redhat-linux-build/sioyek -t %{buildroot}%{_bindir}
install -Dm 644 -p pdf_viewer/prefs.config pdf_viewer/keys.config -t %{buildroot}%{_sysconfdir}/sioyek
install -Dm 644 -p resources/sioyek.desktop -t %{buildroot}%{_datadir}/applications
install -Dm 644 -p resources/sioyek-icon-linux.png %{buildroot}%{_datadir}/pixmaps/sioyek.png
install -Dm 644 -p tutorial.pdf -t %{buildroot}%{_datadir}/sioyek
install -Dm 644 -p resources/sioyek.1 -t %{buildroot}%{_mandir}/man1

cp -r pdf_viewer/shaders %{buildroot}%{_datadir}/sioyek

%files
%license LICENSE
%doc README.md
%{_bindir}/sioyek
%{_datadir}/applications/sioyek.desktop
%{_datadir}/pixmaps/sioyek.png
%{_mandir}/man1/sioyek.1.gz
%dir %{_sysconfdir}/sioyek
%config(noreplace) %{_sysconfdir}/sioyek/*
%dir %{_datadir}/sioyek
%{_datadir}/sioyek/tutorial.pdf
%{_datadir}/sioyek/shaders/*

%changelog
* Fri Apr 04 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0-git3172c42-1
- simple changes in line with fedora packaging guidelines

* Mon Mar 31 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0-git4ee8831-1
- misc changes

* Wed Mar 12 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0-gitb3575d9-1
- Further cleanup

* Fri Feb 28 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0-git986af1e-4
- Cleanup build and file section

* Wed Feb 26 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0-git986af1e-3
- Fix icon not being able to be replaced by papirus-icons

* Tue Feb 25 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0-git986af1e-2
- Fix missing icon

* Fri Feb 21 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0-git986af1e-1
- First release and initial testing
