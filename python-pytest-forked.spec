%global pypi_name pytest-forked

Name:           python-%{pypi_name}
Version:        1.6.0
Release:        1
Summary:        run tests in isolated forked subprocesses
Group:          Development/Python
License:        MIT
URL:            https://github.com/pytest-dev/pytest-forked
Source0:        https://files.pythonhosted.org/packages/source/p/pytest-forked/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(py)
BuildRequires:  python3dist(pytest) >= 3.10
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)

%description
pytest-forked: run each test in a forked subprocess .. warning:: this is a
extraction of the xdist --forked module, future maintenance beyond the bare
minimum is not planned until a new maintainer is found. This plugin **does not
work on Windows** because there's no fork support. * --forked: run each test in
a forked subprocess to survive SEGFAULTS or otherwise dying processes.
Installation...

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pytest_forked
%{python3_sitelib}/pytest_forked-%{version}.dist-info
