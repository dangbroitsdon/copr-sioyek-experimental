%global         latest_git_commit 62a0b8482fd19bf59ed7e8a55899ddb8bd512809
%global         shortened_git_commit %(c=%{latest_git_commit}; echo ${c:0:7})
%global         date %(date +%Y%m%d)
%global         hour %(date +%H)
%global         base_pkg_name sioyek

%define _disable_source_fetch 0

Name:           %{base_pkg_name}-experimental
Version:        3.0.0+%{date}.%{hour}.%{shortened_git_commit}
Release:        1%{?dist}
Summary:        PDF viewer with a focus on textbooks and research papers.
Url:            https://github.com/ahrm/%{base_pkg_name}
Source:         https://github.com/ahrm/%{base_pkg_name}/archive/%{latest_git_commit}/%{base_pkg_name}-%{latest_git_commit}.tar.gz
License:        GPL-3.0-or-later

BuildRequires: qt6-qtdeclarative-devel mupdf-devel qt6-qtbase-private-devel qt6-qtbase-static pkgconfig(Qt6Core) pkgconfig(Qt6Network) pkgconfig(Qt6OpenGL) pkgconfig(Qt63DCore) pkgconfig(Qt6Qml) pkgconfig(Qt6QuickControls2) pkgconfig(Qt6QuickWidgets) pkgconfig(Qt6Svg) pkgconfig(Qt6TextToSpeech) pkgconfig(Qt6Widgets) pkgconfig(Qt6OpenGLWidgets) pkgconfig(zlib) pkgconfig(sqlite3) pkgconfig(harfbuzz) pkgconfig(glfw3) pkgconfig(dri) gcc-c++ desktop-file-utils 

%description
Sioyek is a PDF viewer with a focus on textbooks and research papers.

%prep
%autosetup -n %{base_pkg_name}-%{latest_git_commit}

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_SKIP_RPATH=1
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
* Sun Jul 27 2025 Donavan Campbell <vncvltvred@proton.me> - 3.0.0+20250727.13.8d173d9-2
- build against mupdf 1.26 and minor change

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
