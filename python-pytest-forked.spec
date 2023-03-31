# Created by pyp2rpm-3.3.5
%global pypi_name pytest-forked

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        2
Summary:        run tests in isolated forked subprocesses
Group:          Development/Python
License:        MIT
URL:            https://github.com/pytest-dev/pytest-forked
Source0:        %{pypi_name}-%{version}.tar.gz
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
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pytest_forked
%{python3_sitelib}/pytest_forked-%{version}-py%{python3_version}.egg-info
