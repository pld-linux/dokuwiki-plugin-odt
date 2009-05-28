%define		plugin		odt
Summary:	DokuWiki odt (Open Document Text) Export Plugin
Summary(pl-UTF8):	Wtyczka do eksportowania plików odt (Open Document Text)
Name:		dokuwiki-plugin-%{plugin}
Version:	20090115
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://gauret.free.fr/fichiers/dokuwiki/dokuwiki-odt-%{version}.tgz
# Source0-md5:	278748da7659129ae9806b9726961e53
Source1:	dokuwiki-find-lang.sh
URL:		http://wiki.splitbrain.org/plugin:odt
Requires:	dokuwiki >= 20070626
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
This plugin allows you to export a page to the OpenDocument format
used by Open Office and other word processors. This is especially
useful when you need to give a single page to a customer

Hint: Open Office can also export to PDF.

%description -l pl-UTF8
Ta wtyczka pozwala na eksportowanie strony do formatu OpenDocument,
używanego przez Open Office i inne edytory tekstu. Przydatna jest
w sytuacji w której musisz dać pojedyńczą stronę klientowi.

Podpowiedź: Open Office pozwala także na eksportowanie do PDF.

%prep
%setup -q -n %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm -f $RPM_BUILD_ROOT%{plugindir}/{ChangeLog,.gitignore}

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
%doc ChangeLog
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.txt
%{plugindir}/*.png
%{plugindir}/*.xml
%{plugindir}/*.php
%dir %{plugindir}/conf
%{plugindir}/conf/*.php
