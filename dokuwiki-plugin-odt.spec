%define		subver	2017-02-18
%define		ver		%(echo %{subver} | tr -d -)
%define		plugin		odt
%define		php_min_version 5.5
Summary:	OpenOffice.org/LibreOffice.org Export
Summary(pl.UTF-8):	Wtyczka do eksportowania plików odt (Open Document Text)
Name:		dokuwiki-plugin-%{plugin}
Version:	%{ver}
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/LarsGit223/dokuwiki-plugin-odt/archive/%{subver}/%{name}-%{ver}.tar.gz
# Source0-md5:	6768d4d2e55c676bc46ef877abaeeb34
URL:		https://www.dokuwiki.org/plugin:odt
Requires:	dokuwiki >= 20150810
Requires:	php(core) >= %{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
This plugin allows you to export a page to the OpenDocument format
used by OpenOffice.org, LibreOffice.org and other word processors.

This is especially useful when you need to print or to give a single
page to a customer.

Hint: OpenOffice.org can also export to PDF.

%description -l pl.UTF-8
Ta wtyczka pozwala na eksportowanie strony do formatu OpenDocument,
używanego przez Open Office i inne edytory tekstu. Przydatna jest w
sytuacji w której musisz dać pojedyńczą stronę klientowi.

Podpowiedź: Open Office pozwala także na eksportowanie do PDF.

%prep
%setup -q -n %{name}-%{subver}

%build
version=$(awk '/^date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/deleted.files
%{__rm} $RPM_BUILD_ROOT%{plugindir}/phpdoc.dist.xml
%{__rm} $RPM_BUILD_ROOT%{plugindir}/{ChangeLog,README}.txt

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
%{plugindir}/*.css
%{plugindir}/*.php
%{plugindir}/*.png
%{plugindir}/*.txt
%{plugindir}/*.xml
%{plugindir}/ODT
%{plugindir}/action
%{plugindir}/conf
%{plugindir}/helper
%{plugindir}/renderer
