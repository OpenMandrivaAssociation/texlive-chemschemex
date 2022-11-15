Name:		texlive-chemschemex
Version:	46723
Release:	1
Summary:	Typeset and cross-reference chemical schemes based on TikZ code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chemschemex
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemschemex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemschemex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemschemex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a comfortable means of typesetting
chemical schemes, and also offers automatic structure
referencing.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/chemschemex
%{_texmfdistdir}/tex/latex/chemschemex
%doc %{_texmfdistdir}/doc/latex/chemschemex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
