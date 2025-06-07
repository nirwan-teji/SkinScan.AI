
# SkinScan.AI – AI-Powered Skincare Assistant

**SkinScan.AI** is a full-stack intelligent skincare assistant that analyzes a user's facial image in real-time to detect skin concerns and provide personalized skincare recommendations using multimodal AI models.

---

## Key Features

- Real-time face analysis using MediaPipe FaceMesh to detect facial regions like the T-zone, cheeks, and forehead.
- Skin condition classification powered by a fine-tuned ResNet-50 model trained on dermatologically labeled datasets.
- AI-based personalized skincare product recommendation using Mistral-7B via Hugging Face API.
- Live camera preview and RGB normalization handled with OpenCV for high-quality input processing.
- RESTful backend built with Flask to ensure modularity and scalability.
- End-to-end multimodal AI pipeline: from image input to NLP-generated product suggestions.
- Optional frontend (planned) using React or static HTML/CSS for interactive user experience.
- Designed for real-time inference with high accuracy and low latency.

---

## Tech Stack

| Layer       | Technologies Used                                                              |
|-------------|---------------------------------------------------------------------------------|
| AI Models   | ResNet-50, Mistral-7B                                                           |
| ML Tools    | PyTorch, OpenCV, MediaPipe, Hugging Face Transformers                          |
| Backend     | Flask, Python                                                                   |
| Frontend    | HTML, CSS, JavaScript *(React planned)*                                        |
| API         | Hugging Face API, Local Flask API Endpoints                                     |
| Others      | NumPy, Pandas, Matplotlib (for testing and visualization)                       |

---

## Architecture Overview

```
User Image
   ↓
OpenCV Camera Capture & RGB Conversion
   ↓
MediaPipe FaceMesh – Facial Region Extraction
   ↓
ResNet-50 – Skin Issue Classification
   ↓
Mistral-7B (via Hugging Face API) – Product Recommendations
   ↓
Frontend UI / Console Output
```

---

## How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/nirwan-teji/SkinScan.AI.git
cd SkinScan.AI
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the Flask app**
```bash
python app.py
```

4. **Access locally**
Visit `http://127.0.0.1:5000/` in your browser.

---

## Future Enhancements

- Add authentication and user profiles.
- Track skin improvement over time with periodic scans.
- Mobile-first design using React Native.
- Integration with real skincare brands for personalized purchasing.

---

## License

This project is licensed under the MIT License.

---

## Maintainer

**Anubhav Nirwan**  
[GitHub: nirwan-teji](https://github.com/nirwan-teji)  
[LinkedIn](https://www.linkedin.com/in/anubhav-nirwan-7a89ab275/)
