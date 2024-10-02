from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Simulated database (stores volunteers in memory)
volunteers = []

# Serve the index.html file
@app.route('/')
def home():
    return render_template('index.html')

# Route to add a new volunteer
@app.route('/volunteers', methods=['POST'])
def add_volunteer():
    data = request.json
    name = data.get('name')
    skill = data.get('skill')

    if name and skill:
        volunteers.append({"name": name, "skill": skill})
        return jsonify({"message": "Volunteer added successfully!"}), 201
    else:
        return jsonify({"error": "Invalid data. Please provide both name and skill."}), 400

# Route to get all volunteers
@app.route('/volunteers', methods=['GET'])
def get_volunteers():
    return jsonify({"volunteers": volunteers})

# Run the app on the dynamically assigned port or port 5000
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
