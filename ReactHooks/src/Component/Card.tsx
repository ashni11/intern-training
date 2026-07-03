type CardProps = {
  title: string;
  description: string;
};

function Card(props: CardProps) {
  return (
    <div className="box">
      <h2>{props.title}</h2>
      <p>{props.description}</p>
    </div>
  );
}

export default Card;