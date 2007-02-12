Summary:	Preety puzzle games for one player
Summary(pl.UTF-8):   Ładne układanki dla jednego gracza
Name:		54321
Version:	1.0.2001.11.16
Release:	4
License:	GPL
Group:		X11/Applications/Games
Source0:	http://nklein.com/products/54321/%{version}/%{name}.tgz
# Source0-md5:	20b2ad52ef45742c1a65911b225b6ddc
Source1:	%{name}.desktop
Patch0:		%{name}-sdl_include_dir_fix.patch
Patch1:		%{name}-linking.patch
Patch2:		%{name}-SDL_main.patch
URL:		http://www.nklein.com/products/54321/
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	SDL_image-devel
Requires:	SDL >= 1.2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
54321 is five games in four-, three-, or two-dimensions for one
player. 54321 takes five classic two-dimensional puzzle games and
extends them into three and four dimensions.

%description -l pl.UTF-8
54321 to pięć gier w czterech, trzech i dwóch wymiarach dla jednego
gracza. Gry bazują na klasycznych schematach układanek; oprawione są w
ładną grafikę.

%prep
%setup -q -n 54321
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} -f GNUmakefile \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	LDFLAGS="%{rpmldflags}" \
	CXXFLAGS="%{rpmcflags} -I/usr/include/SDL -DNDEBUG=1" \
	STRIP="echo"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_bindir},%{_datadir}/54321/bin/Linux,%{_libdir}/54321}

cp -r Release/data $RPM_BUILD_ROOT%{_datadir}/54321
# hack to preserve %{_datadir} arch-independent
install Release/bin/Linux/54321 $RPM_BUILD_ROOT%{_libdir}/54321
cat > $RPM_BUILD_ROOT%{_bindir}/54321 <<EOF
#!/bin/sh
cd /usr/share/54321/bin/Linux && exec %{_libdir}/54321/54321 \$*
EOF

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%dir %{_datadir}/%{name}/bin/Linux
%{_datadir}/%{name}/data
%{_desktopdir}/*.desktop
