#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-pdm_pep517
Version  : 1.1.3
Release  : 19
URL      : https://files.pythonhosted.org/packages/d6/d7/bee6e16a0a5e93f38f2f8224183ea6c36cfde1ee93cf5e941f1d6cdb20cf/pdm-pep517-1.1.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/d6/d7/bee6e16a0a5e93f38f2f8224183ea6c36cfde1ee93cf5e941f1d6cdb20cf/pdm-pep517-1.1.3.tar.gz
Summary  : A PEP 517 backend for PDM that supports PEP 621 metadata
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause CC-BY-4.0 ISC MIT
Requires: pypi-pdm_pep517-license = %{version}-%{release}
Requires: pypi-pdm_pep517-python = %{version}-%{release}
Requires: pypi-pdm_pep517-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# PDM-PEP517
**This project has been renamed and re-published as [pdm-backend](https://pypi.org/project/pdm-backend)**

%package license
Summary: license components for the pypi-pdm_pep517 package.
Group: Default

%description license
license components for the pypi-pdm_pep517 package.


%package python
Summary: python components for the pypi-pdm_pep517 package.
Group: Default
Requires: pypi-pdm_pep517-python3 = %{version}-%{release}

%description python
python components for the pypi-pdm_pep517 package.


%package python3
Summary: python3 components for the pypi-pdm_pep517 package.
Group: Default
Requires: python3-core
Provides: pypi(pdm_pep517)

%description python3
python3 components for the pypi-pdm_pep517 package.


%prep
%setup -q -n pdm-pep517-1.1.3
cd %{_builddir}/pdm-pep517-1.1.3
pushd ..
cp -a pdm-pep517-1.1.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679586087
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pdm_pep517
cp %{_builddir}/pdm-pep517-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pdm_pep517/f15bd5033216f10c392e98887c39374601c898ac || :
cp %{_builddir}/pdm-pep517-%{version}/pdm/pep517/_vendor/boolean.py.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pdm_pep517/b2e6af1d5adfcb019f28053da0e78010b34a8fda || :
cp %{_builddir}/pdm-pep517-%{version}/pdm/pep517/_vendor/cerberus/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pdm_pep517/1887ddf1ee05ccdccdade2ccab4757f2dd1cbb74 || :
cp %{_builddir}/pdm-pep517-%{version}/pdm/pep517/_vendor/license_expression/apache-2.0.LICENSE %{buildroot}/usr/share/package-licenses/pypi-pdm_pep517/2048933452c7fda41ba194b27031d931dd6ddadf || :
cp %{_builddir}/pdm-pep517-%{version}/pdm/pep517/_vendor/license_expression/cc-by-4.0.LICENSE %{buildroot}/usr/share/package-licenses/pypi-pdm_pep517/6e55f0780239c6f263c1ab27a55205efb0204d6d || :
cp %{_builddir}/pdm-pep517-%{version}/pdm/pep517/_vendor/license_expression/data/cc-by-4.0.LICENSE %{buildroot}/usr/share/package-licenses/pypi-pdm_pep517/6e55f0780239c6f263c1ab27a55205efb0204d6d || :
cp %{_builddir}/pdm-pep517-%{version}/pdm/pep517/_vendor/packaging/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/pypi-pdm_pep517/598f87f072f66e2269dd6919292b2934dbb20492 || :
cp %{_builddir}/pdm-pep517-%{version}/pdm/pep517/_vendor/packaging/LICENSE.BSD %{buildroot}/usr/share/package-licenses/pypi-pdm_pep517/fdc0e4eabc45522b079deff7d03d70528d775dc0 || :
cp %{_builddir}/pdm-pep517-%{version}/pdm/pep517/_vendor/tomli/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pdm_pep517/9da6ca26337a886fb3e8d30efd4aeda623dc9ade || :
cp %{_builddir}/pdm-pep517-%{version}/pdm/pep517/_vendor/tomli_w/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pdm_pep517/9da6ca26337a886fb3e8d30efd4aeda623dc9ade || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pdm_pep517/1887ddf1ee05ccdccdade2ccab4757f2dd1cbb74
/usr/share/package-licenses/pypi-pdm_pep517/2048933452c7fda41ba194b27031d931dd6ddadf
/usr/share/package-licenses/pypi-pdm_pep517/598f87f072f66e2269dd6919292b2934dbb20492
/usr/share/package-licenses/pypi-pdm_pep517/6e55f0780239c6f263c1ab27a55205efb0204d6d
/usr/share/package-licenses/pypi-pdm_pep517/9da6ca26337a886fb3e8d30efd4aeda623dc9ade
/usr/share/package-licenses/pypi-pdm_pep517/b2e6af1d5adfcb019f28053da0e78010b34a8fda
/usr/share/package-licenses/pypi-pdm_pep517/f15bd5033216f10c392e98887c39374601c898ac
/usr/share/package-licenses/pypi-pdm_pep517/fdc0e4eabc45522b079deff7d03d70528d775dc0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
