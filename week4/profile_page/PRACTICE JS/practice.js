//arithmetic operations
let a=20;
let b=10;
console.log(a+b);
console.log(a-b);
console.log(a*b);
console.log(a/b);
console.log(a%b);
console.log(a**2);

//increment and decrement operators
let z=++a;
console.log(z);
let w=--b;
console.log(w);

//assignment operators 
let r=80;
r+=10;
console.log(r);
r-=20;
console.log(r);
r*=2;
console.log(r);
r/=5;
console.log(r);
r%=3;
console.log(r);

//comparison operators :
let x=10;
let y="10";
console.log(x==y);
console.log(x===y);
console.log(x!=y);
console.log(x!==y);
console.log(x>5);
console.log(x<20);
console.log(x>=10);
console.log(x<=9);


//logical operators
let age=21;
let id=true;
console.log(age>=18 && id);
console.log(age<18 || id);
console.log(!id);

//ternary operator
let marks=75;
let result=marks>=50 ? "Pass" : "Fail";
console.log(result);

//spread operator 
let arr1 = [1,2,3];
let arr2 = [...arr1,4,5];
console.log(arr2);

//array methods :

let fruits = ["Apple", "Banana"];
fruits.push("Orange");//push()methods-adds new element at the end of the array
console.log(fruits);
fruits.pop();    //pop()methods-remove last element
console.log(fruits);
fruits.shift();  //shift()methods-remove first element
console.log(fruits);
fruits.unshift("Mango"); //unshift()methods-adds new element at the beginning of the array
console.log(fruits);
let numbers = [1, 2, 3]; //map()methods-creates a new array by applying a function to each element of the original array
let square = numbers.map(num => num * num);
console.log(square); //filter()methods
let even = numbers.filter(num => num % 2 === 0);
console.log(even);
let numberss = [10, 20, 30, 40];//find()methods-returns the first element that satisfies a condition
let results = numbers.find(num => num > 20);
console.log(results);

//normal functions:
function greet() {
    console.log("Hello");
}
greet();

//arrow functions:
const greetname = () => {
    console.log("Hello");
};
greetname();
