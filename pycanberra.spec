# import from rawhide


%global git_hash 65c3b3f

Name:          pycanberra
Summary:       A very basic (and incomplete) wrapper for libcanberra
License:       LGPLv2
Group:	       Development/Python
# There's no versioning upstream, it's all about the Git hash
Version:       0
Release:       0.6.git%{git_hash}

URL:           https://github.com/psykoyiko/pycanberra/

# There aren't any release yet, I'm creating a git snapshot:
#     $ git clone git://github.com/psykoyiko/pycanberra.git
#     $ cd pycanberra
#     $ GIT_HASH=$(git rev-parse --short HEAD)
#     $ git archive --prefix=pycanberra-$GIT_HASH/ --format=tar HEAD | xz > pycanberra-git.$GIT_HASH.tar.xz
Source0:       %{name}-git.%{git_hash}.tar.xz

# I submitted these patches upstream, but they haven't been accepted yet
#     https://github.com/psykoyiko/pycanberra/pull/2
# I'm pulling them in the package because other packages need pycanberra with
# Python 3 (e.g gnome-clocks)
Patch0:        0001-Do-not-use-the-exceptions-module.patch
Patch1:        0002-Ensure-all-strings-passed-to-libcanberra-are-byte-st.patch

BuildArch:     noarch

BuildRequires: python-devel
BuildRequires: python3-devel

# This will break at run time when libcanberra bumps its soname :(
Requires:      pkgconfig(libcanberra)

%description
A very basic (and incomplete) wrapper of libcanberra for Python 2.


%package -n python3-canberra
Summary:       A very basic (and incomplete) wrapper for libcanberra

%description -n python3-canberra
A very basic (and incomplete) wrapper of libcanberra for Python 3.


%prep
%setup -q -n pycanberra-%{git_hash}

%patch0 -p1
%patch1 -p1


%build
# Nothing to build


%install
install -d %{buildroot}%{python_sitelib}
install -p -m 0644 pycanberra.py %{buildroot}%{python_sitelib}

install -d %{buildroot}%{python3_sitelib}
install -p -m 0644 pycanberra.py %{buildroot}%{python3_sitelib}


%files
%doc COPYING README
%{python_sitelib}/pycanberra.py*

%files -n python3-canberra
%doc COPYING README
%{python3_sitelib}/pycanberra.py
%{python3_sitelib}/__pycache__/pycanberra.cpython-3?.py?



