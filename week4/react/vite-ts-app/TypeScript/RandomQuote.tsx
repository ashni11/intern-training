import { useState } from "react";
import type { Quote } from "../Interface/interfaces";

function RandomQuote() {
  const [quote, setQuote] = useState("");
  const [author, setAuthor] = useState("");
  async function fetchQuote() {
    try {
      const response = await fetch("https://dummyjson.com/quotes/random");
      const data: Quote = await response.json();
      setQuote(data.quote);
      setAuthor(data.author);
    } catch {
      setQuote("Unable to fetch quote.");
      setAuthor("");
    }
  }
  return (
    <div>
      <h2>Random Quotes</h2>
      <button onClick={fetchQuote}>Get Quote</button>
      <p>{quote}</p>
      <h4>{author}</h4>
    </div>
  );
}

export default RandomQuote;