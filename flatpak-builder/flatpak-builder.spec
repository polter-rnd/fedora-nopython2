%global glib2_version 2.44
%global ostree_version 2017.14
%global flatpak_version 0.10.2

Name:           flatpak-builder
Version:        0.10.10
Release:        2.nopy2%{?dist}
Summary:        Tool to build flatpaks from source

License:        LGPLv2+
URL:            http://flatpak.org/
Source0:        https://github.com/flatpak/flatpak-builder/releases/download/%{version}/%{name}-%{version}.tar.xz

# Patch to remove bzr dependency
Patch0:		%{name}-%{version}-nopy2.patch

BuildRequires:  gettext
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  flatpak >= %{flatpak_version}
BuildRequires:  libcap-devel
BuildRequires:  libdwarf-devel
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(ostree-1) >= %{ostree_version}
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  /usr/bin/xmlto
BuildRequires:  /usr/bin/xsltproc

Requires:       flatpak%{?_isa} >= %{flatpak_version}
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       ostree-libs%{?_isa} >= %{ostree_version}
Requires:       /usr/bin/bzip2
Requires:       /usr/bin/eu-strip
Requires:       /usr/bin/git
Requires:       /usr/bin/patch
Requires:       /usr/bin/rofiles-fuse
Requires:       /usr/bin/strip
Requires:       /usr/bin/svn
Requires:       /usr/bin/tar
Requires:       /usr/bin/unzip

%description
Flatpak-builder is a tool for building flatpaks from sources.

See http://flatpak.org/ for more information.


%prep
%autosetup -p1


%build
%configure \
    --enable-docbook-docs \
    --with-dwarf-header=%{_includedir}/libdwarf

%make_build V=1


%install
%make_install


%files
%license COPYING
%doc %{_pkgdocdir}
%{_bindir}/flatpak-builder
%{_mandir}/man1/flatpak-builder.1*
%{_mandir}/man5/flatpak-manifest.5*


%changelog
* Tue May 29 2018 Pavel Artsishevsky <polter.rnd@gmail.com> - 0.10.10-2.nopy2
- Removed bzr source to get rid from python2 dependency

* Fri Apr 27 2018 David King <amigadave@amigadave.com> - 0.10.10-2
- Add some extra dependencies

* Thu Apr 26 2018 Kalev Lember <klember@redhat.com> - 0.10.10-1
- Update to 0.10.10

* Mon Feb 19 2018 David King <amigadave@amigadave.com> - 0.10.9-1
- Update to 0.10.9

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 15 2017 Kalev Lember <klember@redhat.com> - 0.10.6-1
- Update to 0.10.6

* Tue Nov 28 2017 David King <amigadave@amigadave.com> - 0.10.5-1
- Update to 0.10.5

* Mon Nov 06 2017 Kalev Lember <klember@redhat.com> - 0.10.4-1
- Update to 0.10.4

* Tue Oct 31 2017 David King <amigadave@amigadave.com> - 0.10.3-1
- Update to 0.10.3

* Mon Oct 30 2017 David King <amigadave@amigadave.com> - 0.10.2-1
- Update to 0.10.2

* Fri Oct 27 2017 Kalev Lember <klember@redhat.com> - 0.10.1-1
- Update to 0.10.1

* Thu Oct 26 2017 Kalev Lember <klember@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Mon Oct 09 2017 Kalev Lember <klember@redhat.com> - 0.9.99-1
- Update to 0.9.99

* Mon Sep 25 2017 Kalev Lember <klember@redhat.com> - 0.9.98-1
- Update to 0.9.98

* Wed Sep 13 2017 Kalev Lember <klember@redhat.com> - 0.9.11-1
- Update to 0.9.11

* Mon Sep 04 2017 Kalev Lember <klember@redhat.com> - 0.9.9-1
- Initial flatpak-builder package
