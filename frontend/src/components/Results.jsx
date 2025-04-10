export default function Results({ analysis }) {
    return (
      <div className="mt-8 p-6 bg-gray-50 rounded-lg">
        <h2 className="text-2xl font-bold mb-4">Your Skin Report</h2>
        
        <div className="grid md:grid-cols-2 gap-8">
          <div>
            <h3 className="text-lg font-semibold mb-3">Detected Concerns</h3>
            <ul className="space-y-2">
              {analysis?.skin_issues?.map((issue, i) => (
                <li key={i} className="bg-white p-3 rounded shadow-sm">
                  {issue.label} - {Math.round(issue.score * 100)}% confidence
                </li>
              ))}
            </ul>
          </div>
  
          <div>
            <h3 className="text-lg font-semibold mb-3">Recommended Products</h3>
            <div className="bg-white p-4 rounded shadow-sm">
              {analysis?.recommendations?.split('\n').map((line, i) => (
                <p key={i} className="mb-2">{line}</p>
              ))}
            </div>
          </div>
        </div>
      </div>
    );
  }