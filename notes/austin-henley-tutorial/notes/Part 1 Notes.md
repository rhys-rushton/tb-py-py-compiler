# Austin Henly Tutorial on Making A Compiler
- Following along with this before I have a go and make my own.

# Part 1 Notes
* [Part 1 Link](https://austinhenley.com/blog/teenytinycompiler1.html)
- A compiler can be simplified into three parts
- Lexer/Parser/Emitter
- Lexer: given inputted source code it will break the code up into tokens. Similar to words/punctuation.
- Parser: makes sure the tokens are in order and allowed in the language we are compiling to. 
- Emitter: Emits the code that our language transaltes to (can be the same language) -> i.e. C code can be compiled by a c compiler. 


## Lexer Overview
- The first module of our compiler is called the lexer. Given a string of Teeny Tiny code, it will iterate character by character to do two things: decide where each token starts/stops and what type of token it is. If the lexer is unable to do this, then it will report an error for an invalid token.