Summary:	PostgreSQL driver and tools library
Name:		python3-py-postgresql
Version:	1.1.0
Release:	9
License:	BSD
Group:		Development/Languages/Python
Source0:	https://github.com/python-postgres/fe/archive/v%{version}.tar.gz
# Source0-md5:	8efe810a4abbbbe1c25b4fcef29421fa
URL:		http://python.projects.postgresql.org/
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq  python3-modules
Requires:	python3-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
py-postgresql is a set of Python modules providing interfaces to
various parts of PostgreSQL. Notably, it provides a pure-Python driver
+ C optimizations for querying a PostgreSQL database.

%prep
%setup -q -n fe-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py3_sitedir}/postgresql
%{py3_sitedir}/*.egg-info
