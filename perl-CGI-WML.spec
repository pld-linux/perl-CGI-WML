#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	CGI
%define		pnam	WML
%include	/usr/lib/rpm/macros.perl
Summary:	CGI::WML - subclass LDS's "CGI.pm" for WML output and WML methods
Summary(pl.UTF-8):	CGI::WML - podklasa CGI.pm do wyjścia i metod WML
Name:		perl-CGI-WML
Version:	0.09
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	091abe6a07f1b795d63437e78bf68efd
Patch0:		%{name}-noninteractive.patch
URL:		http://search.cpan.org/dist/CGI-WML/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{with tests}
BuildRequires:	perl-CGI
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTML-TableExtract
BuildRequires:	perl-XML-Parser
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::WML provides WML output and WML methods for CGI programming. The
purpose of the module is to retain the familiar CGI.pm way of
programming to enable experienced CGI programmers to use their
existing skills when creating WAP applications.

%description -l pl.UTF-8
CGI::WML udostępnia wyjście WML i metody WML do programowania CGI.
Celem tego modułu jest zachowanie znanej metody programowania CGI, aby
umożliwić doświadczonym programistom CGI używanie swoich umiejętności
przy tworzeniu aplikacji WAP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/CGI/WML/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
