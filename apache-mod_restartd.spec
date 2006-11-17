%define		apxs		/usr/sbin/apxs
Summary:	mod_restartd - run certain CGIs as root
Summary(pl):	mod_restartd - uruchamianie pewnych CGI z uprawnieniami roota
Name:		mod_restartd
Version:	1.0.3
Release:	0.1
License:	Apache 2.0
Group:		Networking/Daemons
Source0:	http://directory.fedora.redhat.com/sources/mod_restartd-%{version}.tar.gz
# Source0-md5:	6336780a292dbd41d2cc66212f3be7fa
URL:		http://directory.fedora.redhat.com/wiki/Mod_restartd
BuildRequires:	%{apxs}
BuildRequires:	apache-devel >= 2.2
BuildRequires:	apr-devel >= 1:1.0
BuildRequires:	apr-util-devel >= 1:1.0
Requires:	apache(modules-api) = %apache_modules_api
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)
%define		_sysconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)

%description
An Apache 2 module for doing suid CGIs. The Admin Server provides CGIs
to stop, start, and restart the servers, which may run on port 389,
which means they must be started by root. However, Apache does not
like to run as root for security reasons. This module allows CGIs to
be run as root by copying the the mod_cgid and fixing it so that only
certain CGIs may be run as root.

%description -l pl
Modu³ Apache'a 2 do wykonywania suidowych CGI. Admin Server udostêpnia
CGI do zatrzymywania, uruchamiania i restartowania serwerów
dzia³aj±cych na porcie 389, co oznacza, ¿e musz± byæ uruchamiane jako
root. Jednak Apache nie lubi dzia³aæ jako root ze wzglêdów
bezpieczeñstwa. Ten modu³ pozwala na wykonywanie CGI jako root poprzez
skopiowanie mod_cgid i poprawienie tak, by pozwala³ na wykonywanie
jako root tylko okre¶lonych CGI.

%prep
%setup -q -n mod_restartd-%{version}

%build
# apr-util is missing in configure check
CPPFLAGS="`apu-1-config --includes`"
%configure \
	--with-apxs=%{apxs} \
	--with-apr-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pkglibdir}

install .libs/libmodrestartd.so $RPM_BUILD_ROOT%{_pkglibdir}

# TODO: XX_mod_restartd.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_pkglibdir}/libmodrestartd.so
