%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Template
%define		_pearname	%{_class}_%{_subclass}_Flexy
Summary:	%{_pearname} - A Flexible Caching Template Engine Based on SimpleTemplate
Summary(pl):	%{_pearname}
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
Patch0:		%{name}-cosmetic.patch
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
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

%prep
%setup -q -c
cd %{_pearname}-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Filter

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/Flexy/Filter/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Filter/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/Flexy/example.ini
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Flexy
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Filter
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Flexy/Filter/*.php
