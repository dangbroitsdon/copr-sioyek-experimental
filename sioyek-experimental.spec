%define         latest_git_commit 38f066df3e0b964cb944023317f074611dc1d219
%define         shortened_git_commit %(c=%{latest_git_commit}; echo ${c:0:7})
%define         date %(date +%Y%m%d)
%define         hour %(date +%H)
%define         base_pkg_name sioyek

Name:           %{base_pkg_name}-experimental
Version:        3.0.0+%{date}.%{hour}.%{shortened_git_commit}
Release:        1%{?dist}
Summary:        PDF viewer with a focus on textbooks and research papers.
Url:            https://github.com/ahrm/%{base_pkg_name}
Source0:        https://github.com/ahrm/%{base_pkg_name}/archive/%{latest_git_commit}/%{base_pkg_name}-%{latest_git_commit}.tar.gz
Patch1:         https://github.com/dangbroitsdon/copr-%{base_pkg_name}-experimental/cmake.patch
License:        GPL-3.0-or-later

BuildRequires:  qt6-qtbase-devel qt6-qtbase-static qt6-qtdeclarative-devel qt6-qt3d-devel qt6-qtspeech-devel qt6-qtsvg-devel mesa-libGL-devel glfw-devel mupdf-devel zlib-ng-compat-devel sqlite-devel gcc desktop-file-utils

%description
Sioyek is a PDF viewer with a focus on textbooks and research papers.

%prep
%autosetup -p1 -n %{base_pkg_name}-%{latest_git_commit}

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
install -Dm 755 -p redhat-linux-build/%{base_pkg_name} -t %{buildroot}%{_bindir}
install -Dm 644 -p pdf_viewer/prefs.config pdf_viewer/keys.config -t %{buildroot}%{_sysconfdir}/%{base_pkg_name}
install -Dm 644 -p resources/%{base_pkg_name}.desktop -t %{buildroot}%{_datadir}/applications
install -Dm 644 -p resources/%{base_pkg_name}-icon-linux.png %{buildroot}%{_datadir}/pixmaps/%{base_pkg_name}.png
install -Dm 644 -p tutorial.pdf -t %{buildroot}%{_datadir}/%{base_pkg_name}
install -Dm 644 -p resources/%{base_pkg_name}.1 -t %{buildroot}%{_mandir}/man1

desktop-file-install --delete-original --set-icon=%{base_pkg_name} --dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{base_pkg_name}.desktop

cp -r pdf_viewer/shaders %{buildroot}%{_datadir}/%{base_pkg_name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{base_pkg_name}
%{_datadir}/applications/%{base_pkg_name}.desktop
%{_datadir}/pixmaps/%{base_pkg_name}.png
%{_mandir}/man1/%{base_pkg_name}.1.gz
%dir %{_sysconfdir}/%{base_pkg_name}
%config(noreplace) %{_sysconfdir}/%{base_pkg_name}/*
%dir %{_datadir}/%{base_pkg_name}
%{_datadir}/%{base_pkg_name}/tutorial.pdf
%{_datadir}/%{base_pkg_name}/shaders/*

%changelog
* Sat Apr 05 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0+20250405.18.957f1dd-1
- update versioning

* Fri Apr 04 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0+git3172c42-1
- simple changes in line with fedora packaging guidelines

* Mon Mar 31 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0+git4ee8831-1
- misc changes

* Wed Mar 12 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0+gitb3575d9-1
- Further cleanup

* Fri Feb 28 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0+git986af1e-4
- Cleanup build and file section

* Wed Feb 26 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0+git986af1e-3
- Fix icon not being able to be replaced by papirus-icons

* Tue Feb 25 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0+git986af1e-2
- Fix missing icon

* Fri Feb 21 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0+git986af1e-1
- First release and initial testing
