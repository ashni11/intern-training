import  { Component } from "react";
type QuoteState = {
  quote: string;
  author: string;
  loading: boolean;
  error: string;
};
class QuoteGenerator extends Component<object, QuoteState> {
  constructor(props: object) {
    super(props);
    this.state = {
      quote: "Loading quote...",
      author: "",
      loading: true,
      error: "",
    };
  }
  fetchQuote = () => {
    this.setState({
      loading: true,
      error: "",
    });
    fetch("https://dummyjson.com/quotes/random")
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          quote: data.quote,
          author: data.author,
          loading: false,
        });
      })
      .catch((error) => {
        console.error("Error fetching quote:", error);
        this.setState({
          error: "Failed to fetch quote. Please try again.",
          loading: false,
        });
      });
  };
  componentDidMount(): void {
    this.fetchQuote();
  }
  render() {
    const { quote, author, loading, error } = this.state;
    return (
      <div className="card-box">
        <h2>Random Quote Generator</h2>
        {loading ? (
          <p>Loading quote...</p>
        ) : error ? (
          <p>{error}</p>
        ) : (
          <>
            <p className="quote-text">"{quote}"</p>
            <p className="quote-author">- {author}</p>
          </>
        )}

        <button onClick={this.fetchQuote}>Get New Quote</button>
      </div>
    );
  }
}
export default QuoteGenerator;