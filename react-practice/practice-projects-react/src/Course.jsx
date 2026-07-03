import { useState } from 'react';
function Course(props) {

    const [purchased, setPurchased] = useState(false);

    function BuyCourse(){
        alert(`You have bought ${props.name} for ${props.price}`);
        setPurchased(true);
        console.log(purchased);
    }

  return (
    <div className="card">
      <h1>{props.name}</h1>
      <p>{props.price}</p>
      <button onClick={BuyCourse}>Buy Now</button>
      <p>{purchased ? "Purchased!" : "Not purchased yet."}</p>
    </div>
  );
}

export default Course;
