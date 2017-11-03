### Approaches to Natural Language Processing
- Kind of technical use cases
- Or how to implement nlp internally in our system
1. Conduct Basic Text Processing
    - ??????
2. Categorize and tag words
    - Eg: happy, joy, insightful: positive words
    - sad, kill, war: negative words

    - Eg: table, bottle, fan: Non living
    - human, dog, plant: Living

    - Eg: Queen, actress, goddess: Female
    - King, God, actor: Male

    - Eg: Pizza, Burger, French Fries: Fast Food
    - Nuts, Cashew, Spinach: Healthy foods

    - Eg: Crown: Royal, king, attire, wear, head etc

3. Classifying Text
    - Classifying a news article as sports, politics, entertainment etc
    - Classify a novel as drama, sci fi, funny, adult etc
    - Classify a paragraph/sentence as aggresive, speech, information, knowledgable etc

4. Extract Information
    - find useful stock information from a business article
    - finding a launch date from a speech given by a person
    - finding language specs from documentation of a programming language

5. Analyse sentence structure
    - Using CFG to find whether sentence is ill formed or not

6. Build feature based structure
    - Using CFG determine which are nouns, pronouns etc

7. Analyse the meaning
    - Quantitive analysis
    - Find entities in a text and find how they are related
    - Eg: Angry Dog is barking on the old guy
        - guy is old
        - guy is being barked on
        - dog is doing the barking
        - mood of the dog is currently angry
        - Guy: {age > 60}
        - Dog: {mood: angry}
        - barks(Dog, Guy)

### Basic Terminology
