Name:           perl-Config-Simple
Version:        4.59
Release:        5.1%{?dist}
Summary:        Simple configuration file class 

Group:          Development/Libraries
#see README
License:        GPL+ or Artistic
URL:            http://search.cpan.org/~sherzodr/Config-Simple/
Source0:        http://cpan.org/authors/id/S/SH/SHERZODR/Config-Simple-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
# Correct for lots of packages, other common choices include eg. Module::Build
BuildRequires:  perl(ExtUtils::MakeMaker) perl(Test::Simple)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Simple configuration file class.

%prep
%setup -q -n Config-Simple-%{version}
chmod -x README Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*
chmod -x $RPM_BUILD_ROOT%{perl_vendorlib}/Config/Simple.pm


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Fri Jan 22 2010 Dennis Gregorovic <dgregor@redhat.com> - 4.59-5.1
- Rebuilt for RHEL 6
Related: rhbz#543948

* Thu Jul 02 2009 Jeff Fearn <jfearn@redhat.com> - 4.59-5
- bump for RHEL

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.59-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4.59-3
Rebuild for new perl

* Sun Dec 23 2007 Rafał Psota <rafalzaq@gmail.com> 4.59-2
- License tag fix
- Source0 fix
* Sat Dec 22 2007 Rafał Psota <rafalzaq@gmail.com> 4.59-1
- Initial release
