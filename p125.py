from flask import Flask,jsonify, request
from Project125 import get_prediction

app = Flask(__name__)

@app.route("/predictdigit", methods=["POST"])
def predictdigit():
    image = request.files.get("digit")
    prediction = get_prediction(image)

    return jsonify({
         "prediction":prediction,
        
     }),200

if (__name__ == "__main__"):
    app.run(debug=True)     
  