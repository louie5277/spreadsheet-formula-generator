from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from ai_formula import generate_excel_formula
import os

app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")
CORS(app)  # Enables frontend requests from localhost:3000

@app.route('/generate-formula', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt')
    explanation = data.get('explanation', False)

    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    result = generate_excel_formula(prompt, explanation=explanation)
    return jsonify({'result': result})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
