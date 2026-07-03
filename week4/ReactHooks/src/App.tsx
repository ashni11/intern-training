import { useState } from "react";
import "./App.css";
import Counter from "./Component/Counter";
import CardList from "./Component/CardList";
import ThemeToggle from "./Component/ThemeToggle";
import QuoteGenerator from "./Component/QuoteGenerator";
import QuotesWithUseEffect from "./Component/QuotesWithUseEffect";
function App() {
  const [darkMode, setDarkMode] = useState<boolean>(false);
  return (
    <div
      className={
        darkMode
          ? "app-container dark-theme"
          : "app-container light-theme"
      }
    >
      <h1>Day 19 - React Fundamentals</h1>
      <ThemeToggle darkMode={darkMode} setDarkMode={setDarkMode} />
      <Counter />
      <CardList />
      <QuoteGenerator />
      <QuotesWithUseEffect />
    </div>
  );
}
export default App;