Name:		dns2tcp
Version:	0.5.2
Release:	4
Summary:	Tunnel TCP over DNS
Group:		Networking/Other
License:	GPLv2+
URL:		http://www.hsc.fr/ressources/outils/dns2tcp/
Source0:	http://www.hsc.fr/ressources/outils/dns2tcp/download/%{name}-%{version}.tar.gz
Source1: 	dns2tcpd.service
Source2: 	dns2tcpd.conf
Source3: 	dns2tcpc.service
Source4: 	dns2tcpc.conf
BuildRequires:  openssl-devel
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
Dns2tcp is a tool for relaying TCP connections over DNS. There is no
authentications nor encryption mecanisms : DNS encapsulation must be
considered as an unsecure and anonymous transport layer. Ressources should
be public external services like ssh, ssltunnel ... 

%package	client
Summary:	Client for dns2tcp (Tunnel TCP over DNS)
Group:		Networking/Other
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description	client
Dns2tcp is a tool for relaying TCP connections over DNS. There is no
authentications nor encryption mecanisms : DNS encapsulation must be
considered as an unsecure and anonymous transport layer. Ressources should
be public external services like ssh, ssltunnel ...

This package contains the client part.

%package	server
Summary:	dns2tcp server (Tunnel TCP over DNS)
Group:		Networking/Other
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

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

%makeinstall

install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/dns2tcpd.service
install -D -m 0755 %{SOURCE2} %{buildroot}%{_sysconfdir}/dns2tcpd.conf
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/dns2tcpc.service
install -D -m 0755 %{SOURCE4} %{buildroot}%{_sysconfdir}/dns2tcpc.conf

%clean

%post server
%systemd_post dns2tcpd.service

%preun server
%systemd_preun dns2tcpd.service

%postun server
%systemd_postun_with_restart dns2tcpd.service

%post client
%systemd_post dns2tcpc.service

%preun client
%systemd_preun dns2tcpc.service

%postun client
%systemd_postun_with_restart dns2tcpc.service

%files server
%doc README COPYING ChangeLog
%{_bindir}/dns2tcpd
%{_unitdir}/dns2tcpd.service
%config(noreplace) %{_sysconfdir}/dns2tcpd.conf
%{_mandir}/man1/dns2tcpd.1.*

%files client
%doc README COPYING ChangeLog
%{_bindir}/dns2tcpc
%{_unitdir}/dns2tcpc.service
%config(noreplace) %{_sysconfdir}/dns2tcpc.conf
%{_mandir}/man1/dns2tcpc.1.*
