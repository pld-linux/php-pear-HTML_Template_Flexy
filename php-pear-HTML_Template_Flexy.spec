%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Template
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Flexy
Summary:	%{_pearname} - A Flexible Caching Template Engine Based on SimpleTemplate
Summary(pl):	%{_pearname} - elastyczny buforuj�cy silnik szablon�w oparty na SimpleTemplate
Name:		php-pear-%{_pearname}
Version:	0.3
Release:	0.9
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	b6e525b838148852d91ba0106273566e
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
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
Flexy Template to silnik szablon�w do konwertera kodu PHP, bazowany na
Simple Template i podobny do Smarty. Powinien by� bardzo szybki, jest
�atwy w rozszerzaniu, rozwijaniu i u�ywaniu dowolnej sk�adni
szablon�w. Domy�lny filtr (SimpleTags) zawiera: zmienne, p�tle
foreach, warunki, wywo�ania metod, w��czanie kodu, obs�uguje znaczniki
zakodowane w URL-ach - wi�c mo�e modyfikowa� szablony w Mozilli itp.
Inne filtry to:
 - RtfSimpletags - do tworzenia dokument�w RTF dla Worda,
 - BodyOnly - wycinaj�cy nag��wek i stopk� z szablonu,
 - Php - wycinaj�cy kod php z szablonu,
 - Email - do przetwarzania szablon�w e-mail.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/{Filter,Token}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/Flexy/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/
install %{_pearname}-%{version}/Flexy/Filter/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Filter/
install %{_pearname}-%{version}/Flexy/Token/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Token/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/Flexy/example.ini
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Flexy
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Filter
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Token
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Filter/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Token/*.php
