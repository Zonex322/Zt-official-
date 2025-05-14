from flask import Flask, jsonify
from flask_cors import CORS
import random
from datetime import datetime
import pytz

app = Flask(__name__)
CORS(app)
pairs = ["USDINR_OTC", "USDPKR_OTC", "EURUSD", "BTCUSD", "ETHUSD", "USDZAR", "AUDCAD", "EURCAD", "USDCAD", "USDJPY"]

@app.route("/api/signal", methods=["GET"])
def get_signal():
    pair = random.choice(pairs)
    direction = random.choice(["CALL", "PUT"])
    time = datetime.now(pytz.timezone("Asia/Karachi")).strftime("%H:%M")
    signal = f"{time} - {pair} - {direction}"
    return {"signal": signal}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
