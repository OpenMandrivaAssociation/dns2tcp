Name:		dns2tcp
Version:	0.5.2
Release:	2
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
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun server
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable dns2tcpd.service > /dev/null 2>&1 || :
    /bin/systemctl stop dns2tcpd.service > /dev/null 2>&1 || :
fi

%postun server
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart dns2tcpd.service >/dev/null 2>&1 || :
fi


%post client
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun client
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable dns2tcpc.service > /dev/null 2>&1 || :
    /bin/systemctl stop dns2tcpc.service > /dev/null 2>&1 || :
fi

%postun client
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart dns2tcpc.service >/dev/null 2>&1 || :
fi

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
