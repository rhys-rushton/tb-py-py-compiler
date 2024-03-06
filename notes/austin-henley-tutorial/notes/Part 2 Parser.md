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
```statement ::= "PRINT" (expression | string) nl | "LET" ident "=" expression nl```

- Statement rule above is defined as one of two options.
- PRINT or LET
- LET is a statement for assigning a value to a variable. 
- ident is a type of token from the lexer, which will act as a variable identifier. 
- expression is another grammar rule which is for math expressions.

```statement ::= "PRINT" (expression | string) nl
    | "LET" ident "=" expression nl
    | "IF" comparison "THEN" nl {statement} "ENDIF" nl```

- Now an if statement has been added to our grammar. 
- The thing to notice with this rule is that it is recursive. 
- The statement rule references the statement rule. 
- How this works in this example is that you call the statement rule in the if statement and then begin to work recursively. 
- The reason why this is powerful is because you haven't had to write any more rules in order to handle this. 
- Recursion enables concise and powerful grammars, as they can represent complex structures with just a few rules. 

- Entire grammar: 
```program ::= {statement}
statement ::= "PRINT" (expression | string) nl
    | "IF" comparison "THEN" nl {statement} "ENDIF" nl
    | "WHILE" comparison "REPEAT" nl {statement} "ENDWHILE" nl
    | "LABEL" ident nl
    | "GOTO" ident nl
    | "LET" ident "=" expression nl
    | "INPUT" ident nl
comparison ::= expression (("==" | "!=" | ">" | ">=" | "<" | "<=") expression)+
expression ::= term {( "-" | "+" ) term}
term ::= unary {( "/" | "*" ) unary}
unary ::= ["+" | "-"] primary
primary ::= number | ident
nl ::= '\n'+```

- The main thing to note is that each of the grammar rules will get a one to one
mapping in the Python code. 
- gramar -> code = 1:1 mapping.
- Notation: 
- {} zero or more
- [] zero or one 
- + one or more of whatever is left
- () just for grouping
- | logical or.
- words are references to other grammar rules or to tokens that have been defined in the lexer. 
- keywords/operators are quotes as strings of text.
- The parser object will control the lexer and request a new token as needed. So next, we have to implement the parser object.



