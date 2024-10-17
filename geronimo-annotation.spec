%{?_javapackages_macros:%_javapackages_macros}
%global spec_ver 1.1
%global spec_name geronimo-annotation_%{spec_ver}_spec

Name:             geronimo-annotation
Version:          1.0
Release:          14.1%{?dist}
Summary:          Java EE: Annotation API v1.1
License:          ASL 2.0
URL:              https://geronimo.apache.org/

Source0:          http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{spec_name}/%{version}/%{spec_name}-%{version}-source-release.tar.gz
BuildArch:        noarch

BuildRequires:    java-devel >= 1:1.6.0
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    geronimo-parent-poms
BuildRequires:    maven-resources-plugin

Requires:         java >= 1:1.6.0
Requires:         jpackage-utils

Provides:         annotation_api = %{spec_ver}

%description
This package defines the common annotations.

%package javadoc
Summary:          Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{spec_name}-%{version}
sed -i 's/\r//' LICENSE NOTICE
%pom_set_parent org.apache.geronimo.specs:specs:1.4

%mvn_alias : org.apache.geronimo.specs:geronimo-annotation_1.0_spec
%mvn_alias : javax.annotation:jsr250-api
%mvn_alias : org.eclipse.jetty.orbit:javax.annotation

%mvn_file : %{name} annotation

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Aug 08 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-14
- Update to latest packaging guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-12
- Add depmap for org.eclipse.jetty.orbit
- Resolves: rhbz#917620

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-10
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Aug 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-9
- Install NOTICE file

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar  6 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-7
- Add javax.annotation:jsr250-api to depmap

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 16 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0-5
- Build with maven 3.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 4 2010 Chris Spike <chris.spike@arcor.de> 1.0-3
- Added 'org.apache.geronimo.specs:geronimo-annotation_1.0_spec' to maven depmap

* Mon Jul 26 2010 Chris Spike <chris.spike@arcor.de> 1.0-2
- Fixed whitespace/tabs use
- Fixed wrong EOL encoding

* Sun Jul 18 2010 Chris Spike <chris.spike@arcor.de> 1.0-1
- Initial version of the package
