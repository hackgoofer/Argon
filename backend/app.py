from flask import Flask, request, jsonify
import base64
from flask_cors import CORS

from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

# Using small model, better results would be obtained with `medium` or `large`.
model = MusicGen.get_pretrained('small')
print('model loaded')
app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes
model.set_generation_params(
    use_sampling=True,
    top_k=250,
    duration=30
)
@app.route('/generate', methods=['GET'])
def generate():
    print('generate called')
    start = request.args.get('start', type=float)
    end = request.args.get('end', type=float)
    text = request.args.get('text', type=str)
    output = model.generate_unconditional(num_samples=1, progress=True)
    # convert from tensor to numpy to bytes 
    print(f'output shape: {output.shape}')
    # add wav file header
    for idx, one_wav in enumerate(output):
        audio_write(f'test', one_wav.cpu(), model.sample_rate)
    # load wav file, convert to base64
    with open(f'test.wav', 'rb') as f:
        audio_bytes = f.read()
    audio_base64 = base64.b64encode(audio_bytes).decode('ascii')
    return jsonify({'audio': audio_base64})

# Function to generate audio. This is a placeholder, fill it with your logic.
def generate_audio(start, end, text):
    # This function should return an audio buffer.
    pass

if __name__ == '__main__':
    app.run(debug=True, port=80)
