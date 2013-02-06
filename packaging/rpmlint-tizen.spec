#
# spec file for package rpmlint-Factory
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           rpmlint-tizen
Requires:       rpmlint-mini
Summary:        Rpm correctness checker - Tizen Trunk configuration
License:        GPL-2.0+
Group:          System/Packages
Version:        1.0
Release:        0
Url:            http://rpmlint.zarb.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source1:        COPYING
Source2:        config
Source3:        config.strict
BuildArch:      noarch

%description
Rpmlint is a tool to check common errors on rpm packages. This package
provides the configuration specific for SUSE Factory.

%package strict
Summary:        Confict only applying to openSUSE:Factory itself
Group:          System/Packages

%description strict
Forbid invalid licenses

%prep
cp %{SOURCE1} .

%build

%install
install -m 644 -D %{SOURCE2} $RPM_BUILD_ROOT/etc/rpmlint/factory.config
install -m 644 -D %{SOURCE3} $RPM_BUILD_ROOT/etc/rpmlint/factory-strict.config

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc COPYING
%dir /etc/rpmlint
/etc/rpmlint/factory.config

%files strict
%defattr(-,root,root,0755)
%dir /etc/rpmlint
/etc/rpmlint/factory-strict.config

%changelog
