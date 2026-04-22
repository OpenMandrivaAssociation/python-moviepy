%global pypi_name moviepy

Name:           python-%{pypi_name}
Version:        2.2.1
Release:        1
Group:          Development/Python
Summary:        Video editing with Python
License:        MIT
URL:            https://zulko.github.io/moviepy/
Source0:        https://pypi.io/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(imageio-ffmpeg)
BuildRequires:  python3dist(proglog)
BuildRequires:  python3dist(pip)

Requires: python3dist(imageio-ffmpeg)
Requires: python3dist(proglog)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description
MoviePy is a Python library for video editing: cutting, concatenations,
title insertions, video compositing (a.k.a. non-linear editing), video
processing, and creation of custom effects. See the gallery for some
examples of use at https://zulko.github.io/moviepy/gallery.html.


%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files
%doc README* docs
%license LICENCE.txt
%{python_sitelib}/moviepy-%{version}.dist-info
%{python_sitelib}/moviepy/*
