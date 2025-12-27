%global module pytest-forked
%define oname pytest_forked

Name:           python-%{module}
Version:        1.6.0
Release:        3
Summary:        run tests in isolated forked subprocesses
Group:          Development/Python
License:        MIT
URL:            https://github.com/pytest-dev/pytest-forked
Source0:        https://files.pythonhosted.org/packages/source/p/pytest-forked/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch:      noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(py)
BuildRequires:  python%{pyver}dist(pytest) >= 3.10
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

%description
pytest-forked: run each test in a forked subprocess .. warning:: this is a
extraction of the xdist --forked module, future maintenance beyond the bare
minimum is not planned until a new maintainer is found. This plugin **does not
work on Windows** because there's no fork support. * --forked: run each test in
a forked subprocess to survive SEGFAULTS or otherwise dying processes.
Installation...


%files
%license LICENSE
%doc README.rst
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
