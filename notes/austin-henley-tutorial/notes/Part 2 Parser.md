# Parser Notes 

- Parser is the component that makes sure the code follows the correct syntax
- You need to make rules for the parser to follow. These rules are the grammar of your parser.

- Creating a grammar: 

```program ::= {statement}```
- ^ There is a grammar rule named program that is made of 0 or more statements. 

A statement is show below: 
``` statement ::= "PRINT" (expression | string) nl```
- The statement rule here is defined as the PRINT keyword followed by either an expression or a string and then a newline. 
- Expression and new line are other grammar rules that we are referencing. 
- String is a type of token from the lexer.

The statement rule can be expanded so that there are multiple options: 
```statement ::= "PRINT" (expression | string) nl "LET" ident "=" expression nl```




