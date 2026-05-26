from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from deep_translator import GoogleTranslator

app = Flask(__name__)
CORS(app)  # Allows your standalone desktop window to talk to this backend

@app.route('/')
def home():
    # This fixes the 404 error if you visit http://127.0.0.1:5000 in your browser
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        text = data.get('text', '').strip()

        if not text:
            return jsonify({'error': 'No text provided'}), 400

        # Translates English to Odia
        translated_text = GoogleTranslator(source='en', target='or').translate(text)
        
        return jsonify({
            'original': text,
            'translated': translated_text
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)