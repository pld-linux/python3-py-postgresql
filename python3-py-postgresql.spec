Summary:	PostgreSQL driver and tools library
Name:		python3-py-postgresql
Version:	0.9.1
Release:	1
Group:		Development/Languages/Python
License:	BSD
Source0:	http://python.projects.postgresql.org/files/py-postgresql-%{version}.tar.gz
# Source0-md5:	c9239b83d5055058b993076f9c92fd6d
URL:		http://python.projects.postgresql.org/
BuildRequires:	python3-devel
%pyrequires_eq  python3-modules
Requires:	python3-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
py-postgresql is a set of Python modules providing interfaces to various parts
of PostgreSQL. Notably, it provides a pure-Python driver + C optimizations for
querying a PostgreSQL database.

%prep
%setup -q -n py-postgresql-%{version}

%build
python3 -- setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python3 -- setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py3_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{py3_sitedir}/postgresql
%{py3_sitedir}/*.egg-info
