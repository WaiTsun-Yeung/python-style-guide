# A-1. <a name="top"/>How to write a good README.md file</a>

[[home]](/README.md) > [[A-strongly-recommended]](/A-strongly-recommended/README.md)

The primary purpose of a README.md is to instruct _usage_ of the repository from download to deployment, assuming 
only minimal user understanding of package distribution systems. A README.md document is also important for asserting 
the legal rights of the contributors and the users, which all users of the repository are taken to have implicitly 
agreed with the legal terms posted by its contributors.

The folder [README-example](README-example/README.md) contains a sample README document for a hello world script.

## Table of Contents
- [Resources](#resources) 
- [Structure](#structure)
  1. [Name & Description](#description)
  2. [Installation](#installation)
  3. [Usage](#usage)

## <a name="resources"/>Resources</a>
Given the importance of a good README.md file, there are ample online resources on how to write one. To name a few 
examples:

- [makeareadme.com](https://www.makeareadme.com/) describes a comprehensive outline on what can 
  be included in a README.md file, complete with an instructive template and renderer. This is especially useful for 
  coders without convenient means to preview their own README.md file.
- [GitHub Docs - Basic writing and formatting syntax](
  https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
  and [GitHub Guides - Mastering Markdown](https://guides.github.com/features/mastering-markdown/) are GitHub's guides
  to the formatting syntax of README.md files. Special attention should be paid to [GitHub-flavoured markdown 
  specifications](https://github.github.com/gfm/#what-is-github-flavored-markdown-), for GitHub is the most popular 
  platform that hosts and displays README.md documents.
- [Markdown Guide - Basic Syntax](https://www.markdownguide.org/basic-syntax/) is a compendious syntax guide for vanilla 
  Markdown documents, which also applies for GitHub-rendered README.md files. Note that image rendering and HTML syntax 
  are also supported, which is useful when a more elaborate README.md file needs to be made.

[[^top]](#top)

## <a name="structure"/>Structure</a>
As there are countless types of coding projects, there is not a standard format for a README.md document. However, for a
repository to be usable for others, the README.md document should have the minimum of following sections:

[[^top]](#top)

### <a name="description"/>I. Name & Description</a>
Written at the top part of a README.md document, this tells the potential user the function of the repository. 

If it is a public repository, this is also the place to advertise it well, and would be best to include the _context_ of 
where the repository could be used, and any _features_ the authors would want to highlight. For codes where speed and 
accuracy are important differentiating factors, this is also where the performance evaluation with popular _benchmarks_ 
should be given.

[[^top]](#top)

### <a name="installation"/>II. Installation</a>
This is a step-by-step guide where if the user follows through, they should be able to use the repository according to
the instructions at the [Usage](#usage) section.

Each programming language has its own package distribution systems. As far as only Python code is concerned, the user
would need to set up a Python environment, with the necessary Python package dependencies to run the script. Advanced 
users might also care about packaging the repository itself for easier access from bigger projects.

Since Python is an interpreted language, it is relatively platform-dependent. Still, if the repository is known to run
only on certain operating systems and computer architectures, those should be stated at the outset. If there are any
package dependencies that could not be simply installed by a `pip install <package-name>` or `conda install 
<package-name>` command, those should also be highlighted at the beginning of the installation section. These packages
typically comprised of mostly system- & architecture-dependent low level routines, like [OpenBLAS](
https://www.openblas.net/), [CUDA toolkit](https://developer.nvidia.com/cuda-toolkit), and deep-learning frameworks such 
as [PyTorch](https://pytorch.org/) and [TensorFlow](https://www.tensorflow.org/).

There are several ways to build a python environment. Sample hello world scripts are provided in [Installation Guide](
installation-guide):

#### Package and Environment Management systems
Python has 2 major package distribution systems: pip and conda.



[[^top]](#top)

### <a name="usage"/>III. Usage</a>

[[^top]](#top)