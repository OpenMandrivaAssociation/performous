Name:			performous
Release:		%mkrel 01
Version:		0.5.1
Group:			Games/Other
Summary:		Performous - A cross-platform clone of the Playstation 2 game Singstar
License:		GPL
Url:			http://performous.org/index.html
Source:			%{name}-%{version}-Source.tar.bz2
Source1:		Jamelia-Demo.tar.bz2
BuildRoot:		%{_tmppath}/%{name}-%{version}-build

BuildRequires:	liboil-devel jpeg-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	libglib2.0-devel
BuildRequires:	glibmm2.4-devel
BuildRequires:	libgstreamer-devel
BuildRequires:	libgstreamer-plugins-base-devel gamin-devel
BuildRequires:	libffmpeg-devel
BuildRequires:	libjack-devel jack
BuildRequires:	libmagick-devel 
BuildRequires:	libpulseaudio-devel 
BuildRequires:	librsvg2-devel 
BuildRequires:	libsamplerate-devel
BuildRequires:	libsigc++2.0-devel 
BuildRequires:	libxml2-devel
BuildRequires:  libxml++2.6-devel
BuildRequires:	libSDL-devel
BuildRequires:	libglew-devel
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	cairo-devel >= 1.2
BuildRequires:	gcc-c++
BuildRequires:	help2man
BuildRequires:	pkgconfig
BuildRequires:	portaudio-devel
BuildRequires:	sndfile-devel
BuildRequires:	imagemagick

%define debug_packages	%{nil}


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



%build
rm -rf CMakeCache.txt
%__install -dm 755 build
 pushd build
	cmake .. \
		-DCMAKE_BUILD_TYPE="RELEASE" \
		-DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT%{_usr} \
		
%make
%install
pushd build
%make install prefix=$RPM_BUILD_ROOT/usr

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
Encoding=UTF-8
Name=Performous
Comment=A karaoke game
Comment[de]=Ein Karaoke Spiel
Comment[ro]=Un joc de tip karaoke
Comment[fr]=Un jeu de Karaoke
Comment[fi]=Karaokepeli
Comment[es]=Un juego de karaoke
Exec=performous
Icon=performous.png
Terminal=false
Type=Application
Categories=Application;Game;Simulation;
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs/*
%{_bindir}/ss*
%{_bindir}/gh*
%{_bindir}/itg_pck
%{_bindir}/performous
%dir %{_datadir}/games/performous
%{_datadir}/games/performous/*
%dir %{_datadir}/games/ultrastar
%{_datadir}/games/ultrastar/*
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/*.xpm
%{_datadir}/applications/*.desktop
%{_datadir}/man/man6/performous.6.lzma
%{_datadir}/locale/*

%changelog

