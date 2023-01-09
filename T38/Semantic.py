import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#  This prints out a  value between 0 and 1.
#  According to spaCy the word cat is more similar to monkey than banana.
#  The model appears to give more weight where there are two animals vs if an animal can be associated with an object
#  e.g the value for cat - monkey = 0.592+ and the value for monkey - banana = 0.404+

word4 = nlp("john")
word5 = nlp("beer")

print(word4.similarity(word5))
print([ent.label_ for ent in word4.ents])

#  Using a persons name vs an object to be associated with a human provided a negative result.
#  When the capital letter is removed from the name it gives a positive letter.
#  running the .ent method and property label returns "PERSON" for both "John" and "john".

tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#  as expected comparing can to banana gave the same value as comparing banana to cat.


sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)



