import { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState("");

  const searchMemory = async () => {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/search",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            text: query,
          }),
        }
      );

      const data = await response.json();

      if (data.results.length === 0) {
        setResult("Relevant data not found.");
      } else {
        setResult(data.response);
      }

    } catch (error) {
      setResult("Backend connection error.");
    }
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>AI Memory Search</h1>

      <input
        type="text"
        placeholder="Enter your query here"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{
          padding: "10px",
          width: "300px",
        }}
      />

      <br /><br />

      <button
        onClick={searchMemory}
        style={{
          padding: "10px 20px",
        }}
      >
        Search Memory
      </button>

      <br /><br />

      <h3>{result}</h3>
    </div>
  );
}

export default App;