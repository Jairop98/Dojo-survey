from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
# our index route will handle rendering our form
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process',methods=['POST'])
def process():
    # Here we add four properties to session to store the name, location, language and comments
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/results')
    # Never render a template on a POST request.
    # # Instead we will redirect to our index route.

@app.route('/results')
def results():
    return render_template('results.html')



if __name__=="__main__":
    app.run(debug=True)