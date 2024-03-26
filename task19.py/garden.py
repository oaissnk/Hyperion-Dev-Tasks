#garden path sentences
gardenPathSentences = [
 "The man whistling tunes pianos beautifully.",
 "The complex houses married and single soldiers and their families.",
 "Mary gave the child a Band-Aid.",
 "That Jill is never here hurts.", 
 "The cotton clothing is made of cotton that grows in Mississippi."
]


import spacy
nlp = spacy.load("en_core_web_sm")

for sentence in gardenPathSentences:
    doc = nlp(sentence)
    for ent in doc.ents:
        print(ent.text, ent.label_)
    for ent in doc.ents:
        print(f"Entity: {ent.text}, Label: {ent.label_}, Explanation: {spacy.explain(ent.label_)}")
    print()

#Based on the output, "Mary" and "Jill" are categorised as "PERSON", and "Mississippi" is categorised as "GPE"
    
'''Mary PERSON
Entity: Mary, Label: PERSON, Explanation: People, including fictional

Jill PERSON
Entity: Jill, Label: PERSON, Explanation: People, including fictional

Mississippi GPE
Entity: Mississippi, Label: GPE, Explanation: Countries, cities, states

All three of the above are correctly categorised as PERSON and GPE, respectively.

'''
