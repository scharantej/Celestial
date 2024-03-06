
# Import necessary modules
from flask import Flask, render_template, request, jsonify
import smart_reply
import music_suggestion

# Create a Flask app
app = Flask(__name__)

# Define the main route
@app.route('/', methods=['GET'])
def index():
    """Render the main HTML page."""
    return render_template('index.html')

# Define the route for smart reply generation
@app.route('/smart_reply', methods=['POST'])
def generate_smart_reply():
    """Generate a smart reply to the user's message."""
    message = request.json['message']
    reply = smart_reply.generate_reply(message)
    return jsonify({'reply': reply})

# Define the route for music suggestion
@app.route('/music_suggestion', methods=['POST'])
def suggest_music():
    """Suggest music based on the user's message."""
    message = request.json['message']
    songs = music_suggestion.suggest_songs(message)
    return jsonify({'songs': songs})

# Run the app
if __name__ == '__main__':
    app.run()
