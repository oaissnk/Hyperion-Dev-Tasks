import spacy


nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana')

#Iterate over each token pair and print their similarity
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = [
    "where did my dog go",
    "Hello, there is my car",
    "I've lost my car in my car",
    "I'd like my boat back",
    "I will name my dog Diana"
]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - " + str(similarity))

# The reason why monkey has more similarities to the fruits is because monkeys are highly associated with eating fruits whereas cats are not
# When I ran the file with sm, it did not even process the similarities with the singular words as there are no vector words loaded. However, with the sentences. The scores were better as they were slightly less negative, but the trends were similar
    
word1 = nlp("mouse")
word2 = nlp("cow")
word3 = nlp("cheese")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('mouse cow cheese food')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))