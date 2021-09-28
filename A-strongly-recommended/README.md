# A. Important practices that improve readability

[[^main page]](/README.md)

These are practices that would make a profound impact on the utility of a codebase, and are suggested to be followed in 
all scenarios possible.


##### <a name="table_of_contents"/>Table of Contents</a>
1. [README.md](#readme)  

<a name="readme"/></a>
## 1. README.md

A README.md is a markdown document that is usually present in any codebase or repository, and occasionally in sub-repositories as well in collaborating projects. GitHub itself has provided extensive support for generating and rendering README.md files.

A good README.md file should have a minimum of the following information:

- The description/purpose of the repository
- Method of Installation, to name some common examples:
    - requirements.txt
    - docker image
    - setup.py
    - cmake / make
- Usage
    - including clear definitions of parameters. 
    - If the codebase is an API, all public classes and functions should be well-described and provided with clear examples. 
    - If this section is too long, the author should inline the smallest example of usage and provide links to documents describing more sophisticated examples.
- License / Copyright
- Support / Authors and Acknowledgements

The following websites would serve as a nice introduction to how to write a good README.md file.

- [Template and structure - makeareadme.com](https://www.makeareadme.com/)
- [GitHub Docs - Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [GitHub Guides - Mastering Markdown](https://guides.github.com/features/mastering-markdown/)