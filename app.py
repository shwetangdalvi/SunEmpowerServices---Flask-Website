from flask import Flask, render_template, url_for

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# SME Loans Page
@app.route('/sme-loans')
def sme_loans():
    return render_template('sme-loans.html')

# Auto Loans Page
@app.route('/auto-loans')
def auto_loans():
    return render_template('auto-loans.html')

# Education Loans Page
@app.route('/education-loans')
def education_loans():
    return render_template('education-loans.html')

# Credit Cards Page
@app.route('/credit-cards')
def credit_cards():
    return render_template('credit-cards.html')

# Contact Us Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Sign In Page
@app.route('/signin')
def signin():
    return render_template('signin.html')

if __name__ == '__main__':
    app.run(debug=True)
