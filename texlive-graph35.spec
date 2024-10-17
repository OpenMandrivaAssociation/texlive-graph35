Name:		texlive-graph35
Version:	66772
Release:	1
Summary:	Draw keys and screen items of several Casio calculators
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/graph35
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graph35.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graph35.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graph35.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package defines commands to draw the Casio Graph 35 /
fx-9750GII calculator (and other models). It can draw the whole
calculator, or parts of it (individual keys, part of the
screen, etc.). It was written to typeset documents instructing
stundents how to use their calculator.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/graph35
%{_texmfdistdir}/tex/latex/graph35
%doc %{_texmfdistdir}/doc/latex/graph35

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
