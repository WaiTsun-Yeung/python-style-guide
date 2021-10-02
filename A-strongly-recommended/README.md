# A. <a name="top"/>Important practices that improve readability</a>

[[home]](/README.md)

These are practices that would make a profound impact on the utility of a codebase, and are suggested to be followed in 
all scenarios possible.


## Table of Contents
1. [README.md](#readme)  

## <a name="readme"/>1. [README.md](1-README/README.md)</a>

A README.md is a markdown document that is usually present in any codebase or repository, and occasionally in 
sub-repositories as well. Its purpose is to instruct _usage_ of the repository from download to deployment, assuming 
only minimal user understanding of package distribution systems. GitHub itself has provided extensive support for 
generating and rendering README.md files.

A good README.md file should have a minimum of the following information:

- The [description / purpose](1-README/README.md/#description) of the repository
- [Method of Installation](1-README/README.md/#installation), to name some common examples:
    - [requirements.txt](1-README/installation-guide/environment/pip-requirements/README.md)
    - [environment.yml](1-README/installation-guide/environment/conda-environment/README.md)
    - [setup.py](1-README/installation-guide/build-package/setup-py/README.md)
    - [make](1-README/installation-guide/build-package/make/README.md)
    - [Usage](1-README/README.md#usage)
    - [docker image](1-README/installation-guide/docker/README.md)
    - Clear instructions for users to run the code without need for extensive knowledge of the programming language or 
      experience in relevant development projects. All necessary and optional arguments that would be called by the user 
        should be clearly defined. 
    - If the codebase is an API, all public classes and functions should be well-described and provided with clear 
      examples. 
    - If this section is too long, the author should inline the smallest example of usage and provide links to documents 
      describing more sophisticated examples.
- License / Copyright
- Support / Authors and Acknowledgements

The following websites would serve as a nice introduction to how to write a good README.md file.

- [makeareadme.com](https://www.makeareadme.com/)
- [GitHub Docs - Basic writing and formatting syntax](
  https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [GitHub Guides - Mastering Markdown](https://guides.github.com/features/mastering-markdown/)

Click [here](1-README/README.md) for more detailed specifications of a good README.md file.

[[^top]](#top)