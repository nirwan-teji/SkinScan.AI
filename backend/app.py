from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import cv2
import numpy as np
from skin_analysis import analyze_skin
from recommender import generate_recommendations

app = Flask(__name__)
CORS(app)

def decode_image(base64_str):
    try:
        img_data = base64.b64decode(base64_str.split(',')[1])
        nparr = np.frombuffer(img_data, np.uint8)
        return cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    except Exception as e:
        raise ValueError(f"Image decoding failed: {str(e)}")

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        image_data = request.json.get('image')
        if not image_data:
            return jsonify({'error': 'No image provided'}), 400
            
        image = decode_image(image_data)
        skin_issues = analyze_skin(image)
        recommendations = generate_recommendations(skin_issues)
        
        return jsonify({
            'skin_issues': skin_issues,
            'recommendations': recommendations
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)