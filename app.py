from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from datetime import date
from dateutil.relativedelta import relativedelta

app = Flask(__name__)
CORS(app)

# Route to serve the html page
@app.route("/")
def home(): 
    return render_template("index.html")

# API to calculate age
@app.route("/age_calculations", methods=["POST"])
def age_calculations(): 
    try:
        data = request.json
        birth_year = int(data["year"])
        birth_month = int(data["month"])
        birth_day = int(data["day"])

        birth_date = date(birth_year, birth_month, birth_day)
        today = date.today()
        age =  relativedelta(today, birth_date)

        return jsonify({
            "years": age.years,
            "months": age.months,
            "days": age.days
        })
    
    except: 
        return jsonify ({
            "error": "Invalid input"
        }), 400
    
if __name__ == "__main__":
    app.run(debug=True)