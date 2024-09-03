from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        password = request.form['password']
        if password == 'yourpassword':  # Replace 'yourpassword' with your desired password
            return redirect(url_for('welcome'))
        else:
            return "Incorrect password, please try again."
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    return "Welcome!"

if __name__ == '__main__':
    app.run()
