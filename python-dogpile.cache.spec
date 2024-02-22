# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-dogpile.cache
Epoch: 100
Version: 1.3.4
Release: 1%{?dist}
BuildArch: noarch
Summary: A caching front-end based on the Dogpile lock
License: MIT
URL: https://github.com/sqlalchemy/dogpile.cache/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
dogpile.cache is a Python caching API which provides a generic interface
to caching backends of any variety.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-dogpile.cache
Summary: A caching front-end based on the Dogpile lock
Requires: python3
Requires: python3-decorator >= 4.0.0
Requires: python3-stevedore >= 3.0.0
Requires: python3-typing-extensions >= 4.0.1
Provides: python3-dogpile.cache = %{epoch}:%{version}-%{release}
Provides: python3dist(dogpile.cache) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-dogpile.cache = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(dogpile.cache) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-dogpile.cache = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(dogpile.cache) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-dogpile.cache
dogpile.cache is a Python caching API which provides a generic interface
to caching backends of any variety.

%files -n python%{python3_version_nodots}-dogpile.cache
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-dogpile.cache
Summary: A caching front-end based on the Dogpile lock
Requires: python3
Requires: python3-decorator >= 4.0.0
Requires: python3-stevedore >= 3.0.0
Requires: python3-typing-extensions >= 4.0.1
Provides: python3-dogpile.cache = %{epoch}:%{version}-%{release}
Provides: python3dist(dogpile.cache) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-dogpile.cache = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(dogpile.cache) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-dogpile.cache = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(dogpile.cache) = %{epoch}:%{version}-%{release}

%description -n python3-dogpile.cache
dogpile.cache is a Python caching API which provides a generic interface
to caching backends of any variety.

%files -n python3-dogpile.cache
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-dogpile.cache
Summary: A caching front-end based on the Dogpile lock
Requires: python3
Requires: python3-decorator >= 4.0.0
Requires: python3-stevedore >= 3.0.0
Requires: python3-typing-extensions >= 4.0.1
Provides: python3-dogpile.cache = %{epoch}:%{version}-%{release}
Provides: python3dist(dogpile.cache) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-dogpile.cache = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(dogpile.cache) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-dogpile.cache = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(dogpile.cache) = %{epoch}:%{version}-%{release}

%description -n python3-dogpile.cache
dogpile.cache is a Python caching API which provides a generic interface
to caching backends of any variety.

%files -n python3-dogpile.cache
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
