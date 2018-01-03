from nate import * 

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/testimonies/')
def testimonies():
    return render_template('testimonies.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')




