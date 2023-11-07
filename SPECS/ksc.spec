%global forgeurl https://github.com/RedHatOfficial/ksc
%global commitdate 20230109
%global commit 869a25c7de8ed880a72f66ae4f3e8407f1aa4114
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%{?python_enable_dependency_generator}
%forgemeta -i

Name:		ksc
Version:	1.12
Release:	4%{?dist}
Summary:	Kernel source code checker
Group:		Development/Tools
AutoReqProv:	no
License:	GPLv2+
URL:		https://github.com/RedHatOfficial/ksc
BuildArch:	noarch
Requires:	kmod
Requires:	binutils
Requires:	kernel-devel
Requires:	python3-requests
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
Source0:	https://github.com/RedHatOfficial/ksc/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:		0001-manpage.patch
Patch1:		0002-c9s-notifications.patch

%description
A kernel module source code checker to find usage of select symbols

%prep
%forgesetup
%patch0 -p1
%patch1 -p1

%build
%py3_build

%install
%py3_install
install -D ksc.1 %{buildroot}%{_mandir}/man1/ksc.1

%files
%license COPYING
%doc README PKG-INFO
%{_bindir}/ksc
%{_datadir}/ksc
%{_mandir}/man1/ksc.*
%config(noreplace) %{_sysconfdir}/ksc.conf
%{python3_sitelib}/ksc-%{version}*.egg-info

%changelog
* Mon Mar 06 2023 Čestmír Kalina <ckalina@redhat.com> - 1.12-3
- Resolves: #2165820 - The email method always mark CentOS Stream as release

* Mon Jan 23 2023 Čestmír Kalina <ckalina@redhat.com> - 1.12-2
- Resolves: #2066231 - add manpage docs

* Mon Jan 09 2023 Čestmír Kalina <ckalina@redhat.com> - 1.12-1
- Resolves: #2066231 - update to ksc 1.12

* Mon Jun 13 2022 Čestmír Kalina <ckalina@redhat.com> - 1.11-2
- Resolves: #2066228 - Explicitly require target specification

* Wed May 18 2022 Čestmír Kalina <ckalina@redhat.com> - 1.11-1
- Resolves: #2066228 - Explicitly require target specification

* Wed Apr 13 2022 Čestmír Kalina <ckalina@redhat.com> - 1.10-1
- Resolves: #2066226 Drop mandatory kernel-abi-stablelist dependency

* Wed Feb 09 2022 Čestmír Kalina <ckalina@redhat.com> - 1.9-1
- Resolves: #2043447 ksc: Support Authorization header in bugzilla API

* Sun Dec 19 2021 Čestmír Kalina <ckalina@redhat.com> - 1.8-5
- Resolves: #2032138 add Red Hat Enterprise Linux 9 support

* Mon Nov 22 2021 Čestmír Kalina <ckalina@redhat.com> - 1.8-4
- Resolves: #1761398 Add symbol namespace support to ksc

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - Forge-specific packaging variables
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Tue Jun 01 2021 Ziqian SUN <zsun@redhat.com> - 1.8-2
- Adding python3-requests into Requires.

* Mon May 17 2021 Čestmír Kalina <ckalina@redhat.com> - 1.8-1
- Resolves: #1954495 ksc: i18n issues

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - Forge-specific packaging variables
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 05 2021 Čestmír Kalina <ckalina@redhat.com> - 1.7-1
- Initial Fedora commit.
