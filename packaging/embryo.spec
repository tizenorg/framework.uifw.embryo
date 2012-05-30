#sbs-git:slp/pkgs/e/embryo embryo 1.1.0+svn.68928slp2+build01 ff312ab0f1dd243c5f94e56b2e55f3c43b0cf40f
Name:       embryo
Summary:    A small virtual machine engine (in a library) and bytecode compiler
Version:    1.1.0+svn.69899slp2+build01
Release:    1
Group:      System/Libraries
License:    BSD
URL:        http://www.enlightenment.org/
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/embryo.manifest 
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: pkgconfig(eina)
Provides: embryo-bin


%description
Development files for libembryo0 Embryo is primarily a shared library that gives you an API to load
 and control interpreted programs compiled into an abstract machine
 bytecode that it understands.  This abstract (or virtual) machine is
 similar to a real machine with a CPU, but it is emulated in
 software.
 .
 This packages contains headers and static libraries for Embryo.



%package devel
Summary:    A small virtual machine engine and bytecode compile (devel)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
A small virtual machine engine (in a library) and bytecode compile (devel)

%prep
%setup -q


%build
cp %{SOURCE1001} .
export CFLAGS+=" -fvisibility=hidden -fPIC"
export LDFLAGS+=" -fvisibility=hidden -Wl,--hash-style=both -Wl,--as-needed"

%autogen --disable-static
%configure --disable-static
make %{?jobs:-j%jobs}

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest embryo.manifest
%defattr(-,root,root,-)
%{_libdir}/libembryo.so.*
%{_bindir}/embryo_cc
%{_datadir}/embryo/include/default.inc


%files devel
%manifest embryo.manifest
%defattr(-,root,root,-)
%{_includedir}/embryo-1/Embryo.h
%{_libdir}/libembryo.so
%{_libdir}/pkgconfig/*.pc
