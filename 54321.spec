Summary:	- Preety 3D puzzles for one player.
Summary(pl):	- £adne trójwymiarowe puzzle dla jednego gracza.
Name:		- 54321
Version:	-
Release:	-
License:	- (enter GPL/LGPL/BSD/BSD-like/other license name here)
Group:		-
Icon:		-
Source0:	%{name}-%{version}.tar.gz
URL:		- http://www.nklein.com/products/54321/
BuildRequires:	- SDL-devel
BuildRequires:  - SDL_image-devel
Requires:	- SDL >= 1.2.4
Requires:       - SDL_image
Requires:       - libpng
Requires:	- zlib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

%files subpackage
%defattr(644,root,root,755)
%doc extras/*.gz
%{_datadir}/%{name}-ext
