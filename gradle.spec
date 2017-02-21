Summary:	Groovy based build system
Name:		gradle
Version:	3.4
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Java
Source0:	http://services.gradle.org/distributions/%{name}-%{version}-bin.zip
# Source0-md5:	d172a02b7ac1a2fea9b60bb00d95f8ca
URL:		http://www.gradle.org/
Requires:	jdk >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gradle is a build system written in Groovy. It uses Groovy
also as the language for its build scripts. It has a powerful
multi-project build support. It has a layer on top of Ivy
that provides a build-by-convention integration for Ivy. It
gives you always the choice between the flexibility of Ant
and the convenience of a build-by-convention behavior.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/bin}
ln -sf %{_datadir}/%{name}/bin/gradle $RPM_BUILD_ROOT%{_bindir}/gradle

install -d $RPM_BUILD_ROOT
install bin/gradle $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
cp -a lib media $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NOTICE getting-started.html
%attr(755,root,root) %{_bindir}/gradle
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%attr(755,root,root) %{_datadir}/%{name}/bin/gradle
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/media
