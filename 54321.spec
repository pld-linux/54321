Summary:	Preety puzzle games for one player
Summary(pl):	£adne uk³adanki dla jednego gracza
Name:		54321
Version:	1.0.2001.11.16
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://nklein.com/products/54321/1.0.2001.11.16/%{name}.tgz
# Source0-md5:	20b2ad52ef45742c1a65911b225b6ddc
Source1:	%{name}.desktop
Source2:	%{name}-exec
Patch0:		%{name}-sdl_include_dir_fix.patch
URL:		http://www.nklein.com/products/54321/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
Requires:	SDL >= 1.2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
54321 is five games in four-, three-, or two-dimensions for one
player. 54321 takes five classic two-dimensional puzzle games and
extends them into three and four dimensions.

%description -l pl
54321 to piêæ gier w czterech, trzech i dwóch wymiarach dla jednego
gracza. Gry bazuj± na klasycznych schematach uk³adanek; oprawione s± w
³adn± grafikê.

%prep
%setup -q -n 54321
%patch0 -p1

%build
%{__make} -f GNUmakefile CXXFLAGS="%{rpmcflags} -I /usr/include/SDL -DNDEBUG=1" CC="%{__cc}" CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT $RPM_BUILD_ROOT%{_desktopdir} \
$RPM_BUILD_ROOT{%{_bindir},%{_datadir}/54321}

cp -r Release/* $RPM_BUILD_ROOT%{_datadir}/54321
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT%{_bindir}/54321-exec $RPM_BUILD_ROOT%{_bindir}/54321

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc README
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/data
%dir %{_datadir}/%{name}/bin
%dir %{_datadir}/%{name}/bin/Linux

%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}/data/*
%attr(755,root,root) %{_datadir}/%{name}/bin/Linux/*
%{_desktopdir}/*
