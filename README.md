# tb-py-py-compiler


# Inspiration 
- Austin Henley's Blog Article below [here](https://austinhenley.com/blog/challengingprojects.html).

# Notes from blog post
- First hurdle is lexing (tokenizing) input code.
- Then parse the code - check the structure of the input and produce a tree representation of the code
- ^ Recursive Descent Parsing Technique
- Semantically check the input 
* Check code makes sense
* Check type rules are being followed. 
- Generate Output
- Extending the project: 
* Simple 2D Graphics Functionality
* Optimization Passes
* Error Messages

# Resources 
So far I havel the below list of resources as outlined in Austin Henley's blog post re. making first compiler. I will add to this as I go if needed but I think he provides a pretty comprehensive list to get started with.

1. Concepts:
* [Lexical Analysis](https://en.wikipedia.org/wiki/Lexical_analysis)
* [Syntactic Analysis](https://en.wikipedia.org/wiki/Parsing)
* [Recursive Descent Parsing](https://en.wikipedia.orgwikiRecursive_descent_parser)
* [Recursive Descent Parsing](https://en.wikipedia.org/wiki/Recursive_descent_parser)
*[Abstract Syntax Tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree)
*[Semantic Analysis](https://en.wikipedia.org/wiki/Semantic_analysis_compilers)
*[Optimization Passes](https://en.wikipedia.org/wiki/Optimizing_compiler)
*[Code Generation](https://en.wikipedia.org/wiki/Code_generation_compiler)

2. To Read and Watch: 
* [A tutorial](https://austinhenley.com/blog/teenytinycompiler1.html)
* [Crafting Interpreters](https://www.craftinginterpreters.com/contents.html)
* [Compiler Building](https://compilers.iecc.com/crenshaw/)
* [Learn about Tiny BASIC](https://en.wikipedia.org/wiki/Tiny_BASIC)


# Notes 
up to page 2 - just done the checkToken/checkPeek functions for parser