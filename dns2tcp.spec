%define name	dns2tcp
%define version	0.4.3
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
BuildRoot:	%{_tmppath}/%{name}-root

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
%configure
%make


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir -p $RPM_BUILD_ROOT/%_initrddir/
mkdir -p $RPM_BUILD_ROOT/%_sysconfdir/
install -m 0755 %SOURCE1 $RPM_BUILD_ROOT/%_initrddir/dns2tcpd
install -m 0755 %SOURCE2 $RPM_BUILD_ROOT/%_sysconfdir/dns2tcpd.conf
install -m 0755 %SOURCE3 $RPM_BUILD_ROOT/%_initrddir/dns2tcpc
install -m 0755 %SOURCE4 $RPM_BUILD_ROOT/%_sysconfdir/dns2tcpc.conf

%clean
rm -rf $RPM_BUILD_ROOT

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
%{_sysconfdir}/dns2tcpd.conf
%{_mandir}/man1/dns2tcpd.1.*

%files client
%defattr(-,root,root)
%doc README COPYING ChangeLog
%{_bindir}/dns2tcpc
%{_initrddir}/dns2tcpc
%{_sysconfdir}/dns2tcpc.conf
%{_mandir}/man1/dns2tcpc.1.*

