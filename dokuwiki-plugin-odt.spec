%define		plugin		odt
Summary:	DokuWiki odt (Open Document Text) Export Plugin
Summary(pl-UTF8):	Wtyczka do eksportowania plików odt (Open Document Text)
Name:		dokuwiki-plugin-%{plugin}
Version:	20080219
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://wiki.splitbrain.org/_media/plugin:odt-plugin-2008-02-19.tgz
# Source0-md5:	f79363c82281978e274442164581d91a
Source1:	dokuwiki-find-lang.sh
Patch0:		http://gauret.free.fr/fichiers/dokuwiki/dokuwiki-odt-20070626.patch
URL:		http://wiki.splitbrain.org/plugin:odt
Requires:	dokuwiki >= 20070626
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.txt
%{plugindir}/*.png
%{plugindir}/*.xml
%{plugindir}/*.php
