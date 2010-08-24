%define		plugin		pageredirect
Summary:	DokuWiki Page Redirect Plugin
Summary(pl.UTF-8):	Wtyczka Page Redirect (przekierowywania stron) dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	2
Release:	2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://wiki.zyberdog.dk/_media/php/dw/pageredirect/pageredirect_current.zip
# Source0-md5:	ee8fbe1f5686c43441e07e2dc4c82e37
Source1:	dokuwiki-find-lang.sh
Patch0:		%{name}-pagematch.patch
Patch1:		mute-warning.patch
URL:		http://www.dokuwiki.org/plugin:page_redirector
BuildRequires:	unzip
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
This plugin allows you to redirect users between pages and namespaces
by adding a particular pattern to a page.

%description -l pl.UTF-8
Ta wtyczka pozwala przekierowywać użytkowników między stronami i
przestrzeniami nazw poprzez dodawanie określonych oznaczeń na stronie.

%prep
%setup -q -n %{plugin}
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

# find locales
sh %{SOURCE1} %{name}.lang

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
%{plugindir}/*.php
%{plugindir}/*.css
%{plugindir}/conf
%{plugindir}/images
