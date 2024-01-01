#global optflags %{optflags} -fcommon

Name:		dns2tcp
Version:	0.5.2
Release:	7
Summary:	Tunnel TCP over DNS
Group:		Networking/Other
License:	GPLv2+
URL:		https://github.com/alex-sector/dns2tcp
Source0:	https://codeload.github.com/alex-sector/dns2tcp/tar.gz/refs/tags/v%{version}#/%{name}-%{version}.tar.gz
Source1: 	dns2tcpd.service
Source2: 	dns2tcpd.conf
Source3: 	dns2tcpc.service
Source4: 	dns2tcpc.conf
Patch0:		dns2tcp-0.5.2-compile.patch
BuildRequires:  pkgconfig(openssl)

%description
Dns2tcp is a tool for relaying TCP connections over DNS. There is no
authentications nor encryption mecanisms : DNS encapsulation must be
considered as an unsecure and anonymous transport layer. Ressources should
be public external services like ssh, ssltunnel ... 

%package	client
Summary:	Client for dns2tcp (Tunnel TCP over DNS)
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
%autosetup -p1
%configure

%build
%make_build

%install
%make_install

install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/dns2tcpd.service
install -D -m 0755 %{SOURCE2} %{buildroot}%{_sysconfdir}/dns2tcpd.conf
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/dns2tcpc.service
install -D -m 0755 %{SOURCE4} %{buildroot}%{_sysconfdir}/dns2tcpc.conf

%files server
%doc README COPYING ChangeLog
%{_bindir}/dns2tcpd
%{_unitdir}/dns2tcpd.service
%config(noreplace) %{_sysconfdir}/dns2tcpd.conf
%{_mandir}/man1/dns2tcpd.1*

%files client
%doc README COPYING ChangeLog
%{_bindir}/dns2tcpc
%{_unitdir}/dns2tcpc.service
%config(noreplace) %{_sysconfdir}/dns2tcpc.conf
%{_mandir}/man1/dns2tcpc.1*
