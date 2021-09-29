# A guide for writing hygienic code in Python

Writing organised code might not come across as an easy task for everyone. However, in practice, a programmer that can 
write clean and readable code is more valued than one who is gifted with mathematical ingenuity, as a piece of 
unreadable code is a piece of unusable code. This matters for both the collaborator working on the same codebase, and 
the exact author who originated that piece of code 6 months later. 

As a result, this calls for new languages and coding standards that strive to bring the act of coding closer and closer 
to writing an instruction manual, which often becomes a great subject of debate and contention, especially when it 
involves other concerns such as processing speed and programming paradigms.

This is a style guide written to serve as a basis for its author to negotiate coding standards with his collaborators in 
his own projects. Hence, this guide and these examples are mostly written for private purposes, and its author would 
welcome any suggestions for improvements and updates.

The contents of this guide is sorted into two categories by their significance, each with its own subrepository. The 
first one describes practices that have a profound impact on the utility of a codebase, and is treated by its author as 
a minimum required effort in his own coding projects. The second one is suggestive, and even at times, argumentative, 
subjective to the coders' personal preferences.

Brevity is valued in this guide. However, if the example is too comprehensive to be included in the README.md file, the 
relevant example will have its own python script or even its own subrepository. This guide mostly follows the syntax of 
Python 3.9, and is subjected to future updates.

## Table of contents
1. [Important practices that improve readability](A-strongly-recommended/README.md)
2. [Suggested practices that help with code maintenance](B-suggested/README.md)


## Author
Wai-Tsun Yeung (he/his/him)

##License
[Apache License Version 2.0](LICENSE)