#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	JSON
%define	pnam	Tiny
Summary:	JSON::Tiny - minimal JSON with no dependencies
Summary(pl.UTF-8):	JSON::Tiny - minimalny JSON bez zależności
Name:		perl-JSON-Tiny
Version:	0.58
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/JSON/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aa006882222e17a94295b3a655aab91b
URL:		https://metacpan.org/release/JSON-Tiny
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Exporter) >= 5.59
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lightweight, fast, pure-Perl JSON in a stand-alone module with only
core dependencies.

%description -l pl.UTF-8
Lekka, szybka, czysto perlowa biblioteka JSON w samodzielnym module
bez zależności spoza podstawowego Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/JSON/Tiny.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/JSON/Tiny.pm
%{_mandir}/man3/JSON::Tiny.3pm*
