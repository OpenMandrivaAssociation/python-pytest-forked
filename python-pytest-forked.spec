%global module pytest-forked
%define oname pytest_forked

Name:           python-%{module}
Version:        1.7.5
Release:        1
Summary:        run tests in isolated forked subprocesses
Group:          Development/Python
License:        MIT
URL:            https://github.com/pytest-dev/pytest-forked
Source0:        https://files.pythonhosted.org/packages/source/p/pytest-forked/%{oname}-%{version}.tar.gz
BuildSystem:	python
BuildArch:      noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(py)
BuildRequires:  python%{pyver}dist(pytest) >= 7
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"

%description
Run each test in a forked subprocess so a crash does not kill the
rest of the suite. This is the former pytest-xdist --forked plugin.
It does not work on Windows.


%files
%license LICENSE
%doc README.rst
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
