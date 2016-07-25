# Time - A natural language UI
This Repository, for now, will include all the Research work for the above project

### Brain
- Text to Text using processes based system
- Make simple processes like file manager, music player
- Checking for status/posts
- Try to implement everything a GUI/OS does

### Natural Language Generation
- Program should be able to reply in a fun, natural way

### Natural Language Understanding
- Understanding what user is trying to say
- Spelling Correction and lowercase but preserving the actual input because it might mean something
- Finding Alternate meaning(Synonyms, Homophones) of the words
- Its input will be a sentence with all the words separated by spaces
- Determining how to divide it into words, sentences and paragraphs[](#Making Out a sentence)
- Calculating its grammar
- Making out exact meaning of the words and checking if any input doesn't make sense
- Checking the sentences before the current one to give it more understanding of current one
- Using real world references and knowledge
- [Basic Points]( http://www.tutorialspoint.com/artificial_intelligence/artificial_intelligence_natural_language_processing.htm)
- [Basic Program](http://www.vikparuchuri.com/blog/natural-language-processing-tutorial/)

### Making Out a sentence
- Using Context Free Language
- Basically programming syntax of English Grammar
- Use to check if that sentence makes any sense
- http://www.cs.columbia.edu/~kathy/NLP/ClassSlides/Class7-Parsing09/cfg-parsing.pdf, page 7
#### CFG RULE
- S → NP VP
- VP → V NP
- NP → Det N | Adj NP
- N → boy | girl
- V → sees | likes
- Adj → big | small
- DetP → a | the

### Spelling Correction
- http://norvig.com/spell-correct.html
- [spelling.py](./spelling/)

### Text To Speech
- Record every word in English language
- Get a text, search in above database and play it
- Learn about Natural Language Processing and implement it here
- Make logic for searching for sentences

### Speech To Text
- Record every word in different styles
- On recording, check for the sound which has high volume
- Get the audio snippet from the above recording
- Search for it in the database
- Use English grammar/ Natural Language Processing to optimize the search
- Make a Feedback system where if the conversion is wrong, it corrects itself for later times

### Artificial Intelligence
- Research needed

### GUI
- Make a smart GUI with above concept
- This will also mean making your own OS (maybe on top of linux kernel)

### Personal Assistant bot
- VTOP
