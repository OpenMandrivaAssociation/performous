Name:			performous
Release:		%mkrel 3
Version:		0.5.1
Group:			Games/Other
Summary:		Performous - A cross-platform clone of the Playstation 2 game Singstar
License:		GPL
Url:			http://performous.org/index.html
Source:			%{name}-%{version}-Source.tar.bz2
Source1:		Jamelia-Demo.tar.bz2
BuildRoot:		%{_tmppath}/%{name}-%{version}-build
BuildRequires:	libgl-devel
BuildRequires:	libglew-devel
BuildRequires:	libglu-devel
BuildRequires:	imagemagick-devel
BuildRequires:	SDL-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	boost-devel
BuildRequires:	gtk+2-devel
BuildRequires:	jpeg-devel
BuildRequires:	png-devel
BuildRequires:	librsvg-devel
BuildRequires:	glibmm2.4-devel
BuildRequires:	portaudio-devel
BuildRequires:	portmidi-devel
BuildRequires:	libxml++-devel
BuildRequires:	cmake
BuildRequires:	imagemagick
BuildRequires:	help2man

%description
Performous - new Sing Screen using themed lyrics.

Performous is a free cross-platform clone of the Playstation 2
game Singstar.

While Performous might be classified as a karaoke program, it is
actually much more than that. Instead of just displaying the lyrics,
notes are also displayed and the performance is scored based on how
well you actually hit the notes. Unlike in many other games in this
genre, you will also see the pitch that you are singing, so that you
can see what you are doing wrong and easily (well, everything is
relative) correct your pitch.

Most of the songs available also contain the original vocals and actual
karaoke versions are rare.

Features
* Should work on almost any platform
* Very accurate singing pitch detection
* OpenGL-based graphics rendering
* Music videos as backgrounds
* Free software, licensed under GNU GPL version 2 or later

Note:
start it firsttime with performous --help to get the options!

%prep
%setup -q -n %{name} -a1
rm -f CMakeCache.txt

%build
export CXXFLAGS="%optflags -DBOOST_FILESYSTEM_VERSION=2"
%cmake
%make

%install
rm -fr %buildroot
%makeinstall_std -C build

# demo song
%__install -dm 755 "%{buildroot}%{_datadir}/games/ultrastar/songs/Jamelia Superstar"
cd $RPM_BUILD_DIR/%{name}/
%__install -m 644 "Jamelia Superstar"/* \
	"%{buildroot}%{_datadir}/games/ultrastar/songs/Jamelia Superstar"


# icon
%__install -dm 755 %{buildroot}%{_datadir}/pixmaps
convert %{buildroot}%{_datadir}/pixmaps/performous.xpm -resize 48x48! \
	%{buildroot}%{_datadir}/pixmaps/performous.png

# menu-entry
%__install -dm 755 %{buildroot}%{_datadir}/applications
%__rm %{buildroot}%{_datadir}/applications/performous.desktop
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Performous
Comment=A karaoke game
Comment[de]=Ein Karaoke Spiel
Comment[ro]=Un joc de tip karaoke
Comment[fr]=Un jeu de Karaoke
Comment[fi]=Karaokepeli
Comment[es]=Un juego de karaoke
Exec=performous
Icon=performous
Terminal=false
Type=Application
Categories=Game;Simulation;
EOF

%find_lang Performous

%clean
rm -rf $RPM_BUILD_ROOT

%files -f Performous.lang
%defattr(-,root,root)
%doc docs/*
%{_bindir}/ss*
%{_bindir}/gh*
%{_bindir}/itg_pck
%{_bindir}/performous
%{_datadir}/games/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop
%{_mandir}/man6/performous.6*
