%global tl_name graph35
%global tl_revision 66772

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.4
Release:	%{tl_revision}.1
Summary:	Draw keys and screen items of several Casio calculators
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/graph35
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graph35.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graph35.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graph35.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package defines commands to draw the Casio Graph 35 / fx-9750GII
calculator (and other models). It can draw the whole calculator, or
parts of it (individual keys, part of the screen, etc.). It was written
to typeset documents instructing students how to use their calculator.

