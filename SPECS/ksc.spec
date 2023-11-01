Name:		ksc
Version:	1.9
Release:	2%{?dist}
Summary:	Kernel source code checker
Group:		Development/Tools
AutoReqProv:	no
License:	GPLv2+
URL:		https://github.com/RedHatOfficial/ksc
Source0:	ksc-%{version}.tar.gz
BuildArch:	noarch
%{?__python3:Requires: %{__python3}}
Requires:	(kernel-abi-whitelists or kernel-abi-stablelists)
Requires:	kmod
Requires:	binutils
Requires:	kernel-devel
Requires:	python3-magic
Requires:	python3-requests
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
Patch0:		Replace-python3-with-platform-python.patch

%description
A kernel module source code checker to find usage of non whitelist symbols

%prep
%setup -q
%patch0 -p1

%build
%py3_build

%install
%{__python3} setup.py install -O1 --root %{buildroot}
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
* Mon Feb 21 2022 Čestmír Kalina <ckalina@redhat.com> - 1.9-2
- Resolves: #2043450 ksc: Support Authorization header in bugzilla API
- Use platform-python in place of python3
* Fri Feb 11 2022 Čestmír Kalina <ckalina@redhat.com> - 1.9-1
- Resolves: #2043450 ksc: Support Authorization header in bugzilla API
- Rebase to latest ksc release
* Mon May 17 2021 Čestmír Kalina <ckalina@redhat.com> - 1.8-3
- Resolves: #1954340 ksc: i18n issues,
- Add release to Source0
* Tue Jan 05 2021 Čestmír Kalina <ckalina@redhat.com> - 1.7-1
- Resolves: #1886901 Avoid divisive language
- Resolves: #1912506 File bugs with Tracking keyword by default
* Wed Nov 06 2019 Čestmír Kalina <ckalina@redhat.com> - 1.6-2
- Resolves: #1729039 Extend ksc output to include environment metadata
- (OSCI) Add kmod to Makefile-generated Requires
* Wed Nov 06 2019 Čestmír Kalina <ckalina@redhat.com> - 1.6-1
- Resolves: #1729039 Extend ksc output to include environment metadata
- Add modinfo vermagic field to the output.
- Add kmod (provides modinfo) to requires.
* Thu Nov 29 2018 Čestmír Kalina <ckalina@redhat.com> - 1.5-1
- Resolves: #1647528 ksc add feature to copy justifications between ksc...
- Resolves: #1648026 ksc add a non-processed .ko file
- Resolves: #1647974 piped input causes ksc to fail when asking for user input
- Add support for justification carry over.
- Add support for symbol filtering using -K.
- Fix input problems when piping through to ksc.
- Extend manpage with EXAMPLES section.
- Version bump fo 1.5.

* Tue Nov 06 2018 Cestmir Kalina <ckalina@redhat.com> - 1.4-1
- Resolves: #1643187 ksc manpage lies -k can only be specified once
- Resolves: #1645335 FILE is shown in ksc man page but no explain or effect
- Support for multiple -k arguments added
- Man page reworded to match ksc behaviour

* Tue Oct 30 2018 Cestmir Kalina <ckalina@redhat.com> - 1.3-1
- Resolves: #1642134 Error restrict bugs to groups without permission while
  trying to submit RHEL8 symbols
- New ksc reports will no longer be submitted under redhat bugzilla group.
- At least one bugzilla group must be specified by a ksc user, otherwise ksc
  will terminate with an error.
- Version bump to 1.3

* Tue Oct 23 2018 Cestmir Kalina <ckalina@redhat.com> - 1.2-1
- Version bump to resolve RPMDiff blockers.
- Related: #1641485

* Mon Oct 22 2018 Cestmir Kalina <ckalina@redhat.com> - 1.1-5
- Fix ksc report type error when executing against a no-exist file
- Resolves: #1641485

* Wed Oct 10 2018 Cestmir Kalina <ckalina@redhat.com> - 1.1-4
- Fix Requires so that rhpkg build does not fail when invoked.
- Related: #1619153

* Tue Oct 09 2018 Cestmir Kalina <ckalina@redhat.com> - 1.1-3
- Bump version to 1.1
- Related: #1633691
- Resolves: #1637594

* Tue Oct 09 2018 Cestmir Kalina <ckalina@redhat.com> - 1.1-1
- Replace the Python interpreter path to RHEL8 compliant path.
- Related: #1633691
- Resolves: #1637594

* Thu Sep 20 2018 Tomas Orsava <torsava@redhat.com> - 1.0-2
- Require the Python interpreter directly instead of using the package name
- Related: rhbz#1619153

* Fri Sep 7 2018 Cestmir Kalina <ckalina@redhat.com> - 1.0-1
- Resolves: #1623321

* Mon Jun 4 2018 Stanislav Kozina <skozina@redhat.com> - 0.9.24-1
- Remove options -d and --internal

* Wed May 2 2018 Petr Oros <poros@redhat.com> - 0.9.23-1
- Port for python 3

* Wed Dec 13 2017 Martin Lacko <mlacko@redhat.com> - 0.9.22-1
- Resolves: #1524779

* Tue Dec 5 2017 Martin Lacko <mlacko@redhat.com> - 0.9.21-1
- Resolves: #1520224

* Tue Nov 28 2017 Martin Lacko <mlacko@redhat.com> - 0.9.20-1
- Resolves: #1502930

* Tue Nov 7 2017 Stanislav Kozina <skozina@redhat.com> - 0.9.19-1
- Resolves: #1432864
- Resolves: #1500383
- Resolves: #1502930
- Resolves: #1503526
- Resolves: #1503603
- Resolves: #1503964
- Resolves: #1499249
- Resolves: #1441455
- Resolves: #1481310
- Resolves: #1456140

* Mon Sep 5 2016 Stanislav Kozina <skozina@redhat.com> - 0.9.18-1
- Resolves: #1373120

* Mon Aug 15 2016 Stanislav Kozina <skozina@redhat.com> - 0.9.17-1
- Add -y option to provide path to the Module.symvers file
- Resolves: #1366929
- Resolves: #1366952

* Fri Jul 15 2016 Stanislav Kozina <skozina@redhat.com> - 0.9.16-3
- Fix requires
- Resolves: #1356905

* Wed May 04 2016 Stanislav Kozina <skozina@redhat.com> - 0.9.16-1
- embed python-bugzilla interface to get rid of the package dependency
- Resolves: #1332810

* Tue Apr 26 2016 Stanislav Kozina <skozina@redhat.com> - 0.9.15-1
- always load whitelist file from kernel-abi-whitelists package, remove the attached files
- always load Module.symvers file from kernel-devel package, remove attached files
- use python-bugzilla instead of private bz_xmlrpc package
- Resolves: #1328384
- Resolves: #906664
- Resolves: #906659
- Resolves: #1272348

* Tue Feb 25 2014 Jiri Olsa <jolsa@redhat.com> - 0.9.11-1
- Resolves: #1066162

* Fri Jan 10 2014 Jiri Olsa <jolsa@redhat.com> - 0.9.10-1
- Resolves: #1051506

* Fri Jan 10 2014 Jiri Olsa <jolsa@redhat.com> - 0.9.9-2
- added binutils cpp file dependencies
- Resolves: #1051411

* Thu Jan 09 2014 Jiri Olsa <jolsa@redhat.com> - 0.9.9-1
- updating to version 0.9.9
- Resolves: #881654
- Resolves: #1028410
- Resolves: #1045025
- Resolves: #1045368
- Resolves: #1045388

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.9.8-2
- Mass rebuild 2013-12-27

* Mon Nov 18 2013 Jiri Olsa <jolsa@redhat.com> - 0.9.8-1
- updating to version 0.9.8
- Resolves: #1028410

* Tue Aug 20 2013 Jiri Olsa <jolsa@redhat.com> - 0.9.5-1
- updating to version 0.9.5

* Fri Nov 30 2012 Jiri Olsa <jolsa@redhat.com> - 0.9.3-3
- removing kabi-whitelists dependency

* Fri Nov 30 2012 Jiri Olsa <jolsa@redhat.com> - 0.9.3-2
- spec file updates

* Fri Nov 30 2012 Jiri Olsa <jolsa@redhat.com> - 0.9.3-1
- new version with license info updated

* Tue Nov 20 2012 Jiri Olsa <jolsa@redhat.com> - 0.9.2-1
- initial
