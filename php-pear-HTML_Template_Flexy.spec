%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Template
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Flexy

Summary:	%{_pearname} - A Flexible Caching Template Engine Based on SimpleTemplate
Summary(pl):	%{_pearname} - elastyczny buforuj±cy silnik szablonów oparty na SimpleTemplate
Name:		php-pear-%{_pearname}
Version:	0.6.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	00ec49d17055eec5fac558ed528c3809
Patch0:		%{name}-case_fix.patch
URL:		http://pear.php.net/package/HTML_Template_Flexy/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flexy Template is a Template Engine to php code convertor, based on
Simple Template, and similar to Smarty. It should be very fast, and is
easy to extend to develop or use any template syntax you like. Default
filter (SimpleTags) includes: variables, foreach loops, conditionals,
method calls, includes, Handles urlencoded tags - so you can edit the
template in mozilla etc. Other filters include:
 - RtfSimpletags - to make RTF/Word documents,
 - BodyOnly - to strip header and footer from a template,
 - Php - to strip php code from template,
 - Email - For parsing email templates.

This class has in PEAR status: %{_status}.

%description -l pl
Flexy Template to silnik szablonów do konwertera kodu PHP, bazowany na
Simple Template i podobny do Smarty. Powinien byæ bardzo szybki, jest
³atwy w rozszerzaniu, rozwijaniu i u¿ywaniu dowolnej sk³adni
szablonów. Domy¶lny filtr (SimpleTags) zawiera: zmienne, pêtle
foreach, warunki, wywo³ania metod, w³±czanie kodu, obs³uguje znaczniki
zakodowane w URL-ach - wiêc mo¿e modyfikowaæ szablony w Mozilli itp.
Inne filtry to:
 - RtfSimpletags - do tworzenia dokumentów RTF dla Worda,
 - BodyOnly - wycinaj±cy nag³ówek i stopkê z szablonu,
 - Php - wycinaj±cy kod php z szablonu,
 - Email - do przetwarzania szablonów e-mail.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c
cd %{_pearname}-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/{Compiler/{Standard,Regex},Token}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/Flexy/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy
install %{_pearname}-%{version}/Flexy/Compiler/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Compiler
install %{_pearname}-%{version}/Flexy/Compiler/Standard/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Compiler/Standard
install %{_pearname}-%{version}/Flexy/Compiler/Regex/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Compiler/Regex
install %{_pearname}-%{version}/Flexy/Token/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Token

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/Flexy/example.ini
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Flexy
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Compiler/Standard
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Compiler/Regex
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Token
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Compiler/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Compiler/Standard/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Compiler/Regex/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Token/*.php
