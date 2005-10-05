%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Template
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_Flexy

Summary:	%{_pearname} - a flexible caching template engine based on SimpleTemplate
Summary(pl):	%{_pearname} - elastyczny buforuj±cy silnik szablonów oparty na SimpleTemplate
Name:		php-pear-%{_pearname}
Version:	1.2.2
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1d7d1ae0bc831fbb2f9a622d7aadac49
Patch0:		%{name}-case_fix.patch
Patch1:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/HTML_Template_Flexy/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
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

%description -l pl
HTML_Template_Flexy pocz±tkowo by³ uproszczeniem HTML_Template_Xipe,
jednak od wersji 0.2 sta³ siê jednym z pierwszych silników szablonów
u¿ywaj±cych prawdziwego analizatora leksykalnego zamiast wyra¿eñ
regularnych, co umo¿liwia robienie rzeczy w stylu ASP.net czy
znaczników Cold Fusion. Jednak nadal ma bardzo prosty zbiór
zastosowañ. Cechy silnika:
- bardzo proste API - ³atwe do nauczenia, zapobiega umieszczaniu zbyt
  du¿ej ilo¶ci logiki w szablonach
- ³atwe pisanie dokumentowalnego kodu - poprzez u¿ycie zmiennych
  obiektowych dla szablonu zamiast przypisywania mo¿na u¿ywaæ
  komentarzy phpDoc do wypisywania u¿ywanych zmiennych
- edytowalny w edytorach WYSIWYG - mo¿na tworzyæ w pe³ni funkcjonalne
  szablony, które nie psuj± siê po ka¿dym u¿yciu Dreamweavera(tm) czy
  edytora Mozilli; przy dodawaniu pêtli i warunków u¿ywane s± atrybuty
  z przestrzeniami nazw
- ekstremalnie szybki - kod uruchomieniowy jest przynajmniej 4 razy
  mniejszy ni¿ wiêkszo¶æ innych silników szablonów (np. Smarty); u¿ywa
  skompilowanych szablonów, dziêki czemu jest wiele razy szybszy na
  blokach i pêtlach ni¿ szablony oparte na wyra¿eniach regularnych
  (np. IT/phplib)
- bezpieczniejszy (pod k±tem ataków cross-site scripting) - wszystkie
  zmienne domy¶lnie s± wypisywane z u¿yciem sekwencji kontrolnych HTML
  (mo¿na to zmieniæ modyfikatorem :h)
- wspiera wielojêzyczno¶æ - przetwarza ³añcuchy z szablonu, co pozwala
  na zbudowanie narzêdzi do t³umaczenia; kompiluje specyficzne dla
  jêzyka szablony, dziêki czemu t³umaczenie jest robione tylko raz, a
  nie przy ka¿dym ¿±daniu
- w pe³ni obs³uguje dynamiczne elementy (jak ASP.NET), dziêki czemu
  mo¿na pobieraæ elementy do zast±pienia w czasie dzia³ania.

D³ugoterminowym planem rozwoju Flexy jest zintegrowanie jako backend
dla Future Template Package (dostêpny bêdzie wrapper BC, jako ¿e autor
te¿ musi tego u¿ywaæ).

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
install -d docs/%{_pearname}
mv ./%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/example.ini docs/%{_pearname}
cd ./%{php_pear_dir}/%{_class}/%{_subclass}
%patch0 -p1
%patch1 -p1

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
