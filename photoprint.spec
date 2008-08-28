Summary:	Photo Print - Prints photos in various layouts and with color management
Name:		photoprint
Version:	0.3.1
%define		bordersversion 0.0.1
Release:	1mdk
License:	GPL
Group:		Publishing
Source:		http://www.blackfiveservices.co.uk/PhotoPrint/Downloads/%{name}-%{version}.tar.bz2
Source1:	http://www.blackfiveservices.co.uk/PhotoPrint/Downloads/photoprint-borders-%{bordersversion}.tar.bz2
Source2:	http://www.blackfiveservices.co.uk/PhotoPrint/Downloads/ProfilingKit.tar.bz2
Url:		http://www.blackfiveservices.co.uk/PhotoPrint/About.shtml
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	liblcms-devel, libtiff-devel, libjpeg-devel, libnetpbm-devel
BuildRequires:	libcups-devel, libgutenprint-devel, libgtk+2.0-devel
BuildRequires:	ImageMagick

%description

Photo Print is a utility for printing images via Gutenprint (a
rebranding of Gimp-Print for the latest version).

It supports different printing layouts, as one picture per page,
several pictures (scaled to equal size) per page, a poster of one
picture put together of several sheets, or several pictures combined
to one round picture for a CD back.

Image frames (Templates in /usr/share/photoprint/borders/) and color
management (Profiling instructions in
/usr/share/photoprint/ProfilingKit/ProfilingKit.html) are also
supported.

Photo Print can be used as GUI tool and also as command line tool in
batch mode.

Works nicely as an image editor in GQ-View.

%prep

%setup -q
%setup -q -T -D -a 1 -n %{name}-%{version}
%setup -q -T -D -a 2 -n %{name}-%{version}

%build

# Do not do any compiler optimizations, they break the program.
#CFLAGS='' CXXFLAGS='' ./configure --program-prefix= --prefix=%{_prefix} --exec-prefix=%{_prefix} --bindir=%{_bindir} --sbindir=%{_sbindir} --sysconfdir=%{_sysconfdir} --datadir=%{_datadir} --includedir=%{_includedir} --libdir=%{_libdir} --libexecdir=%{_libdir} --localstatedir=/var/lib --sharedstatedir=%{_prefix}/com --mandir=%{_mandir} --infodir=%{_infodir} --x-includes=%{_prefix}/X11R6/include --x-libraries=%{_prefix}/X11R6/lib

%configure

%make

# Generate menu icons in required format
convert splashscreen/SplashScreen.tif -resize 32x32 photoprint.png
convert splashscreen/SplashScreen.tif -resize 16x16 photoprint_mini.png
convert splashscreen/SplashScreen.tif -resize 48x48 photoprint_large.png

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# install borders
install -d %buildroot%{_datadir}/photoprint/borders
cp -a photoprint-borders*/. %buildroot%{_datadir}/photoprint/borders
install -d %buildroot%{_datadir}/photoprint/ProfilingKit
cp -a ProfilingKit*/. %buildroot%{_datadir}/photoprint/ProfilingKit

%find_lang %{name} --with-gnome

# install man page

install -d %buildroot%{_mandir}/man1/
install -m 644 photoprint.1 %buildroot%{_mandir}/man1/

# install menu icon
install -d %buildroot%{_datadir}/icons
install -m 644 photoprint.png %buildroot%{_datadir}/icons/
install -d %buildroot%{_datadir}/icons/mini
install -m 644 photoprint_mini.png %buildroot%{_datadir}/icons/mini/photoprint.png
install -d %buildroot%{_datadir}/icons/large
install -m 644 photoprint_large.png %buildroot%{_datadir}/icons/large/photoprint.png

# install menu entry
install -d %buildroot/%_menudir
cat <<EOF > %buildroot/%_menudir/photoprint
?package(photoprint): needs=X11 \
section="Multimedia/Graphics" \
title="Photo Print" \
longtitle="Prints photos in various layouts and with color management" \
command="photoprint" \
icon="photoprint.png"
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -fr %buildroot

%files -f %{name}.lang
%defattr(-,root,root)
%doc README COPYING NEWS TODO
%_bindir/*
%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png
%_menudir/%name
%_mandir/man*/*
%_datadir/photoprint

%changelog
* Tue Feb 21 2006 Till Kamppeter <till@mandriva.com> 0.3.1-1mdk
- Updated to version 0.3.1 (Dedicated profile selector, path editor widget,
  image selector, new "Paths" dialog for selecting profile and border paths,
  batch mode fixed, various bug fixes).

* Tue Nov  1 2005 Till Kamppeter <till@mandriva.com> 0.3.0-1mdk
- Updated to version 0.3.0 (Color management improvements, bug fixes).

* Sat Aug 27 2005 Till Kamppeter <till@mandriva.com> 0.2.9-2mdk
- Improved package description.

* Sat Aug 27 2005 Till Kamppeter <till@mandriva.com> 0.2.9-1mdk
- Updated to version 0.2.8 (Changing of of modes for many/all photos,
  canceling of transfer between layouts possible).
- Added photoprint borders and profiling kit.

* Sat Aug 13 2005 Till Kamppeter <till@mandriva.com> 0.2.8-2mdk
- Rebuilt for new Gutenprint.

* Sat Aug 13 2005 Till Kamppeter <till@mandriva.com> 0.2.8-1mdk
- Updated to version 0.2.8 (Some bug fixes, optimized compilation works 
  now.).
- Activated optimized compilation again.
- New home page and download URLs.

* Tue Jul 25 2005 Till Kamppeter <till@mandriva.com> 0.2.7-1mdk
- Updated to version 0.2.7 (Many bug fixes and improvements).
- Do not do any compiler optimizations, they break the program.

* Sun Jul 17 2005 Till Kamppeter <till@mandriva.com> 0.2.6-1mdk
- initial release.
