#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	WML
Summary:	CGI::WML - Subclass LDS's "CGI.pm" for WML output and WML methods
Summary(pl):	CGI::WML - podklasa CGI.pm do wyj¶cia i metod WML
Name:		perl-CGI-WML
Version:	0.05
Release:	0.2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-CGI
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTML-TableExtract
BuildRequires:	perl-XML-Parser
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::WML provides WML output and WML methods for CGI programming.
The purpose of the module is to retain the familiar CGI.pm way of
programming to enable experienced CGI programmers to use their
existing skills when creating WAP applications.

%description -l pl
CGI::WML udostêpnia wyj¶cie WML i metody WML do programowania CGI.
Celem tego modu³u jest zachowanie znanej metody programowania CGI, aby
umo¿liwiæ do¶wiadczonym programistom CGI u¿ywanie swoich umiejêtno¶ci
przy tworzeniu aplikacji WAP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
