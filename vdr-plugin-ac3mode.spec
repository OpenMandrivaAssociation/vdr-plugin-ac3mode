
%define plugin	ac3mode
%define name	vdr-plugin-%plugin
%define version	0.1
%define rel	21

Summary:	VDR plugin: Displays currently active AC3-Mode
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.vdr-wiki.de/wiki/index.php/Ac3mode-plugin
Source:		vdr-%plugin-%version.tar.bz2
Patch0:		ac3mode-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
If a channel broadcasts "Dolby Digital" (AC3) Sound, there is no information
about the number of channels (Dolby Stereo, 5.1 etc.) actually
available.
This plugin will display this information in a short hint text, whenever
the Dolby Digital mode is changed.

Additionally, a main menu entry is added, which will also display the
selected Dolby Digital type.
If no Dolby track is selected, "PCM Sound" will be displayed.

%prep
%setup -q -n %plugin
%patch0 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1-21mdv2010.0
+ Revision: 401089
- actually rebuild for new VDR

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1-20mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.1-19mdv2009.1
+ Revision: 359270
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.1-18mdv2009.0
+ Revision: 197887
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.1-17mdv2009.0
+ Revision: 197619
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.1-16mdv2008.1
+ Revision: 144998
- rebuild for new vdr

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.1-15mdv2008.1
+ Revision: 144962
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.1-14mdv2008.1
+ Revision: 103048
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.1-13mdv2008.0
+ Revision: 49958
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.1-12mdv2008.0
+ Revision: 42045
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.1-11mdv2008.0
+ Revision: 22801
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.1-9mdv2007.0
+ Revision: 90872
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.1-7mdv2007.1
+ Revision: 73933
- rebuild for new vdr
- Import vdr-plugin-ac3mode

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1-6mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.1-5mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1-4mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.1-3mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.1-2mdv2007.0
- rebuild for new vdr

* Sat Jun 10 2006 Anssi Hannula <anssi@mandriva.org> 0.1-1mdv2007.0
- initial Mandriva release

