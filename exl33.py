import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt" #variable
WORDS = [] #list

Phrases = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object): \n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object): \n\tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters",
    "*** = %%% ()":
        "Set *** to an instance of class %%%.",
    "***.*** (@@@)":
        "From *** get the function *** and call it with parameters self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."

} #dictionary

if len(sys.argv) == "2" and sys.argv[1] == "english":
    PHRASE_FIRST = True

else :
    PHRASE_FIRST = False
# if statement, logical

for word in urlopen(WORD_URL).readlines ():
    WORDS.append(word.strip())
# for-loop

def convert (snippet, phrase): #creating a function convert
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []
    #variables
    for i in range (0, snippet.count("@@@")):
        param_count = random.randint (1,3)
        param_names.append (','.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]
        for word in class_names:
            result = result.replace("%%%", word, 1)
        for word in other_names:
            result = result.replace("***", word, 1)
        for word in param_names:
            result = result.replace("@@@", word, 1)
        result.append(result)

    return results

try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert (snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            print question
            raw_input ("> ")
            print "ANSWER: %s\n\t" % answer

except EOFError:
    print "\nBye"
