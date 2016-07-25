
### Tokens
- Tokens are frequently defined by regular expressions, which are understood by a lexical analyzer such as lex. The lexical analyzer reads in a stream of lexemes and categorizes them into tokens. This is called "tokenizing." If the lexer finds an invalid token, it will report an error.
- Consider a text describing a calculation : "46 - number_of(cows);". The lexemes here might be: "46", "-", "number_of", "(", "cows", ")", and ";". The lexical analyzer will denote lexemes 4 and 6 as 'number' and - as character, and 'number_of ' as a separate token. Even the lexeme ';' in some languages (such as C) has some special meaning.

- Token doesn't need to be valid
