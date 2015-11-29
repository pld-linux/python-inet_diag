#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (enable when useful - now scripts use python2 shebang)

Summary:	Ethernet settings Python 2 bindings
Summary(pl.UTF-8):	Wiązania Pythona 2 do ustawień sieci Ethernet
Name:		python-inet_diag
Version:	0.1
Release:	2
License:	GPL v2
Group:		Libraries/Python
Source0:	https://www.kernel.org/pub/software/libs/python/python-inet_diag/%{name}-%{version}.tar.xz
# Source0-md5:	622310fe9ab0e52e0eda586227383992
URL:		https://rt.wiki.kernel.org/index.php/Tuna
BuildRequires:	python-devel >= 2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
%endif
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 bindings for the inet_diag kernel interface, that allows
querying AF_INET socket state.

%description -l pl.UTF-8
Wiązania Pythona 2 do interfejsu jądra inet_diag, pozwalającego na
odpytywanie stanu gniazd AF_INET.

%package -n python3-inet_diag
Summary:	Ethernet settings Python 3 bindings
Summary(pl.UTF-8):	Wiązania Pythona 3 do ustawień sieci Ethernet
Group:		Libraries/Python

%description -n python3-inet_diag
Python 3 bindings for the inet_diag kernel interface, that allows
querying AF_INET socket state.

%description -n python3-inet_diag -l pl.UTF-8
Wiązania Pythona 3 do interfejsu jądra inet_diag, pozwalającego na
odpytywanie stanu gniazd AF_INET.

%prep
%setup -q

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%if %{with python2}
%py_install
%endif

%if %{with python3}
%py3_install
%endif

cp -p psk.py $RPM_BUILD_ROOT%{_sbindir}/psk
cp -p pss.py $RPM_BUILD_ROOT%{_sbindir}/pss

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/psk
%attr(755,root,root) %{_sbindir}/pss
%attr(755,root,root) %{py_sitedir}/inet_diag.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/inet_diag-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-inet_diag
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/inet_diag.cpython-*.so
%{py3_sitedir}/inet_diag-%{version}-py*.egg-info
%endif
