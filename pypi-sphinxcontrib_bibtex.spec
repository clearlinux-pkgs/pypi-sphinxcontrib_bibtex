#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-sphinxcontrib_bibtex
Version  : 2.6.1
Release  : 40
URL      : https://files.pythonhosted.org/packages/95/57/821fc3506812ffdf636296de321b204aeab8a86655811ef2f841fc81f854/sphinxcontrib-bibtex-2.6.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/95/57/821fc3506812ffdf636296de321b204aeab8a86655811ef2f841fc81f854/sphinxcontrib-bibtex-2.6.1.tar.gz
Summary  : Sphinx extension for BibTeX style citations.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-sphinxcontrib_bibtex-license = %{version}-%{release}
Requires: pypi-sphinxcontrib_bibtex-python = %{version}-%{release}
Requires: pypi-sphinxcontrib_bibtex-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(docutils)
BuildRequires : pypi(pybtex)
BuildRequires : pypi(pybtex_docutils)
BuildRequires : pypi(sphinx)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
sphinxcontrib-bibtex
====================
|ci| |codecov| |version| |license|
Sphinx extension for BibTeX style citations.

%package license
Summary: license components for the pypi-sphinxcontrib_bibtex package.
Group: Default

%description license
license components for the pypi-sphinxcontrib_bibtex package.


%package python
Summary: python components for the pypi-sphinxcontrib_bibtex package.
Group: Default
Requires: pypi-sphinxcontrib_bibtex-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinxcontrib_bibtex package.


%package python3
Summary: python3 components for the pypi-sphinxcontrib_bibtex package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_bibtex)
Requires: pypi(docutils)
Requires: pypi(pybtex)
Requires: pypi(pybtex_docutils)
Requires: pypi(sphinx)

%description python3
python3 components for the pypi-sphinxcontrib_bibtex package.


%prep
%setup -q -n sphinxcontrib-bibtex-2.6.1
cd %{_builddir}/sphinxcontrib-bibtex-2.6.1
pushd ..
cp -a sphinxcontrib-bibtex-2.6.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1693325567
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_bibtex
cp %{_builddir}/sphinxcontrib-bibtex-%{version}/LICENSE.rst %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_bibtex/24b6fd5ce1f2ff1d7f755425a9c98594099d7426 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinxcontrib_bibtex/24b6fd5ce1f2ff1d7f755425a9c98594099d7426

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
