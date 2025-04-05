from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the trained model (Email Spam Classifier)
model = pickle.load(open('Email-Spam-classifier.pkl', 'rb'))

# Load the vectorizer for preprocessing
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Initialize the Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the POST request
        data = request.json
        email_text = data['email_text']
        
        # Preprocess the input (e.g., transform using vectorizer)
        email_features = vectorizer.transform([email_text])
        
        # Predict using the model
        prediction = model.predict(email_features)
        
        # Return the result in JSON format
        result = {
            'email_text': email_text,
            'is_spam': bool(prediction[0])
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)