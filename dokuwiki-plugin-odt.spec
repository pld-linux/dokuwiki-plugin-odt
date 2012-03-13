%define		plugin		odt
Summary:	DokuWiki odt (Open Document Text) Export Plugin
Summary(pl.UTF-8):	Wtyczka do eksportowania plików odt (Open Document Text)
Name:		dokuwiki-plugin-%{plugin}
Version:	20110616
Release:	1
License:	GPL v2
Group:		Applications/WWW
#Source0:	http://aurelien.bompard.org/projects/files/dokuwiki-odt/dokuwiki-odt-%{version}.zip
Source0:	http://gitorious.org/dokuwiki-odt/dokuwiki-odt/archive-tarball/master#/%{name}-%{version}.tgz
# Source0-md5:	a30fe453e3036014c82e5b5e9a7c47b0
Patch0:		dokuwiki-ziplib.patch
Patch1:		geshi.patch
URL:		http://www.dokuwiki.org/plugin:odt
Requires:	dokuwiki >= 20070626
Requires:	php-common >= 4:5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
This plugin allows you to export a page to the OpenDocument format
used by Open Office and other word processors. This is especially
useful when you need to give a single page to a customer

Hint: Open Office can also export to PDF.

%description -l pl.UTF-8
Ta wtyczka pozwala na eksportowanie strony do formatu OpenDocument,
używanego przez Open Office i inne edytory tekstu. Przydatna jest w
sytuacji w której musisz dać pojedyńczą stronę klientowi.

Podpowiedź: Open Office pozwala także na eksportowanie do PDF.

%prep
%setup -qc
mv dokuwiki-odt-dokuwiki-odt/* .
%patch0 -p1
%patch1 -p1

version=$( awk '/^date/{print $2}' info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
#	exit 1
fi

rm -f ZipLib.class.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a conf lang *.php *.png *.xml info.txt $RPM_BUILD_ROOT%{plugindir}
rm -f $RPM_BUILD_ROOT%{plugindir}/{ChangeLog,.gitignore}

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
%doc ChangeLog.txt README.txt
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.txt
%{plugindir}/*.png
%{plugindir}/*.xml
%{plugindir}/*.php
%{plugindir}/conf
