from flask import Flask, render_template, request, jsonify
from imagescan import scanny

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # This serves your HTML page

@app.route('/run-function', methods=['POST'])
def run_function():
    data = request.json
    print("Button clicked with data:", data)  # Example: Log received data
    result = {"message": "Python function executed!"}
    return jsonify(result)  # Send a response back to the frontend

@app.route('/run-scanny', methods=['POST'])
def run_scanny():
    data = request.json  # Receive JSON data from frontend
    print("Button clicked with data:", data)

    result = scanny() 
    
    return jsonify({"plant_name": result})  


if __name__ == '__main__':
    app.run(debug=True)
