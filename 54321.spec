Summary:	Preety puzzle games for one player.
Summary(pl):	£adne puzzlowate gry dla jednego gracza.
Name:		54321
Version:	1.0.2001.11.16
Release:	0.9
License:	GPL
Group:		X11/Applications/Games
Source0:	http://nklein.com/products/54321/1.0.2001.11.16/54321.tgz
Source1:	%{name}.desktop
Source2:	54321-exec
Patch0:		54321-sdl_include_dir_fix.patch
URL:		http://www.nklein.com/products/54321/
BuildRequires:	SDL-devel
BuildRequires:  SDL_image-devel
Requires:	SDL >= 1.2.4
Requires:       SDL_image
Requires:       libpng
Requires:	zlib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
54321 is five games in four-, three-, or two-dimensions for one player. 
54321 takes five classic two-dimensional puzzle games and extends 
them into three and four dimensions. 

%description -l pl
54321 to piêæ gier w czterech, trzech i dwóch wymiarach dla jednego gracza.
Gry bazuj± na klasycznych puzzlowatych schematach oprawionych w ³adn± grafikê.

%prep
%setup -q -n 54321 
%patch0 -p1

%build
%{__make} -f GNUmakefile CXXFLAGS="%{rpmcflags} -DNDEBUG=1" CC="%{__cc}" CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT $RPM_BUILD_ROOT%{_applnkdir}/Games \
$RPM_BUILD_ROOT{%{_bindir},%{_datadir}/54321/Release}

cp -r Release/* $RPM_BUILD_ROOT%{_datadir}/54321/Release
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT%{_bindir}/54321-exec $RPM_BUILD_ROOT%{_bindir}/54321

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
#gzip -9nf README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc *.gz
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/Release/
%dir %{_datadir}/%{name}/Release/data
%dir %{_datadir}/%{name}/Release/bin
%dir %{_datadir}/%{name}/Release/bin/Linux

%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}/Release/data/*
%attr(755,root,root) %{_datadir}/%{name}/Release/bin/Linux/*
%{_applnkdir}/Games/*
