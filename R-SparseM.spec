#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-SparseM
Version  : 1.7
Release  : 24
URL      : http://cran.r-project.org/src/contrib/SparseM_1.7.tar.gz
Source0  : http://cran.r-project.org/src/contrib/SparseM_1.7.tar.gz
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

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library SparseM
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library SparseM


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/SparseM/ChangeLog
/usr/lib64/R/library/SparseM/DESCRIPTION
/usr/lib64/R/library/SparseM/INDEX
/usr/lib64/R/library/SparseM/Meta/Rd.rds
/usr/lib64/R/library/SparseM/Meta/data.rds
/usr/lib64/R/library/SparseM/Meta/demo.rds
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
