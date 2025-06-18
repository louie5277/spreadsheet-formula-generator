import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [explanation, setExplanation] = useState(false);
  const [result, setResult] = useState('');

  const [loading, setLoading] = useState(false);

const handleSubmit = async () => {
  setLoading(true);         // Start loading
  setResult('');            // Clear previous result

  try {
    const res = await axios.post('http://localhost:5000/generate-formula', {
      prompt,
      explanation
    });
    setResult(res.data.result);
  } catch (error) {
    alert("Error connecting to backend.");
  } finally {
    setLoading(false);      // End loading
  }
};

  return (
    <div className="App">
      <h1>🧠 Spreadsheet Formula Generator</h1>
      <textarea
        rows="4"
        cols="60"
        placeholder="Describe your formula (e.g., sum column A where B > 10)"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <br />
      <label>
        <input
          type="checkbox"
          checked={explanation}
          onChange={(e) => setExplanation(e.target.checked)}
        />
        Include explanation
      </label>
      <br />
      <button onClick={handleSubmit}>Generate</button>
      {loading && (
        <div className="spinner">
          🔄 Generating...
        </div>
      )}

      {result && (
        <>
          <h3>Result:</h3>
          <pre>{result}</pre>
        </>
      )}

    </div>
  );
}

export default App;
