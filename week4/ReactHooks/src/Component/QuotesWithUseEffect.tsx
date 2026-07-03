import { useEffect, useState } from "react";
type QuoteData = {
  quote: string;
  author: string;
};
function QuoteWithUseEffect() {
  const [quoteData, setQuoteData] = useState<QuoteData>({
    quote: "",
    author: "",
  });
  useEffect(() => {
    fetch("https://dummyjson.com/quotes/random")
      .then((response) => response.json())
      .then((data) => {
        setQuoteData({
          quote: data.quote,
          author: data.author,
        });
      })
      .catch((error) => {
        console.log("Error fetching quote:", error);
      });
  }, []);
  return (
    <div className="box">
      <h2>Quote using useEffect</h2>
      <button onClick={() => window.location.reload()}>Get New Quote</button>
      <p>Quote:</p>
      <p>{quoteData.quote}</p>
      <p>- {quoteData.author}</p>
    </div>
  );
}
export default QuoteWithUseEffect;