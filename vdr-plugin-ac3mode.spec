
%define plugin	ac3mode
%define name	vdr-plugin-%plugin
%define version	0.1
%define rel	19

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


