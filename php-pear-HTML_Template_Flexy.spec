%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Template
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_Flexy

Summary:	%{_pearname} - a flexible caching template engine based on SimpleTemplate
Summary(pl):	%{_pearname} - elastyczny buforuj±cy silnik szablonów oparty na SimpleTemplate
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ac684af4c1f06230f6c261a6bbd2c262
Patch0:		%{name}-case_fix.patch
URL:		http://pear.php.net/package/HTML_Template_Flexy/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML_Template_Flexy started it's life as a simplification of HTML_Template_Xipe,
however in Version 0.2, It became one of the first template engine to use a real Lexer,
rather than regex'es, making it possible to do things like ASP.net or Cold Fusion tags.
However, it still has a very simple set of goals.
- Very Simple API,
   o easy to learn...
   o prevents to much logic going in templates
- Easy to write document'able code
   o By using object vars for a template rather than 'assign', you
     can use PHPDoc comments to list what variable you use.
- Editable in WYSIWYG editors
   o you can create full featured templates, that doesnt get broken every time you edit with
     Dreamweaver(tm) or Mozzila editor
   o Uses namespaced attributes to add looping/conditionals
- Extremely Fast,
   o runtime is at least 4 time smaller than most other template engines (eg. Smarty)
   o uses compiled templates, as a result it is many times faster on blocks and loops than
     than Regex templates (eg. IT/phplib)
- Safer (for cross site scripting attacks)
   o All variables default to be output as HTML escaped (overridden with the :h modifier)
- Multilanguage support
   o Parses strings out of template, so you can build translation tools
   o Compiles language specific templates (so translation is only done once, not on every request)
- Full dynamic element support (like ASP.NET), so you can pick elements to replace at runtime

Features:
- {variable} to echo $object->variable
- {method()} to echo $object->method();
- {foreach:var,key,value} to PHP foreach loops
- tag attributes FLEXY:FOREACH, FLEXY:IF for looping and conditional HTML inclusion
- {if:variable} to PHP If statement
- {if:method()} to PHP If statement
- {else:} and {end:} to close or alternate If statements
- FORM to HTML_Template_Flexy_Element's
- replacement of INPUT, TEXTAREA and SELECT tags with HTML_Template_Flexy_Element code
  use FLEXY:IGNORE (inherited) and FLEXY:IGNOREONLY (single) to prevent replacements
- FLEXY:START/FLEXY:STARTCHILDREN tags to define where template starts/finishes
- support for urlencoded braces {} in HTML attributes.
- documentation in the pear manual

- examples at http://cvs.php.net/cvs.php/pear/HTML_Template_Flexy/tests/

The long term plan for Flexy is to be integrated as a backend for the Future
Template Package (A BC wrapper will be made available - as I need to use it
too!)

In PEAR status of this package is: %{_status}.

%description -l pl
Flexy Template to silnik szablonów do konwertera kodu PHP, oparty na
Simple Template i podobny do Smarty. Powinien byæ bardzo szybki, jest
³atwy w rozszerzaniu, rozwijaniu i u¿ywaniu dowolnej sk³adni
szablonów. Domy¶lny filtr (SimpleTags) zawiera: zmienne, pêtle
foreach, warunki, wywo³ania metod, w³±czanie kodu, obs³uguje znaczniki
zakodowane w URL-ach - wiêc mo¿e modyfikowaæ szablony w Mozilli itp.
Inne filtry to:
 - RtfSimpletags - do tworzenia dokumentów RTF dla Worda,
 - BodyOnly - wycinaj±cy nag³ówek i stopkê z szablonu,
 - Php - wycinaj±cy kod PHP z szablonu,
 - Email - do przetwarzania szablonów e-mail.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c
cd %{_pearname}-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/{Compiler/{Flexy,Standard,Regex},Token}
	
install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/Flexy/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy
install %{_pearname}-%{version}/Flexy/Compiler/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Compiler
install %{_pearname}-%{version}/Flexy/Compiler/Flexy/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Compiler/Flexy
install %{_pearname}-%{version}/Flexy/Compiler/Standard/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Compiler/Standard
install %{_pearname}-%{version}/Flexy/Compiler/Regex/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Compiler/Regex
install %{_pearname}-%{version}/Flexy/Token/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Token

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{Flexy/example.ini,tests}
%{php_pear_dir}/%{_class}/%{_subclass}/Flexy
%{php_pear_dir}/%{_class}/%{_subclass}/Flexy.php
