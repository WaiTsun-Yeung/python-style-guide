# A-1-II. <a name="top"/>Installation Guide for Python Dependencies</a>
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

## <a name="management"/>1. Package and Environment Management systems</a>
Python has 2 major package distribution systems: pip and conda. A package distribution system distributes well-tested 
Python packages. Without them, users would often need to build the dependent packages from their source codes, which 
is a tedious and time-consuming process. 

Pip and conda fetch pre-built Python packages from the [Python Package Index](https://pypi.org/) by default, where most 
common Python packages are published to. Not all functional open-source projects are available on the Python Package 
Index, as not all of them are well-tested for bugs or have good dependencies management. Those projects would need to be
built from source. On the other hand, for packages that are available on the [Python Package Index](https://pypi.org/), 
some are only distributed in specific operating systems and computer architectures. This is because those packages are 
built with other compiled languages, mostly for the improvement of computational speed, a well-known weakness of the 
Python language. For those repositories that are not distributed only on certain operating systems and computer 
architectures, oftentimes they can still be built from its source. Hence, the user is always encouraged to check out the 
source code and attempt building from source if they cannot install the package through pip / conda.

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
[Python Package Index](https://pypi.org/), pip also enables installing through wheel files, vcs(incl. git), archive 
files, local directory paths and others, where instructions are listed [here](
https://packaging.python.org/tutorials/installing-packages/).

Note that the default Python version is Python 2, so if the Python project is to be 
developed in Python 3, the latest major release, the keyword pip needs to be replaced by pip3, e.g. `pip3 install 
<package-name>`. The documentation for pip commands can be found 
[here](https://pip.pypa.io/en/stable/), and a human-readable guide for packaging with pip can be found [here](
https://packaging.python.org/).

Aside from installation and uninstallation, other useful pip functionalities include:

- Listing installed packages

   There are two commands that list packages installed to the current python executable: `pip freeze`, which lists
   packages in the `<package-name>==<package-version>` format; and `pip list`, which does the same but in a two-column
   tabular format.
- Showing package information

   `pip show <package-name>` shows descriptive information about the package including the Name, Version, Summary, 
   Home-page, Author, Author-email, License, Location, Requires and Required-by.

#### <a name="requirements-txt"/>requirements.txt</a>

#### <a name="pip-virtual-environment"/>Virtual Environment</a>
There has been a myriad of pip environment managers developed by the Python community, a good comparison of them has
been provided by [@Filmm](https://stackoverflow.com/users/247696/flimm) in [this StackOverflow thread](
https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe).
The best pip environment manager would be [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) used 
with [virtualenv](https://virtualenv.pypa.io/en/latest/). [Virtualenv](https://virtualenv.pypa.io/en/latest/) addresses
the need of isolating Python environments well in common development scenarios, so much so that Python version >= 3.3 is 
shipped with [venv](https://docs.python.org/3/library/venv.html), a worse-performing subset of [virtualenv](
https://virtualenv.pypa.io/en/latest/). [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) 
provides a set of extension scripts so managing and switching between Python environment with [virtualenv](
https://virtualenv.pypa.io/en/latest/) becomes even easier.

A short example to using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

However, Python developers are recommended