#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gamm4
Version  : 0.2.6
Release  : 45
URL      : https://cran.r-project.org/src/contrib/gamm4_0.2-6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gamm4_0.2-6.tar.gz
Summary  : Generalized Additive Mixed Models using 'mgcv' and 'lme4'
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-lme4
BuildRequires : R-lme4
BuildRequires : buildreq-R

%description
function gamm() from 'mgcv', using 'lme4' for estimation.

%prep
%setup -q -c -n gamm4
cd %{_builddir}/gamm4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641023388

%install
export SOURCE_DATE_EPOCH=1641023388
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gamm4
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gamm4
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gamm4
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc gamm4 || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gamm4/DESCRIPTION
/usr/lib64/R/library/gamm4/INDEX
/usr/lib64/R/library/gamm4/Meta/Rd.rds
/usr/lib64/R/library/gamm4/Meta/features.rds
/usr/lib64/R/library/gamm4/Meta/hsearch.rds
/usr/lib64/R/library/gamm4/Meta/links.rds
/usr/lib64/R/library/gamm4/Meta/nsInfo.rds
/usr/lib64/R/library/gamm4/Meta/package.rds
/usr/lib64/R/library/gamm4/NAMESPACE
/usr/lib64/R/library/gamm4/R/gamm4
/usr/lib64/R/library/gamm4/R/gamm4.rdb
/usr/lib64/R/library/gamm4/R/gamm4.rdx
/usr/lib64/R/library/gamm4/help/AnIndex
/usr/lib64/R/library/gamm4/help/aliases.rds
/usr/lib64/R/library/gamm4/help/gamm4.rdb
/usr/lib64/R/library/gamm4/help/gamm4.rdx
/usr/lib64/R/library/gamm4/help/paths.rds
/usr/lib64/R/library/gamm4/html/00Index.html
/usr/lib64/R/library/gamm4/html/R.css
