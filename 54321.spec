Summary:	- Preety 3D games for one player.
Summary(pl):	- £adne trójwymiarowe gry dla jednego gracza.
Name:		- 54321
Version:	- 1.0.2001.11.16
Release:	- 0.1
License:	- GPL
Group:		- X11/Applications/Games
Source0:	http://nklein.com/products/54321/1.0.2001.11.16/54321.tgz
Source1:	%{name}.desktop
Patch0:		54321-sdl_include_dir_fix.patch
URL:		- http://www.nklein.com/products/54321/
BuildRequires:	- SDL-devel
BuildRequires:  - SDL_image-devel
Requires:	- SDL >= 1.2.4
Requires:       - SDL_image
Requires:       - libpng
Requires:	- zlib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
54321 is five games in four-, three-, or two-dimensions for one player. 
54321 takes five classic two-dimensional puzzle games and extends 
them into three and four dimensions. 
For more information, see the help within the game.

%description -l pl

%prep
%setup -q 
%patch0 -p1

%build
%{__make} -f GNUmakefile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT $RPM_BUILD_ROOT{%{_applnkdir}/Games \
$RPM_BUILD_ROOT{%{_bindir},%{_datadir}/54321/Release}

cp -r Release/* $RPM_BUILD_ROOT%{_datadir}/54321/Release
ln -sf Release/bin/Linux/54321 $RPM_BUILD_ROOT%{_bindir}/54321

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
#gzip -9nf README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
