from flask import Flask, request
from forecast import get_forecast
import json

app = Flask(__name__)

@app.route("/forecast/<base_date>/<base_time>")
def forecast(base_date, base_time):
    result = get_forecast(base_date, base_time)
    print(result)
    return json.dumps(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")