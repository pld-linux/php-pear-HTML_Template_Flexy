%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Template
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_Flexy

Summary:	%{_pearname} - a flexible caching template engine based on SimpleTemplate
Summary(pl.UTF-8):   %{_pearname} - elastyczny buforujący silnik szablonów oparty na SimpleTemplate
Name:		php-pear-%{_pearname}
Version:	1.2.5
Release:	1
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	12ee960a189cd0de2f7af3d9a4eb6af4
Patch0:		%{name}-case_fix.patch
Patch1:		%{name}-path_fix.patch
Patch2:		%{name}-no_gtk.patch
URL:		http://pear.php.net/package/HTML_Template_Flexy/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.3
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(HTML/Javascript.*)' 'pear(File/Gettext.*)' 'pear(Translation2.*)'

%description
HTML_Template_Flexy started its life as a simplification of
HTML_Template_Xipe, however in version 0.2, it became one of the first
template engine to use a real Lexer, rather than regexes, making it
possible to do things like ASP.net or Cold Fusion tags. However, it
still has a very simple set of goals.
- Very Simple API,
	- easy to learn...
	- prevents to much logic going in templates
- Easy to write documentable code
	- By using object vars for a template rather than 'assign',
	  you can use PHPDoc comments to list what variable you use.
- Editable in WYSIWYG editors
	- you can create full featured templates, that don't get
	  broken every time you edit with Dreamweaver(tm) or Mozilla
	  editor
	- Uses namespaced attributes to add looping/conditionals
- Extremely Fast
	- runtime is at least 4 time smaller than most other template
	  engines (eg. Smarty)
	- uses compiled templates, as a result it is many times faster
	  on blocks and loops than than Regex templates (eg.
	  IT/phplib)
- Safer (for cross-site scripting attacks)
	- All variables default to be output as HTML escaped
	  (overridden with the :h modifier)
- Multilanguage support
	- Parses strings out of template, so you can build translation
	  tools
	- Compiles language specific templates (so translation is only
	  done once, not on every request)
- Full dynamic element support (like ASP.NET), so you can pick
	  elements to replace at runtime

The long term plan for Flexy is to be integrated as a backend for the
Future Template Package (A BC wrapper will be made available - as the
author needs to use it too).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
HTML_Template_Flexy początkowo był uproszczeniem HTML_Template_Xipe,
jednak od wersji 0.2 stał się jednym z pierwszych silników szablonów
używających prawdziwego analizatora leksykalnego zamiast wyrażeń
regularnych, co umożliwia robienie rzeczy w stylu ASP.net czy
znaczników Cold Fusion. Jednak nadal ma bardzo prosty zbiór
zastosowań. Cechy silnika:
- bardzo proste API - łatwe do nauczenia, zapobiega umieszczaniu zbyt
  dużej ilości logiki w szablonach
- łatwe pisanie dokumentowalnego kodu - poprzez użycie zmiennych
  obiektowych dla szablonu zamiast przypisywania można używać
  komentarzy phpDoc do wypisywania używanych zmiennych
- edytowalny w edytorach WYSIWYG - można tworzyć w pełni funkcjonalne
  szablony, które nie psują się po każdym użyciu Dreamweavera(tm) czy
  edytora Mozilli; przy dodawaniu pętli i warunków używane są atrybuty
  z przestrzeniami nazw
- ekstremalnie szybki - kod uruchomieniowy jest przynajmniej 4 razy
  mniejszy niż większość innych silników szablonów (np. Smarty); używa
  skompilowanych szablonów, dzięki czemu jest wiele razy szybszy na
  blokach i pętlach niż szablony oparte na wyrażeniach regularnych
  (np. IT/phplib)
- bezpieczniejszy (pod kątem ataków cross-site scripting) - wszystkie
  zmienne domyślnie są wypisywane z użyciem sekwencji kontrolnych HTML
  (można to zmienić modyfikatorem :h)
- wspiera wielojęzyczność - przetwarza łańcuchy z szablonu, co pozwala
  na zbudowanie narzędzi do tłumaczenia; kompiluje specyficzne dla
  języka szablony, dzięki czemu tłumaczenie jest robione tylko raz, a
  nie przy każdym żądaniu
- w pełni obsługuje dynamiczne elementy (jak ASP.NET), dzięki czemu
  można pobierać elementy do zastąpienia w czasie działania.

Długoterminowym planem rozwoju Flexy jest zintegrowanie jako backend
dla Future Template Package (dostępny będzie wrapper BC, jako że autor
też musi tego używać).

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):   Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
install -d docs/%{_pearname}
mv ./%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/example.ini docs/%{_pearname}
cd ./%{php_pear_dir}/%{_class}/%{_subclass}
%patch0 -p1
%patch1 -p1
%patch2 -p6

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/example.ini
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}/Flexy
%{php_pear_dir}/%{_class}/%{_subclass}/Flexy.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
