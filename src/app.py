from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def get_value_details():
    return jsonify({
        "value": "example_values",
        "timestamp": datetime.datetime.now().isoformat(),
        "hostname": socket.gethostname(),
        "message": "This is a sample response from the Flask application.:)"
    })

@app.route('/api/v1/healthz')
def get_healthz():
    return jsonify({"status": "healthy"}),200

if __name__ == '__main__':
    app.run(host="0.0.0.0")