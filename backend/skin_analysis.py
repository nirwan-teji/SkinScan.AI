from transformers import pipeline
import cv2

# Load free skin analysis model
skin_model = pipeline(
    "image-classification",
    model="dermatology/finetuned-skin-condition"
)

def analyze_skin(image):
    try:
        # Preprocess
        resized = cv2.resize(image, (224, 224))
        rgb_image = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        
        # Predict
        predictions = skin_model(rgb_image)
        
        # Format results
        return [{
            'label': pred['label'],
            'score': float(pred['score'])
        } for pred in predictions[:3]]  # Return top 3 results
        
    except Exception as e:
        raise RuntimeError(f"Skin analysis failed: {str(e)}")