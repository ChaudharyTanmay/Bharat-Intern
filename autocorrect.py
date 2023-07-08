from nltk.corpus import wordnet
from nltk.metrics.distance import edit_distance

def correct_word(word):
    suggestions = []
    
    if wordnet.synsets(word):
        return word
    
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            suggestions.append(lemma.name())
    
    if not suggestions:
        suggestions = wordnet.words()
    
    distances = [(edit_distance(word, suggestion), suggestion) for suggestion in suggestions]
    nearest_word = min(distances)[1]
    
    return nearest_word