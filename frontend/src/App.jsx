import { useState } from 'react';
import ImageUploader from './components/ImageUploader';
import Results from './components/Results';
import { analyzeSkin } from './api';

export default function App() {
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalysis = async (image) => {
    setLoading(true);
    try {
      const analysis = await analyzeSkin(image);
      setResults(analysis);
    } catch (error) {
      console.error('Analysis failed:', error);
    }
    setLoading(false);
  };

  return (
    <div className="max-w-4xl mx-auto p-4">
      <h1 className="text-3xl font-bold text-center mb-8">SkinScan.AI</h1>
      <ImageUploader onAnalysis={handleAnalysis} />
      {loading && <p className="text-center mt-4">Analyzing your skin...</p>}
      {results && <Results analysis={results} />}
    </div>
  );
}