%define name	dns2tcp
%define version	0.5.2
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Tunnel TCP over DNS
Group:		Networking/Other
License:	GPLv2+
URL:		http://www.hsc.fr/ressources/outils/dns2tcp/
Source0:	http://www.hsc.fr/ressources/outils/dns2tcp/download/%{name}-%{version}.tar.gz
Source1: 	dns2tcpd.init
Source2: 	dns2tcpd.conf
Source3: 	dns2tcpc.init
Source4: 	dns2tcpc.conf
BuildRequires:  openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Dns2tcp is a tool for relaying TCP connections over DNS. There is no
authentications nor encryption mecanisms : DNS encapsulation must be
considered as an unsecure and anonymous transport layer. Ressources should
be public external services like ssh, ssltunnel ... 

%package	client
Summary:	dns2tcp client (Tunnel TCP over DNS)
Group:		Networking/Other

%description	client
Dns2tcp is a tool for relaying TCP connections over DNS. There is no
authentications nor encryption mecanisms : DNS encapsulation must be
considered as an unsecure and anonymous transport layer. Ressources should
be public external services like ssh, ssltunnel ...

This package contains the client part.

%package	server
Summary:	dns2tcp server (Tunnel TCP over DNS)
Group:		Networking/Other

%description	server
Dns2tcp is a tool for relaying TCP connections over DNS. There is no
authentications nor encryption mecanisms : DNS encapsulation must be
considered as an unsecure and anonymous transport layer. Ressources should
be public external services like ssh, ssltunnel ...

This package contains the server part.

%prep
%setup -q 

%build
%configure2_5x
%make


%install
rm -rf %{buildroot}
%makeinstall
mkdir -p %{buildroot}/%_initrddir/
mkdir -p %{buildroot}/%_sysconfdir/
install -m 0755 %SOURCE1 %{buildroot}/%_initrddir/dns2tcpd
install -m 0755 %SOURCE2 %{buildroot}/%_sysconfdir/dns2tcpd.conf
install -m 0755 %SOURCE3 %{buildroot}/%_initrddir/dns2tcpc
install -m 0755 %SOURCE4 %{buildroot}/%_sysconfdir/dns2tcpc.conf

%clean
rm -rf %{buildroot}

%post server
%_post_service dns2tcpd
%preun server
%_preun_service dns2tcpd

%post client
%_post_service dns2tcpc
%preun client
%_preun_service dns2tcpc

%files server
%defattr(-,root,root)
%doc README COPYING ChangeLog
%{_bindir}/dns2tcpd
%{_initrddir}/dns2tcpd
%config(noreplace) %{_sysconfdir}/dns2tcpd.conf
%{_mandir}/man1/dns2tcpd.1.*

%files client
%defattr(-,root,root)
%doc README COPYING ChangeLog
%{_bindir}/dns2tcpc
%{_initrddir}/dns2tcpc
%config(noreplace) %{_sysconfdir}/dns2tcpc.conf
%{_mandir}/man1/dns2tcpc.1.*



%changelog
* Wed Jul 28 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.5.2-1mdv2011.0
+ Revision: 562860
- 0.5.2

* Mon Apr 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.5-1mdv2010.1
+ Revision: 536812
- new version

* Sun Dec 20 2009 Michael Scherer <misc@mandriva.org> 0.4.3-4mdv2010.1
+ Revision: 480323
- fix build, as glibc now declare strnlen, which conflict with some symbols
- do not chroot to a inexistant directory

* Fri Dec 26 2008 Pascal Terjan <pterjan@mandriva.org> 0.4.3-3mdv2009.1
+ Revision: 319531
- Only change it for client, server already detach itself
- Fix initscripts so that they don't block boot

* Fri Nov 07 2008 Pascal Terjan <pterjan@mandriva.org> 0.4.3-2mdv2009.1
+ Revision: 300760
- Tag config files as such

* Fri Nov 07 2008 Pascal Terjan <pterjan@mandriva.org> 0.4.3-1mdv2009.1
+ Revision: 300720
- Update to 0.4.3 (Security fix for SA32514)
- Fix condrestart command in services
- Fix status command in services

* Sat Sep 06 2008 Pascal Terjan <pterjan@mandriva.org> 0.4.1-1mdv2009.1
+ Revision: 281898
- import dns2tcp


* Sat Sep  6 2008 Pascal Terjan <pterjan@mandriva.org> 0.4.1-1mdv2009.0
- First version of the package

