#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-SparseM
Version  : 1.77
Release  : 46
URL      : https://cran.r-project.org/src/contrib/SparseM_1.77.tar.gz
Source0  : https://cran.r-project.org/src/contrib/SparseM_1.77.tar.gz
Summary  : Sparse Linear Algebra
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-SparseM-lib
BuildRequires : clr-R-helpers

%description
Versions of SparseM prior to 0.95 included a LICENSE file that described
some uncertainties over the licensing status of the fortran
code in src/cholesky.f.  As of 9 March 2012, original authors of cholesky.f,
Esmond Ng and Barry Peyton,  have now, very kindly,  given permission to
use cholesky.f under an open source license.  They have requested that
their code be credited via the following two publications:

%package lib
Summary: lib components for the R-SparseM package.
Group: Libraries

%description lib
lib components for the R-SparseM package.


%prep
%setup -q -c -n SparseM

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1514061198

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1514061198
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SparseM
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SparseM
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SparseM
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library SparseM|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/SparseM/ChangeLog
/usr/lib64/R/library/SparseM/DESCRIPTION
/usr/lib64/R/library/SparseM/INDEX
/usr/lib64/R/library/SparseM/Meta/Rd.rds
/usr/lib64/R/library/SparseM/Meta/data.rds
/usr/lib64/R/library/SparseM/Meta/demo.rds
/usr/lib64/R/library/SparseM/Meta/features.rds
/usr/lib64/R/library/SparseM/Meta/hsearch.rds
/usr/lib64/R/library/SparseM/Meta/links.rds
/usr/lib64/R/library/SparseM/Meta/nsInfo.rds
/usr/lib64/R/library/SparseM/Meta/package.rds
/usr/lib64/R/library/SparseM/Meta/vignette.rds
/usr/lib64/R/library/SparseM/NAMESPACE
/usr/lib64/R/library/SparseM/R/SparseM
/usr/lib64/R/library/SparseM/R/SparseM.rdb
/usr/lib64/R/library/SparseM/R/SparseM.rdx
/usr/lib64/R/library/SparseM/TODO
/usr/lib64/R/library/SparseM/data/lsq.rda
/usr/lib64/R/library/SparseM/data/triogramX.rda
/usr/lib64/R/library/SparseM/demo/Binding.R
/usr/lib64/R/library/SparseM/demo/Coercion.R
/usr/lib64/R/library/SparseM/demo/LeastSquares.R
/usr/lib64/R/library/SparseM/demo/LinearAlgebra.R
/usr/lib64/R/library/SparseM/demo/Solve.R
/usr/lib64/R/library/SparseM/demo/Visualization.R
/usr/lib64/R/library/SparseM/doc/SparseM.R
/usr/lib64/R/library/SparseM/doc/SparseM.Rnw
/usr/lib64/R/library/SparseM/doc/SparseM.pdf
/usr/lib64/R/library/SparseM/doc/index.html
/usr/lib64/R/library/SparseM/extdata/lsq.out
/usr/lib64/R/library/SparseM/extdata/lsq.rra
/usr/lib64/R/library/SparseM/extdata/rua_32_ax.rua
/usr/lib64/R/library/SparseM/help/AnIndex
/usr/lib64/R/library/SparseM/help/SparseM.rdb
/usr/lib64/R/library/SparseM/help/SparseM.rdx
/usr/lib64/R/library/SparseM/help/aliases.rds
/usr/lib64/R/library/SparseM/help/paths.rds
/usr/lib64/R/library/SparseM/html/00Index.html
/usr/lib64/R/library/SparseM/html/R.css
/usr/lib64/R/library/SparseM/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/SparseM/libs/SparseM.so
/usr/lib64/R/library/SparseM/libs/SparseM.so.avx2
/usr/lib64/R/library/SparseM/libs/SparseM.so.avx512
