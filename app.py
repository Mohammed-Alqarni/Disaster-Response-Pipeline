from flask import Flask, render_template, request
import pickle

# Step 1: Initialize Flask App
app = Flask(__name__)

# Step 2: Load the Machine Learning Model
# Make sure the .pkl file is in the same directory as app.py
with open("classifier_model.pkl", "rb") as file:
    model = pickle.load(file)

# Step 3: Define Routes
# Home Page
@app.route("/")
def home():
    return render_template("index.html")  # Renders the homepage

# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():
    # Get the message from the form
    message = request.form["message"]
    
    # Make a prediction using the loaded model
    prediction = model.predict([message])[0]
    
    # Pass the message and prediction to the result template
    return render_template("result.html", message=message, prediction=prediction)

# Step 4: Run the App
if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for easier development
