# A-1-II. <a name="top"/>Installation Guide for Python Dependencies</a>

[[home]](/README.md) > [[A-Important practices]](/A-strongly-recommended/README.md) > [[1-README]](
/A-strongly-recommended/1-README/README.md)

Python has sophisticated package management systems for distributing pre-built Python packages with default 
configurations. Open-source developers are advised to package and publish their working repositories to those Python 
package management systems for a painless user access. Closed-source developers taking part in large project development 
are also recommended to package their subroutines locally for a better-containerised project organisation.

This guide introduces how to install package libraries with these package management systems, and how to build a package 
from scratch. Special attention will be paid to the containerisation of Python environments. Although this is not the
default mode of Python package installation, containerisation is an extra step that is crucial to the management of 
multiple Python projects.

## Table of Contents
1. [Package and Environment Management systems](#management)
   1. [Pip](#pip)
      - [requirements.txt](#requirements-txt)
      - [Virtual Environment](#pip-virtual-environment)
   2. [Conda](#conda)

## <a name="management"/>1. Package and Environment Management systems</a>
Python has 2 major package distribution systems: pip and conda. A package distribution system distributes well-tested 
Python packages. Without them, users would often need to build the dependent packages from their source codes, which 
is a tedious and time-consuming process. 

Pip and conda fetch pre-built Python packages from the [Python Package Index (PyPI)](https://pypi.org/) by default, 
where most common Python packages are published to. Not all functional open-source projects are available on the Python 
Package Index, as not all of them are well-tested for bugs or have good dependencies management. Those projects would 
need to be built from source. On the other hand, for packages that are available on the [Python Package Index](
https://pypi.org/), some are only distributed in specific operating systems and computer architectures. This is because 
those packages are built with other compiled languages, mostly for the improvement of computational speed, a well-known 
weakness of the Python language. For those repositories that are not distributed only on certain operating systems and 
computer architectures, oftentimes they can still be built from its source. Hence, the user is always encouraged to 
check out the source code and attempt building from source if they cannot install the package through pip / conda.

By default, Python packages are installed to the root Python executable. However, reconfiguration of those executables 
is especially difficult. For this reason, both pip and conda have utilities for creating project-specific virtual 
environments. By assigning each project its own Python executable, it mitigates the problem of package version conflicts 
over multiple unrelated coding projects. Package conflict is often a major source of headache in large project 
developments, and hence, it is recommended that a virtual environment should be used whenever possible.

[[^top]](#top)

### <a name="pip"/>I. Pip</a>
Pip is Python's native package management system, and is automatically shipped with newer versions of Python for Windows 
and macOS users. Pip allows common third-party packages to be installed with a simple command `pip install 
<package-name>`, and to be uninstalled similarly with `pip uninstall <package-name>`. Aside from the aforementioned 
[Python Package Index](https://pypi.org/), pip also enables installing directly with wheel files, vcs(incl. git), 
archive files, local directory paths and others, where instructions are listed [here](
https://packaging.python.org/tutorials/installing-packages/).

Note that the default Python version is Python 2, so if the Python project is to be 
developed in Python 3, the latest major release, the keyword pip needs to be replaced by pip3, e.g. `pip3 install 
<package-name>`. The documentation for pip commands can be found 
[here](https://pip.pypa.io/en/stable/), and a human-readable guide for packaging with pip can be found [here](
https://packaging.python.org/).

Aside from installation and uninstallation, other useful pip functionalities include:

- **Listing installed packages**

   There are two commands that list packages installed to the current python executable: `pip freeze`, which lists
   packages in the `<package-name>==<package-version>` format; and `pip list`, which does the same but in a two-column
   tabular format.
- **Showing package information**

   `pip show <package-name>` shows descriptive information about the package including the Name, Version, Summary, 
   Home-page, Author, Author-email, License, Location, Requires and Required-by.

[[^top]](#top)

#### <a name="requirements-txt"/>requirements.txt</a>
It is often convenient to list all package dependencies in one text file, then call `pip install` with the recursive 
option `-r` to install the listed packages recursively. The file is conventionally named as requirements.txt, so `pip 
install -r requirements.txt` is commonly seen in the installation guides for Python repositories.

The format of the requirements.txt file can be found [here](
https://pip.pypa.io/en/stable/reference/requirements-file-format/#requirements-file-format). As demonstrated in the 
previous hyperlink, fine version control is possible with pip installation. It is advised to retroactively test the 
completed repository against different versions of different package dependencies as to ascertain the range of 
dependencies' versions that can be installed by another user to run the repository. This is because the user is most
likely incorporating several Python packages in one project, each with their own compatible version ranges of different 
dependencies. Hence, the less stringent your dependencies' version requirements are, the less likely it will run into 
dependency conflicts, and the more likely it can be used in other projects. Consequently, it is ill-advised to pipe the
output of `pip freeze` directly into requirements.txt, i.e., `pip freeze > requirements.txt`. Even though the format of
`pip freeze` is entirely correct for the requirements.txt file, it fixes very specific versions of package dependencies,
rendering the repository unusable in many scenarios.

An example of installing with a requirements.txt file is provided [here](environment/pip-requirements/README.md).

[[^top]](#top)

#### <a name="pip-virtual-environment"/>Virtual Environment</a>
There has been a myriad of pip environment managers developed by the Python community, a good comparison of them has
been provided by [@Filmm](https://stackoverflow.com/users/247696/flimm) in [this StackOverflow thread](
https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe).
The best pip environment manager would be [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) used 
with [virtualenv](https://virtualenv.pypa.io/en/latest/). [Virtualenv](https://virtualenv.pypa.io/en/latest/) addresses
the need of isolating Python environments well in common development scenarios, so much so that Python version >= 3.3 is 
shipped with [venv](https://docs.python.org/3/library/venv.html), a worse-performing subset of [virtualenv](
https://virtualenv.pypa.io/en/latest/). [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) 
provides a set of extension scripts for the [virtualenv](https://virtualenv.pypa.io/en/latest/) package so managing and 
switching between Python environment becomes even easier.

However, conda outperforms all existing Python environment managers in terms of package management and 
user-friendliness, and is recommended in nearly all scenarios. Hence, more treatment will be given to environment 
management with conda in this guide.

[[^top]](#top)

### <a name="conda"/>II. Conda</a>
Unlike pip or Python that is created by community-oriented development, conda is created by Anaconda Inc., which now 
hosts both paid proprietary and free open-source services. Like pip, conda is an open-source package manager. However,
conda is rarely used by itself, and is often shipped in either Miniconda or Anaconda Individual Edition (henceforth 
abbreviated as 'Anaconda'), both created by Anaconda Inc. 

The difference between Miniconda and Anaconda is, Miniconda includes only the conda package manager, Python and base 
Python packages upon installation, whilst Anaconda adds about 200+ Python packages on top of that. Therefore, Miniconda 
is more lightweight, but installing packages would typically be longer for Miniconda users, vice versa for Anaconda. 
Anaconda also includes a graphical user interface, which might be a decent bonus for some developers.

There are several features of conda package management that are worth highlighting, especially when compared to pip's 
environment managers:

- **Default environment**

    Unlike Python which defaults its executable at the root system, Conda manages all its environments within the 
anaconda folder inside the user's home directory by default. Once the user starts up conda, a Python environment named 
'base' will be activated. Even though developers are still recommended to create a new environment and not to use the 
base environment for testing and development, managing packages in the conda base environment is still much safer than 
in the root Python environment.

- **Environment rollback**

    The reason why the base environment is safer is largely attributed to conda's `--revisions` feature. The history of
numbered changes in a conda environment can be returned with the command `conda list --revisions`, then the conda
environment can be rolled back to a specified timepoint by its revision number with the command `conda install 
--revision=REVNUM`, where REVNUM is the revision number. To make an example:

```bash
$ python --version
Python 3.9.7

# Calling conda list --revisions when the base environment has just been created.
$ conda list --revisions
2021-09-28 21:02:39  (rev 0)
    +ca-certificates-2021.7.5 (defaults/win-64)
    +certifi-2021.5.30 (defaults/win-64)
    +openssl-1.1.1l (defaults/win-64)
    +pip-21.2.4 (defaults/win-64)
    +python-3.9.7 (defaults/win-64)
    +setuptools-58.0.4 (defaults/win-64)
    +sqlite-3.36.0 (defaults/win-64)
    +tzdata-2021a (defaults/noarch)
    +vc-14.2 (defaults/win-64)
    +vs2015_runtime-14.27.29016 (defaults/win-64)
    +wheel-0.37.0 (defaults/noarch)
    +wincertstore-0.2 (defaults/win-64)

# Now installing numpy as an example:
$ conda install numpy
## Skipping over terminal output from installing numpy, call conda list --revisions again.
$ conda list --revisions
2021-09-28 21:02:39  (rev 0)
    +ca-certificates-2021.7.5 (defaults/win-64)
    +certifi-2021.5.30 (defaults/win-64)
    +openssl-1.1.1l (defaults/win-64)
    +pip-21.2.4 (defaults/win-64)
    +python-3.9.7 (defaults/win-64)
    +setuptools-58.0.4 (defaults/win-64)
    +sqlite-3.36.0 (defaults/win-64)
    +tzdata-2021a (defaults/noarch)
    +vc-14.2 (defaults/win-64)
    +vs2015_runtime-14.27.29016 (defaults/win-64)
    +wheel-0.37.0 (defaults/noarch)
    +wincertstore-0.2 (defaults/win-64)

2021-10-14 18:11:16  (rev 1)
     ca-certificates  {2021.7.5 (defaults/win-64) -> 2021.9.30 (defaults/win-64)}
     certifi  {2021.5.30 (defaults/win-64) -> 2021.10.8 (defaults/win-64)}
    +blas-1.0 (defaults/win-64)
    +intel-openmp-2021.3.0 (defaults/win-64)
    +mkl-2021.3.0 (defaults/win-64)
    +mkl-service-2.4.0 (defaults/win-64)
    +mkl_fft-1.3.0 (defaults/win-64)
    +mkl_random-1.2.2 (defaults/win-64)
    +numpy-1.21.2 (defaults/win-64)
    +numpy-base-1.21.2 (defaults/win-64)
    +six-1.16.0 (defaults/noarch)

# Now I regret installing numpy and wish to revert back to the vanilla conda environment (rev 0), so I call
$ conda install --rev 0
## A conda install/uninstsall terminal output will be returned about removing numpy, skipping over them. Calling conda 
# list --revisions again.
$ conda list --revisions
2021-09-28 21:02:39  (rev 0)
    +ca-certificates-2021.7.5 (defaults/win-64)
    +certifi-2021.5.30 (defaults/win-64)
    +openssl-1.1.1l (defaults/win-64)
    +pip-21.2.4 (defaults/win-64)
    +python-3.9.7 (defaults/win-64)
    +setuptools-58.0.4 (defaults/win-64)
    +sqlite-3.36.0 (defaults/win-64)
    +tzdata-2021a (defaults/noarch)
    +vc-14.2 (defaults/win-64)
    +vs2015_runtime-14.27.29016 (defaults/win-64)
    +wheel-0.37.0 (defaults/noarch)
    +wincertstore-0.2 (defaults/win-64)

2021-10-14 18:11:16  (rev 1)
     ca-certificates  {2021.7.5 (defaults/win-64) -> 2021.9.30 (defaults/win-64)}
     certifi  {2021.5.30 (defaults/win-64) -> 2021.10.8 (defaults/win-64)}
    +blas-1.0 (defaults/win-64)
    +intel-openmp-2021.3.0 (defaults/win-64)
    +mkl-2021.3.0 (defaults/win-64)
    +mkl-service-2.4.0 (defaults/win-64)
    +mkl_fft-1.3.0 (defaults/win-64)
    +mkl_random-1.2.2 (defaults/win-64)
    +numpy-1.21.2 (defaults/win-64)
    +numpy-base-1.21.2 (defaults/win-64)
    +six-1.16.0 (defaults/noarch)

2021-10-14 18:12:47  (rev 2)
     ca-certificates  {2021.9.30 (defaults/win-64) -> 2021.7.5 (defaults/win-64)}
     certifi  {2021.10.8 (defaults/win-64) -> 2021.5.30 (defaults/win-64)}
    -blas-1.0 (defaults/win-64)
    -intel-openmp-2021.3.0 (defaults/win-64)
    -mkl-2021.3.0 (defaults/win-64)
    -mkl-service-2.4.0 (defaults/win-64)
    -mkl_fft-1.3.0 (defaults/win-64)
    -mkl_random-1.2.2 (defaults/win-64)
    -numpy-1.21.2 (defaults/win-64)
    -numpy-base-1.21.2 (defaults/win-64)
    -six-1.16.0 (defaults/noarch)
# You will notice that rev 2 is the exact opposite of rev 1, this is because the environment has only rolled back by 1 
# change in history.
```

Creating, removing, renaming, cloning and switching between environments

Switching Python version

Package dependencies version management

Non-Python package support and exclusively binary packages

Different package repositories