%define		plugin		pageredirect
Summary:	DokuWiki Page Redirect Plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	2
Release:	0.2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://wiki.zyberdog.dk/_media/php/dw/pageredirect/pageredirect_current.zip
# Source0-md5:	ee8fbe1f5686c43441e07e2dc4c82e37
Source1:	dokuwiki-find-lang.sh
Patch0:		%{name}-pagematch.patch
URL:		http://wiki.splitbrain.org/plugin:page_redirector
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_dokudir	/usr/share/dokuwiki
%define		_plugindir	%{_dokudir}/lib/plugins/%{plugin}

%description
This plugin allows you to redirect users between pages and namespaces
by adding a particular pattern to a page.

%prep
%setup -q -n %{plugin}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}
cp -a . $RPM_BUILD_ROOT%{_plugindir}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{_plugindir}
%{_plugindir}/*.php
%{_plugindir}/*.css
%{_plugindir}/conf
%{_plugindir}/images
