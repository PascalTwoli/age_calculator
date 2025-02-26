from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from datetime import date
from dateutil.relativedelta import relativedelta
import os


app = Flask(__name__)
CORS(app) #, resources={r"/age_calculations": {"origins": "*"}}
# port = int(os.environ.get("PORT", 5000))
# app.run(host="0.0.0.0", port=port)

# Route to serve the html page
@app.route("/")
def home(): 
    return render_template("index.html")
    # return "API is working!"

# API to calculate age
@app.route("/age_calculations", methods=["POST"])
def age_calculations(): 
    try:
        # if request.method == "OPTIONS":
        #     return '', 204  # Handle preflight request
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
    # app.run(host="0.0.0.0", port=5000)