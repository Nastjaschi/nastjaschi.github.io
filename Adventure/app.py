from flask import Flask, render_template, url_for

app = Flask(__name__)
#url( "{{ url_for('static', picture_url )}}");

@app.route("/")
def start():
    title = "The Big Trip"
    
    text = """Imagine, you've just graduated and decided to take a gap year. How would you prefer to spend your time?"""

    choices = [
        ('france',"Visit romantic France"),
        ('egypt',"Book a trip to hot and sunny Egypt")
    ]

    return render_template('adventure.html', title="The big trip", text=text, choices=choices, font_color="rgb(11, 11, 100)", picture_url="travel.jpg")
#left is the name of the item from the template


@app.route("/france")
def france():
    title = "You've arrived to beautiful France..."
    
    text = """People are drawn to France for the exquisite cuisine, culture, pure beauty of the country 
    and, ultimately, the way they feel when there. 
    There is a certain romance to France. The days went by in a flash."""

    choices = [
        ('home',"It's time to go home!"),
        ('egypt',"I don't think I liked my stay in France that much. Maybe Egypt is a better destination? ")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices, font_color="rgb(46,26,71)", picture_url="france.jpg")

@app.route("/egypt")
def egypt():
    title = "Welcome to Egypt!"
    
    text = """Egypt is famous for the Pyramids, Sahara Desert, and Nile River. It's known for its ruins, historical places, and sites of world wonders. 
    It is also famous for its mesmerizing beaches, coral reefs, and sea cruises.
    Egyptians are also known for their hospitality and generosity. You can enjoy the country's 
    oriental Arabic culture with its belly dancers and hookahs in Cairo and beyond."""

    choices = [
        ('home',"It's time to go home!"),
        ('france', "How much would cost a ticket from Cairo to Paris? I'm not ready to go home yet.")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices, font_color="rgb(221,50,36)", picture_url="egypt.jpg")



@app.route("/home")
def home():
    title = "Home, sweet home!"
    
    text = """You've had a nice rest and experienced so many adventures! Now you are ready to go to college 
    and bring your 'A' game!"""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices, font_color="rgb(199,36,177)", picture_url="home.jpg")
