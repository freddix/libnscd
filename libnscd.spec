Summary:	Interface to communicate with the nscd daemon
Name:		libnscd
Version:	2.0.2
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://ftp.suse.com/pub/people/kukuk/libnscd/%{name}-%{version}.tar.bz2
# Source0-md5:	a6f37e961de4f09c06df43070a47c615
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides an easy interface for normal programs to
communicate with the nscd daemon from the GNU C Library.

%package devel
Summary:	Header files for libnscd library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libnscd library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libnscd.so.1
%attr(755,root,root) %{_libdir}/libnscd.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnscd.so
%{_libdir}/libnscd.la
%{_includedir}/libnscd.h
%{_mandir}/man3/nscd_flush_cache.3*

