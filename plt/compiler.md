### The Compilation Process
- [Lexical analysis (tokenizing)](lexical-analysis)
- [Syntax analysis (parsing)]()
- [Type checking]()
- [Code generation]()

### Requirements
- Invalid Program must be rejected
- Valid Program must not be rejected
- Errors should be reported in source language
- Position of error should be reported
- What would have happened due to error should be reported
- Translated Program should be small and fast
- In Source language, Entire standard should be implemented
- Any restrictions or limits on source language should be well and clearly documented.

### Describing Programming Language
- Describing using English is unsatisfactory due to possible omissions, contradictions, ambiguities, and vagueness. (How to solve it if our Programming language is English?)
- [BNF](http://en.wikipedia.org/wiki/Backus-Naur_form) can be used
- [EBNF](http://en.wikipedia.org/wiki/EBNF) should be used
- What does nltk or other nlt people are using?
- Even Chomsky Level 0 is inadequate for English
- Regular Grammars - lex,flex and JavaCC
- CFG - yacc, bison, and JavaCC
