from flask import Flask, render_template, url_for, jsonify
from flask_ngrok import run_with_ngrok
import pandas as pd
import os



app = Flask(__name__)
app.secret_key = '2p5cWsuoo3fWNyXOcwBQQnQuGC9_3Lkk2VKoMRJY1v6iwXU8Y'
run_with_ngrok(app)

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

# About Us Page
@app.route('/about-us')
def about_us():
    return render_template('about-us.html')

@app.route('/feasibility-study')
def feasibility_study():
    import pandas as pd

    # Load the Excel file
    excel_path = 'static/files/Impact_Guild_Advisors_Feasibility_Study.xlsx'
    sheet_names = pd.ExcelFile(excel_path).sheet_names

    # Create a dictionary to store each sheet's data
    sheet_data = {}
    for sheet in sheet_names:
        df = pd.read_excel(excel_path, sheet_name=sheet)

        # Replace NaN values with empty strings
        df.fillna('', inplace=True)

        # Convert scientific notation to regular numbers
        df = df.applymap(lambda x: '{:.2f}'.format(x) if isinstance(x, (float, int)) and x != '' else x)

        # Convert the DataFrame to HTML
        sheet_data[sheet] = df.to_html(classes='table table-bordered table-striped', index=False, escape=False)

    return render_template('feasibility_study.html', sheet_data=sheet_data, sheet_names=sheet_names)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/dashboard-data')
def dashboard_data():
    return jsonify({
        "summary": {
            "totalLoanAmount": 7.2,  # $250B
            "totalBorrowers": 4000,
            "revenueGenerated": 1.2,  # $18M
            "totalBranches": 25
        },
        "charts": {
            "region": {
                "labels": ["Ontario/Quebec/Manitoba", "BC/Alberta/Saskatchewan", "Atlantic Provinces"],
                "values": [120, 80, 50]
            },
            "loanType": {
                "labels": ["SME Loans", "Education Loans", "Auto Loans", "Credit Cards"],
                "values": [90, 70, 60, 30]
            },
           "businessInsights": {
                "labels": ["Q1", "Q2", "Q3", "Q4"],  # Quarterly insights
                "values": [1.5, 1.7, 2, 2.3]  # Revenue in $M
            },
            "topRegions": {
                "labels": ["Ontario/Quebec/Manitoba", "BC/Alberta/Saskatchewan", "Atlantic Provinces"],
                "values": [5000, 2000, 1000]
            },
        },
        "table": [
            {"branchName": "Toronto", "loanType": "SME", "amount": "50M", "borrowers": 500, "region": "Ontario/Quebec/Manitoba"},
            {"branchName": "Vancouver", "loanType": "Education", "amount": "40M", "borrowers": 400, "region": "BC/Alberta/Saskatchewan"},
            {"branchName": "Halifax", "loanType": "Auto", "amount": "30M", "borrowers": 300, "region": "Atlantic Provinces"},
        ]
    })


# @app.route('/api/chart-data')
# def chart_data():
#     data = {
#         "region_data": {
#             "labels": ['North', 'South', 'East', 'West'],
#             "values": [12, 19, 3, 5],
#         },
#         "loan_type_data": {
#             "labels": ['Home Loans', 'Auto Loans', 'Education Loans', 'Personal Loans'],
#             "values": [30, 40, 20, 10],
#         },
#         "payment_frequency_data": {
#             "labels": ['Weekly', 'Bi-weekly', 'Monthly', 'Quarterly'],
#             "values": [100, 200, 300, 400],
#         },
#         "top_cities_data": {
#             "labels": ['City A', 'City B', 'City C', 'City D', 'City E'],
#             "values": [15, 10, 8, 6, 4],
#         }
#     }
#     return jsonify(data)

if __name__ == '__main__':
    app.run()
