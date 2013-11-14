Name:		aufs-util
Version:	3.2
Release:	1%{?dist}
Summary:	Utilities for managing aufs filesystems

Group:		System Environment/Base
License:	GPLv2
URL:		http://github.com/Lax/aufs-util/
Source0:	aufs-util.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release})

BuildRequires:	kernel-uek-headers
Requires:	kernel-uek

%description
These utilities are always necessary for aufs.

%prep
rm -rf aufs-util-%{version}/
tar jxvf %{SOURCE0}

%build
cd aufs-util-3.2/
make all %{?_smp_mflags}


%install
rm -rf %{buildroot}
cd aufs-util-3.2/
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
/etc/default/aufs
/sbin/auibusy
/sbin/auplink
/sbin/mount.aufs
/sbin/umount.aufs
/usr/bin/aubrsync
/usr/bin/aubusy
/usr/bin/auchk
/usr/lib/libau.so
/usr/lib/libau.so.2
/usr/lib/libau.so.2.7
/usr/share/man/man5/aufs.5.gz


%changelog

