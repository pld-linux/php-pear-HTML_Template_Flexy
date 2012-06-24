%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Template
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_Flexy

Summary:	%{_pearname} - a flexible caching template engine based on SimpleTemplate
Summary(pl):	%{_pearname} - elastyczny buforuj�cy silnik szablon�w oparty na SimpleTemplate
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	592cae803cbd743b4bb98404a48b6952
Patch0:		%{name}-case_fix.patch
Patch1:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/HTML_Template_Flexy/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
HTML_Template_Flexy pocz�tkowo by� uproszczeniem HTML_Template_Xipe,
jednak od wersji 0.2 sta� si� jednym z pierwszych silnik�w szablon�w
u�ywaj�cych prawdziwego analizatora leksykalnego zamiast wyra�e�
regularnych, co umo�liwia robienie rzeczy w stylu ASP.net czy
znacznik�w Cold Fusion. Jednak nadal ma bardzo prosty zbi�r
zastosowa�. Cechy silnika:
- bardzo proste API - �atwe do nauczenia, zapobiega umieszczaniu zbyt
  du�ej ilo�ci logiki w szablonach
- �atwe pisanie dokumentowalnego kodu - poprzez u�ycie zmiennych
  obiektowych dla szablonu zamiast przypisywania mo�na u�ywa�
  komentarzy phpDoc do wypisywania u�ywanych zmiennych
- edytowalny w edytorach WYSIWYG - mo�na tworzy� w pe�ni funkcjonalne
  szablony, kt�re nie psuj� si� po ka�dym u�yciu Dreamweavera(tm) czy
  edytora Mozilli; przy dodawaniu p�tli i warunk�w u�ywane s� atrybuty
  z przestrzeniami nazw
- ekstremalnie szybki - kod uruchomieniowy jest przynajmniej 4 razy
  mniejszy ni� wi�kszo�� innych silnik�w szablon�w (np. Smarty); u�ywa
  skompilowanych szablon�w, dzi�ki czemu jest wiele razy szybszy na
  blokach i p�tlach ni� szablony oparte na wyra�eniach regularnych
  (np. IT/phplib)
- bezpieczniejszy (pod k�tem atak�w cross-site scripting) - wszystkie
  zmienne domy�lnie s� wypisywane z u�yciem sekwencji kontrolnych HTML
  (mo�na to zmieni� modyfikatorem :h)
- wspiera wieloj�zyczno�� - przetwarza �a�cuchy z szablonu, co pozwala
  na zbudowanie narz�dzi do t�umaczenia; kompiluje specyficzne dla
  j�zyka szablony, dzi�ki czemu t�umaczenie jest robione tylko raz, a
  nie przy ka�dym ��daniu
- w pe�ni obs�uguje dynamiczne elementy (jak ASP.NET), dzi�ki czemu
  mo�na pobiera� elementy do zast�pienia w czasie dzia�ania.

D�ugoterminowym planem rozwoju Flexy jest zintegrowanie jako backend
dla Future Template Package (dost�pny b�dzie wrapper BC, jako �e autor
te� musi tego u�ywa�).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c
cd %{_pearname}-%{version}
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/{Compiler/{Flexy,Standard,Regex},Element,Plugin,Token}
	
install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/Flexy/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy
install %{_pearname}-%{version}/Flexy/Compiler/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Compiler
install %{_pearname}-%{version}/Flexy/Compiler/Flexy/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Compiler/Flexy
install %{_pearname}-%{version}/Flexy/Compiler/Standard/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Compiler/Standard
install %{_pearname}-%{version}/Flexy/Compiler/Regex/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Compiler/Regex
install %{_pearname}-%{version}/Flexy/Element/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Element
install %{_pearname}-%{version}/Flexy/Plugin/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Plugin
install %{_pearname}-%{version}/Flexy/Token/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Token

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{Flexy/example.ini,tests}
%{php_pear_dir}/%{_class}/%{_subclass}/Flexy
%{php_pear_dir}/%{_class}/%{_subclass}/Flexy.php
