from flask import Flask, render_template, url_for

app = Flask(__name__)



@app.route("/fizzbuzz/<int:count_to>") 
def fizzbuzz(count_to): #we're passing the variable from above into the function
    l=[]
    for n in range(1,count_to + 1) :
        if n % 3 == 0 and n % 5 == 0:
            l.append("FizzBuzz")    
        elif n % 3 == 0:
            l.append("Fizz")
        elif n % 5 == 0:
            l.append("Buzz")
        else:    
            l.append(n)

    return render_template('main.html', last_number=count_to, numbers=l)

