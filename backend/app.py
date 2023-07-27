from flask import Flask, request, jsonify
import base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/generate', methods=['GET'])
def generate():
    start = request.args.get('start', type=float)
    end = request.args.get('end', type=float)
    text = request.args.get('text', type=str)

    # Here you would generate your audio buffer using the provided parameters.
    # For example:
    # audio_buffer = generate_audio(start, end, text)

    # For now, let's use a dummy audio_buffer:
    audio_buffer = b"Dummy audio buffer"

    # audio_base64 = base64.b64encode(audio_buffer).decode('utf-8')
    with open("audio.txt") as f:
        audio_base64 = f.read()
    # audio_base64 = 'data:audio/wav;base64,' + audio_base64
    return jsonify({'audio': audio_base64})

# Function to generate audio. This is a placeholder, fill it with your logic.
def generate_audio(start, end, text):
    # This function should return an audio buffer.
    pass

if __name__ == '__main__':
    app.run(debug=True)
