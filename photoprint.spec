Summary:	Photo Print - Prints photos in various layouts and with color management
Name:		photoprint
Version:	0.3.8b
Release:	0.2
License:	GPL
Group:		Publishing
Source0:	http://www.blackfiveservices.co.uk/photoprint_resources/%{name}-%{version}.tar.gz
# Source0-md5:	9f8cc6552a799bbeeee42d64b2cb7a1a
URL:		http://www.blackfiveservices.co.uk/photoprint.shtml
BuildRequires:	ImageMagick
BuildRequires:	libgutenprint-devel
BuildRequires:	liblcms-devel
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

%build
# Do not do any compiler optimizations, they break the program.
#CFLAGS='' CXXFLAGS='' ./configure --program-prefix= --prefix=%{_prefix} --exec-prefix=%{_prefix} --bindir=%{_bindir} --sbindir=%{_sbindir} --sysconfdir=%{_sysconfdir} --datadir=%{_datadir} --includedir=%{_includedir} --libdir=%{_libdir} --libexecdir=%{_libdir} --localstatedir=/var/lib --sharedstatedir=%{_prefix}/com --mandir=%{_mandir} --infodir=%{_infodir} --x-includes=%{_prefix}/X11R6/include --x-libraries=%{_prefix}/X11R6/lib
%configure

%{__make}

# Generate menu icons in required format
convert splashscreen/SplashScreen.tif -resize 32x32 photoprint.png

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/photoprint/{borders,ProfilingKit} \
	$RPM_BUILD_ROOT{%{_iconsdir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# install man page
install photoprint.1 $RPM_BUILD_ROOT%{_mandir}/man1/

# install menu icon
install photoprint.png $RPM_BUILD_ROOT%{_iconsdir}

## install menu entry
#install -d $RPM_BUILD_ROOT%_menudir
#cat <<EOF > $RPM_BUILD_ROOT%_menudir/photoprint
#?package(photoprint): needs=X11 \
#section="Multimedia/Graphics" \
#title="Photo Print" \
#longtitle="Prints photos in various layouts and with color management" \
#command="photoprint" \
#icon="photoprint.png"
#EOF

%find_lang %{name} --with-gnome

%clean
rm -fr $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README COPYING NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/%{name}.png
%{_mandir}/man*/*
%{_datadir}/photoprint
