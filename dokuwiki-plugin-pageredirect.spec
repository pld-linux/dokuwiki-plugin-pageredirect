%define		plugin	pageredirect
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	DokuWiki Page Redirect Plugin
Summary(pl.UTF-8):	Wtyczka Page Redirect (przekierowywania stron) dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20140414
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/glensc/dokuwiki-plugin-pageredirect/tarball/%{version}/%{name}-%{version}.tgz
# Source0-md5:	ca7026838d5dc84eeabddb958f479d45
URL:		https://www.dokuwiki.org/plugin:pageredirect
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	dokuwiki >= 20061106
Requires:	php(core) >= %{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
This plugin allows you to redirect users between pages and namespaces
by adding a particular pattern to a page.

%description -l pl.UTF-8
Ta wtyczka pozwala przekierowywać użytkowników między stronami i
przestrzeniami nazw poprzez dodawanie określonych oznaczeń na stronie.

%prep
%setup -qc
mv *-%{plugin}-*/{.??*,*} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm -rf $RPM_BUILD_ROOT%{plugindir}/{.travis.yml,_test}

# find locales
%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.txt
%{plugindir}/*.php
%{plugindir}/*.css
%{plugindir}/conf
%{plugindir}/images
