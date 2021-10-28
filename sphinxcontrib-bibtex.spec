#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sphinxcontrib-bibtex
Version  : 1.0.0
Release  : 21
URL      : https://files.pythonhosted.org/packages/96/10/ba1498a1c2d7a47a4ce904198989fdbceb0b00057d2e5ff666149e7beb67/sphinxcontrib-bibtex-1.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/96/10/ba1498a1c2d7a47a4ce904198989fdbceb0b00057d2e5ff666149e7beb67/sphinxcontrib-bibtex-1.0.0.tar.gz
Summary  : A Sphinx extension for BibTeX style citations.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-bibtex-license = %{version}-%{release}
Requires: sphinxcontrib-bibtex-python = %{version}-%{release}
Requires: sphinxcontrib-bibtex-python3 = %{version}-%{release}
Requires: Sphinx
Requires: oset
Requires: pybtex
Requires: pybtex-docutils
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : oset
BuildRequires : pybtex
BuildRequires : pybtex-docutils

%description
citations to be inserted into documentation generated by

%package license
Summary: license components for the sphinxcontrib-bibtex package.
Group: Default

%description license
license components for the sphinxcontrib-bibtex package.


%package python
Summary: python components for the sphinxcontrib-bibtex package.
Group: Default
Requires: sphinxcontrib-bibtex-python3 = %{version}-%{release}

%description python
python components for the sphinxcontrib-bibtex package.


%package python3
Summary: python3 components for the sphinxcontrib-bibtex package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_bibtex)
Requires: pypi(oset)
Requires: pypi(pybtex)
Requires: pypi(pybtex_docutils)
Requires: pypi(sphinx)

%description python3
python3 components for the sphinxcontrib-bibtex package.


%prep
%setup -q -n sphinxcontrib-bibtex-1.0.0
cd %{_builddir}/sphinxcontrib-bibtex-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583697089
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib-bibtex
cp %{_builddir}/sphinxcontrib-bibtex-1.0.0/LICENSE.rst %{buildroot}/usr/share/package-licenses/sphinxcontrib-bibtex/929c3fab89a2fb8fb835371fc46b299f07388f79
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib-bibtex/929c3fab89a2fb8fb835371fc46b299f07388f79

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
