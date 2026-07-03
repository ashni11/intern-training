import Card from "./Card";
type CardItem = {
  title: string;
  description: string;
};
function CardList() {
  const cards: CardItem[] = [
    {
      title: "React",
      description: "A JavaScript library",
    },
    {
      title: "Angular",
      description: "A framework ",
    },
    {
      title: "Vue",
      description: "A JavaScript framework",
    },
  ];
  return (
    <>
      {cards.map((card, index) => (
        <Card
          key={index}
          title={card.title}
          description={card.description}
        />
      ))}
    </>
  );
}
export default CardList;