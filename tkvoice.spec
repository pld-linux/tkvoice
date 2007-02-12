Summary:	Frontend for vgetty and sendfax
Summary(pl.UTF-8):   Frontend do programów vgetty i sendfax
Name:		tkvoice
Version:	1.4b
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://tkvoice.netfirms.com/%{name}-%{version}.tar.gz
# Source0-md5:	5299f77cda2112b6cdb09567c10ee0bc
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-install.patch
URL:		http://tkvoice.netfirms.com/
Requires:	mgetty-voice
Requires:	wavplay
Requires:	tk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Frontend for vgetty and sendfax for X.

%description -l pl.UTF-8
Frontend dla X do programów vgetty i sendfax.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/tkvoice} \
	$RPM_BUILD_ROOT%{_datadir}/tkvoice/{TCL,image} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Network/Mail,%{_pixmapsdir}}

install tkvoice $RPM_BUILD_ROOT%{_bindir}
install tkvoice.xpm $RPM_BUILD_ROOT%{_datadir}/tkvoice
install TCL/* $RPM_BUILD_ROOT%{_datadir}/tkvoice/TCL
install image/* $RPM_BUILD_ROOT%{_datadir}/tkvoice/image
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS FAQ README TODO VERSION
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/TCL
%dir %{_datadir}/%{name}/image
%attr(755,root,root) %{_bindir}/tkvoice
%{_datadir}/%{name}/tkvoice.xpm
%{_datadir}/%{name}/TCL/*
%{_datadir}/%{name}/image/*
%{_pixmapsdir}/%{name}.png
%{_applnkdir}/Network/Mail/%{name}.desktop
