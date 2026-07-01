const theme = document.getElementById("themeBtn"); //an HTML element using its id.
themeBtn.addEventListener("click", function () {
    document.body.classList.toggle("dark-theme");
    if(document.body.classList.contains("dark-theme")){
        themeBtn.textContent="Light Mode";
    }else{
        themeBtn.textContent="Dark Mode";
    }
});
1


const itemInput = document.getElementById("itemInput"); //Gets the textbox.
const addBtn = document.getElementById("addBtn"); //Gets the Add button.
const itemList = document.getElementById("itemList");
let items = [];
addBtn.addEventListener("click", function(){
    const value = itemInput.value.trim();
    if(value === ""){
        alert("Please enter an item.");
        return;
    }
    items.push(value);
    renderList(); //Display array items on the webpage.
    itemInput.value = "";
});

//dynamic list
function renderList(){
    itemList.innerHTML = ""; //clr existing list to avoid dup
    items.forEach(function(item){
        const li = document.createElement("li");
        li.textContent = item;
        itemList.appendChild(li);
    });
}



// Fetch API
const quoteBtn = document.getElementById("quoteBtn");
quoteBtn.addEventListener("click", function(){
    fetch("https://dummyjson.com/quotes/random")  //sends req
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        document.getElementById("quote").textContent = `"${data.quote}"`;
        document.getElementById("author").textContent = "- " + data.author;
    })
    .catch(function(){
        document.getElementById("quote").textContent = "Unable to fetch quote.";
        document.getElementById("author").textContent = "";
    });
});