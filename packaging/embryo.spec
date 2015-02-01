Name:       embryo
Summary:    A small virtual machine engine (in a library) and bytecode compiler
Version:    1.6.0+svn.76491slp2+build07
Release:    1
Group:      System/Libraries
License:    BSD 2-Clause
URL:        http://www.enlightenment.org/
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: pkgconfig(eina)


%description
Development files for libembryo0 Embryo is primarily a shared library that gives you an API to load
 and control interpreted programs compiled into an abstract machine
 bytecode that it understands.  This abstract (or virtual) machine is
 similar to a real machine with a CPU, but it is emulated in
 software.
 This packages contains headers and static libraries for Embryo.


%package devel
Summary:    A small virtual machine engine and bytecode compile (devel)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}


%description devel
A small virtual machine engine (in a library) and bytecode compile (devel)


%package tools
Summary:    A small virtual machine engine and bytecode compile (tools)
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}
Provides:   %{name}-bin
Obsoletes:  %{name}-bin


%description tools
A small virtual machine engine (in a library) and bytecode compile (tools)


%prep
%setup -q


%build
export CFLAGS+=" -fvisibility=hidden -fPIC -Wall"
export LDFLAGS+=" -fvisibility=hidden -Wl,--hash-style=both -Wl,--as-needed"

%autogen --disable-static
make %{?jobs:-j%jobs}

%install
%make_install
mkdir -p %{buildroot}/%{_datadir}/license
cp %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/%{_datadir}/license/%{name}
cp %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/%{_datadir}/license/%{name}-tools

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libembryo.so.*
%{_datadir}/license/%{name}
%manifest %{name}.manifest


%files devel
%defattr(-,root,root,-)
%{_includedir}/embryo-1/Embryo.h
%{_libdir}/libembryo.so
%{_libdir}/pkgconfig/*.pc


%files tools
%defattr(-,root,root,-)
%{_bindir}/embryo_cc
%{_datadir}/license/%{name}-tools
%{_datadir}/embryo/include/default.inc
