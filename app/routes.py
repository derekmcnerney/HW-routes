from app import app

@app.route('/')
def home():
    return"Home Page"
    

@app.route('/about')
def about():
    return"Learn all about me. Sorry these routes are super easy i just dont know how to do it any other way yet  "


@app.route('/freakazoid')
def freakazoid():
    return"Page for freakazoid lovers"
