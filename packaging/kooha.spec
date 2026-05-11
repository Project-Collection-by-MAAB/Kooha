Name:           kooha
Version:        2.3.1
Release:        1%{?dist}
Summary:        Elegantly record your screen

License:        GPL-3.0-or-later
URL:            https://github.com/SeaDve/Kooha
Source0:        kooha-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  meson >= 0.59
BuildRequires:  ninja-build
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(glib-2.0) >= 2.80
BuildRequires:  pkgconfig(gio-2.0) >= 2.80
BuildRequires:  pkgconfig(gtk4) >= 4.15.3
BuildRequires:  pkgconfig(libadwaita-1) >= 1.9
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.24
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.24
BuildRequires:  libxkbcommon-devel
BuildRequires:  wayland-devel

Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-bad-free

%description
Kooha is a simple screen recorder with a minimalist interface.
You can just click the record button without having to configure
a bunch of settings.

Features:
- Record microphone, desktop audio, or both at the same time
- Support for WebM, MP4, GIF, and Matroska formats
- Select a monitor or a portion of the screen to record
- Configurable saving location, pointer visibility, frame rate, and delay
- Pause and resume recording

%prep
%autosetup
# Configure cargo to use the vendored sources
mkdir -p .cargo
cat > .cargo/config.toml << 'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%meson
%meson_build

%install
%meson_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.seadve.Kooha.desktop

%files
%license COPYING
%doc README.md
%{_bindir}/kooha
%{_datadir}/applications/io.github.seadve.Kooha.desktop
%{_datadir}/glib-2.0/schemas/io.github.seadve.Kooha.gschema.xml
%{_datadir}/metainfo/io.github.seadve.Kooha.metainfo.xml
%{_datadir}/dbus-1/services/io.github.seadve.Kooha.service
%{_datadir}/icons/hicolor/*/apps/io.github.seadve.Kooha*
%{_datadir}/kooha/

%changelog
* Mon May 11 2026 Dave Patrick Caberto <davecruz48@gmail.com> - 2.3.1-1
- Initial RPM release
