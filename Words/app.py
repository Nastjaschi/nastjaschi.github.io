from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    scrambled_words = ["JDORF", "BANDA", "GROMPAR"]

    return render_template('template1.html',  scrambled_words =  scrambled_words)

@app.route("/words/<string:word>") #word is a variable
def words(word): #we're passing the variable from above
    f=open('words.txt')
    word_list=f.read().splitlines()

    is_real_word = word.upper() in word_list #is it the same word from the function?

    anagrams = []

    for w in word_list:
        if sorted(word.upper()) == sorted(w):
            anagrams.append(w)


    return render_template('main.html', word=word, l=anagrams)