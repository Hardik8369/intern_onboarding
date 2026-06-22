import { useState, useEffect } from "react";
import EntryForm from "./EntryForm";

const API_URL = "http://localhost:5001/api/entries";

function Guestbook() {
  const [entries, setEntries] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchEntries = async () => {
    try {
      const res = await fetch(API_URL);
      const data = await res.json();
      setEntries(data);
    } catch (err) {
      setError("Failed to load entries.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchEntries();
  }, []);

  const handleSubmit = async (name, message) => {
    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, message }),
      });
      if (res.ok) fetchEntries();
    } catch (err) {
      setError("Failed to submit entry.");
    }
  };

  if (loading) return <p>Loading...</p>;
  if (error) return <p style={{color: "red"}}>{error}</p>;

  return (
    <div>
      <h1>📖 Guestbook</h1>
      {entries.length === 0 ? (
        <p>No entries yet. Be the first to sign!</p>
      ) : (
        entries.map((entry) => (
          <div key={entry.id} style={{
            background: "#f9f9f9",
            padding: "10px",
            margin: "10px 0",
            borderLeft: "4px solid #4CAF50",
            borderRadius: "4px"
          }}>
            <strong>{entry.name}</strong>
            <span style={{color: "#888", marginLeft: "10px", fontSize: "0.85em"}}>{entry.time}</span>
            <p>{entry.message}</p>
          </div>
        ))
      )}
      <EntryForm onSubmit={handleSubmit} />
    </div>
  );
}

export default Guestbook;
