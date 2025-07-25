Summary:	Photo Print - Prints photos in various layouts and with color management
Name:		photoprint
Version:	0.4.1b
Release:	1
License:	GPL
Group:		X11/Applications/Publishing
Source0:	http://www.blackfiveimaging.co.uk/photoprint/%{name}-%{version}.tar.gz
# Source0-md5:	9db16efdccbecbcd0110aa67e21938ee
Patch0:		%{name}-stdio.patch
URL:		http://blackfiveimaging.co.uk/index.php?article=02Software%2F01PhotoPrint
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel
BuildRequires:	lcms-devel
BuildRequires:	libgutenprint-devel
BuildRequires:	libtiff-devel
BuildRequires:	netpbm-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Photo Print is a utility for printing images via Gutenprint (a
rebranding of Gimp-Print for the latest version).

It supports different printing layouts, as one picture per page,
several pictures (scaled to equal size) per page, a poster of one
picture put together of several sheets, or several pictures combined
to one round picture for a CD back.

%prep
%setup -q
%patch -P0 -p1

%build
# Do not do any compiler optimizations, they break the program - MDK note
#CFLAGS='' CXXFLAGS='' ./configure --program-prefix= --prefix=%{_prefix} --exec-prefix=%{_prefix} --bindir=%{_bindir} --sbindir=%{_sbindir} --sysconfdir=%{_sysconfdir} --datadir=%{_datadir} --includedir=%{_includedir} --libdir=%{_libdir} --libexecdir=%{_libdir} --localstatedir=/var/lib --sharedstatedir=%{_prefix}/com --mandir=%{_mandir} --infodir=%{_infodir} --x-includes=%{_prefix}/X11R6/include --x-libraries=%{_prefix}/X11R6/lib
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/photoprint/{borders,ProfilingKit} \
	$RPM_BUILD_ROOT{%{_iconsdir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# install man page
install photoprint.1 $RPM_BUILD_ROOT%{_mandir}/man1

# install menu icon
mv $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/fotoprint.png $RPM_BUILD_ROOT%{_iconsdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README COPYING NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/*.png
%{_desktopdir}/*.desktop
%{_mandir}/man*/*
%{_datadir}/photoprint
