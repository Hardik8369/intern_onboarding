import { useState } from "react";

function EntryForm({ onSubmit }) {
  const [name, setName] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!name.trim() || !message.trim()) return;
    await onSubmit(name, message);
    setName("");
    setMessage("");
  };

  return (
    <form onSubmit={handleSubmit} style={{marginTop: "20px"}}>
      <h2>Leave a message</h2>
      <div>
        <label>Name: </label>
        <input value={name} onChange={(e) => setName(e.target.value)} required />
      </div>
      <div style={{marginTop: "10px"}}>
        <label>Message: </label>
        <textarea value={message} onChange={(e) => setMessage(e.target.value)} required />
      </div>
      <button type="submit" style={{marginTop: "10px"}}>Sign Guestbook</button>
    </form>
  );
}

export default EntryForm;
