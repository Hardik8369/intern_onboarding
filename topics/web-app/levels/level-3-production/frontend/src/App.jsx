import { useState, useEffect, Component } from "react";

const API = "/api/entries";

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }
  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }
  render() {
    if (this.state.hasError) {
      return (
        <div className="error-box">
          <h2>Something went wrong.</h2>
          <p>{this.state.error?.message || "An unexpected error occurred."}</p>
          <button onClick={() => this.setState({ hasError: false, error: null })}>Try again</button>
        </div>
      );
    }
    return this.props.children;
  }
}

function GuestBook() {
  const [entries, setEntries] = useState([]);
  const [name, setName] = useState("");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [fetchError, setFetchError] = useState(null);
  const [formError, setFormError] = useState(null);
  const [success, setSuccess] = useState(false);

  useEffect(() => {
    setLoading(true);
    setFetchError(null);
    fetch(API)
      .then((res) => {
        if (!res.ok) throw new Error(`Server error: ${res.status}`);
        return res.json();
      })
      .then((data) => setEntries(data))
      .catch((err) => setFetchError(err.message))
      .finally(() => setLoading(false));
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setFormError(null);
    setSuccess(false);
    setSubmitting(true);
    try {
      const res = await fetch(API, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, message }),
      });
      const data = await res.json();
      if (!res.ok) {
        setFormError(data.error || "Something went wrong. Please try again.");
        return;
      }
      setEntries((prev) => [...prev, data]);
      setName("");
      setMessage("");
      setSuccess(true);
    } catch (err) {
      setFormError("Network error — could not reach the server.");
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="container">
      <h1>📖 Guestbook</h1>
      <form onSubmit={handleSubmit} className="form">
        <h2>Leave a message</h2>
        <label htmlFor="name">Name</label>
        <input id="name" type="text" value={name} onChange={(e) => setName(e.target.value)} placeholder="Your name" maxLength={100} disabled={submitting} />
        <label htmlFor="message">Message</label>
        <textarea id="message" value={message} onChange={(e) => setMessage(e.target.value)} placeholder="Your message" maxLength={500} rows={3} disabled={submitting} />
        {formError && <p className="error-text">⚠ {formError}</p>}
        {success && <p className="success-text">✓ Entry added!</p>}
        <button type="submit" disabled={submitting}>{submitting ? "Submitting…" : "Submit"}</button>
      </form>
      <section className="entries">
        <h2>Messages</h2>
        {loading && <p className="loading">Loading entries…</p>}
        {fetchError && <p className="error-text">⚠ Could not load entries: {fetchError}</p>}
        {!loading && !fetchError && entries.length === 0 && <p className="empty">No messages yet. Be the first!</p>}
        {entries.map((entry) => (
          <div key={entry.id} className="entry">
            <strong>{entry.name}</strong>
            <p>{entry.message}</p>
          </div>
        ))}
      </section>
    </div>
  );
}

export default function App() {
  return (
    <ErrorBoundary>
      <GuestBook />
    </ErrorBoundary>
  );
}
