from flask import Flask, render_template

app = Flask(__name__)



#### DICTIONARY

@app.route("/dictionary/<string:letter>") 
def dictionary(letter): 
    f=open('words.txt')
    word_list=f.read().splitlines()

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v', 
    'w', 'x','y', 'z']

    displayed_list = []

    for l in letters:
        displayed_letters = letter + l
        displayed_list.append(displayed_letters)

    n = 0 #number of words


    for w in word_list:
        if w.lower().startswith(letter.lower()):
            n += 1
    
    is_real_word = letter.upper() in word_list

    return render_template('template2.html', displayed_list = displayed_list, letter=letter, n=n, is_real_word = is_real_word)

@app.route("/dictionary") 
def home(): 

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v', 
    'w', 'x','y', 'z']


    return render_template('template1.html', letters=letters)

