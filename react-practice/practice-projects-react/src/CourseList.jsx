import Course from "./Course";

function CourseList() {
  const courses = [
    { name: "React", price: "$19.99" },
    { name: "Angular", price: "$29.99" },
    { name: "Vue", price: "$39.99" }
  ];
  return (
    <>
      {courses.map((course, index) => (
        <Course
          key={index}
          name={course.name}
          price={course.price}
        />
      ))}
    </>
  );
}

export default CourseList;