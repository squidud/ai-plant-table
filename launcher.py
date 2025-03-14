from flask import Flask, render_template, request, jsonify
from imagescan import scanny
from camerashit import capture
import time
from logger import log_action

app = Flask(__name__)

@app.route('/scan')
def scan():
    return render_template('scan.html')  # serves image scan page

@app.route('/')
def index():
    return render_template('index.html')  # serves main 'dashboard' page

@app.route('/logger')
def logger():
    return render_template('logger.html')  # serves main 'dashboard' page

@app.route('/cam')
def cam():
    return render_template('cam.html')  # serves main 'dashboard' page

@app.route('/run-function', methods=['POST'])
def run_function():
    data = request.json
    print("Button clicked with data:", data)  # Example: Log received data
    result = {"message": "Python function executed!"}
    return jsonify(result)  # Send a response back to the frontend

@app.route('/capture-pic', methods=['POST'])
def capture_pic():
    data = request.json
    capture() # calls capture function from camerashit to actually take picture
    print("Button clicked with data:", data)  # Example: Log received data
    result = {"message": "Picture saved!"}
    return jsonify(result)  # Send a response back to the frontend

@app.route('/run-scanny', methods=['POST'])
def run_scanny():
    data = request.json  # Receive JSON data from frontend
    print("Button clicked with data:", data)

    result = scanny() 
    
    return jsonify({"plant_name": result})  

#log bs below...

LOG_FILE = "static/log.txt" #file for activity log

with open(LOG_FILE, "w") as f:  
    f.write("")  # Clear the log
    log_action("Log initialized")

@app.route("/log", methods=["GET"])
def get_log():
    with open(LOG_FILE, "r") as f:
        log_data = f.readlines()
    return jsonify(log_data)


if __name__ == '__main__':
    app.run(debug=True)
