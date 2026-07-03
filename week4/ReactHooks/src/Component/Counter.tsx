import { useState } from "react";
function Counter() {
  const [count, setCount] = useState<number>(0);
  function increment() {
    setCount(count + 1);
  }
  function decrement() {
    setCount(count - 1);
  }
  return (
    <div className="card-box">
      <h2>Counter Component</h2>
      <p className="counter-value">Count: {count}</p>
      <div className="btn-group">
        <button onClick={increment}>Increment</button>
        <button onClick={decrement}>Decrement</button>
      </div>
    </div>
  );
}
export default Counter;