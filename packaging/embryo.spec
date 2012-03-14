Name:       embryo
Summary:    A small virtual machine engine (in a library) and bytecode compiler
Version:    1.1.0+svn.67705slp2
Release:    1.1
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
URL:        http://www.enlightenment.org/
Source0:    %{name}-%{version}.tar.gz
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

%autogen --disable-static
%configure --disable-static
make %{?jobs:-j%jobs}

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libembryo.so.*
/usr/bin/embryo_cc
/usr/share/embryo/include/default.inc


%files devel
%defattr(-,root,root,-)
%{_includedir}/embryo-1/Embryo.h
%{_libdir}/libembryo.so
%{_libdir}/pkgconfig/*.pc


