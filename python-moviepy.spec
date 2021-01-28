%global pypi_name moviepy

Name:           python-%{pypi_name}
Version:        1.0.3
Release:        %mkrel 1
Group:          Development/Python
Summary:        Video editing with Python
License:        MIT
URL:            https://zulko.github.io/moviepy/
Source0:        https://pypi.io/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
MoviePy is a Python library for video editing: cutting, concatenations,
title insertions, video compositing (a.k.a. non-linear editing), video
processing, and creation of custom effects. See the gallery for some
examples of use at https://zulko.github.io/moviepy/gallery.html.

%package -n python3-%{pypi_name}
Summary:        Video editing with Python 3
Group:          Development/Python
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
MoviePy is a Python3 library for video editing: cutting, concatenations,
title insertions, video compositing (a.k.a. non-linear editing), video
processing, and creation of custom effects. See the gallery for some
examples of use at https://zulko.github.io/moviepy/gallery.html.
This is the Python 3 build of %{pypi_name}.

%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst docs
%license LICENCE.txt
%{python3_sitelib}/%{pypi_name}*
