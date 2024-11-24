let products = {
    data: [
      {
        productName: "IOT Internet of Things",
        category: "Theory",
        price: "FREE",
        image: "../static/iot-logo.jpg",
        info:"Duration : 12 Week ",
        info1: " Get Complition Certification"
      },
      {
        productName: "Data Structure and Algorithms",
        category: "Theory",
        price: "FREE",
        image: "../static/dsa-log.jpg",
        info:"Duration : 16 Week ",
        info1: " Get Complition Certification"
      },
      {
        productName: "operating system",
        category: "Theory",
        price: "FREE",
        image: "../static/oparating-system-logo.jpg",
        info:"Duration : 8 Week ",
        info1: " Get Complition Certification"
      },
      {
        productName: "cyber security",
        category: "Theory",
        price: "FREE",
        image: "../static/cyber-security-logo.jpg",
        info:"Duration : 8 Week ",
        info1: " Get Complition Certification"
      },
      {
        productName: "machine learning",
        category: "Pratical",
        price: "FREE",
        image: "../static/machine-learning-logo.jpg",
        info:"Duration :  6 Month ",
        info1: " Get Complition Certification"
      },
      {
        productName: "c++",
        category: "Pratical",
        price: "FREE",
        image: "../static/c-logo.jpg",
        info:"Duration : 12 Week ",
        info1: " Get Complition Certification"
      },
      {
        productName: "web developement ",
        category: "Pratical",
        price: "FREE",
        image: "../static/web-developement-logo.jpg",
        info:"Duration : 6 Month ",
        info1: " Get Complition Certification"
      },
      {
        productName: "java programming",
        category: "Pratical",
        price: "FREE",
        image: "../static/java-logo.jpg",
        info:"Duration : 6 Month ",
        info1: " Get Complition Certification",
        button: "/java",
      },
      {
        productName: "python programming",
        category: "Pratical",
        price: "FREE",
        image: "../static/python-logo.jpg",
        info: "Duration : 6 month ",
        info1: " Get Complition Certification ",
        button: "/python",
      },
    ],
  };
  
  for (let i of products.data) {
    //Create Card
    let card = document.createElement("div");
    //Card should have category and should stay hidden initially
    card.classList.add("card", i.category, "hide");
    //image div
    let imgContainer = document.createElement("div");
    imgContainer.classList.add("image-container");
    //img tag
    let image = document.createElement("img");
    image.setAttribute("src", i.image);
    imgContainer.appendChild(image);
    card.appendChild(imgContainer);
    //container
    let container = document.createElement("div");
    container.classList.add("container");
    //product name
    let name = document.createElement("h5");
    name.classList.add("product-name");
    name.innerText = i.productName.toUpperCase();
    container.appendChild(name);
    //price
    let price = document.createElement("h6");
    price.innerText =  i.price;
    container.appendChild(price);
  
    card.appendChild(container);
    document.getElementById("products").appendChild(card);
    //create info tag 
    let info = document.createElement("p");
    info.innerText= ""+i.info;
    container.appendChild(info);
    //create info tag 
    let info1 = document.createElement("p");
    info1.innerText= ""+i.info1;
    container.appendChild(info1);
    // let a= document.createElement("a");
    // create abutton 
    let button =document.createElement("a");
    button.setAttribute("href",i.button)
    button.innerText="Enroll Now";
    container.appendChild(button);
  }
  
  //parameter passed from button (Parameter same as category)
  function filterProduct(value) {
    //Button class code
    let buttons = document.querySelectorAll(".button-value");
    buttons.forEach((button) => {
      //check if value equals innerText
      if (value.toUpperCase() == button.innerText.toUpperCase()) {
        button.classList.add("active");
      } else {
        button.classList.remove("active");
      }
    });
  
    //select all cards
    let elements = document.querySelectorAll(".card");
    //loop through all cards
    elements.forEach((element) => {
      //display all cards on 'all' button click
      if (value == "all") {
        element.classList.remove("hide");
      } else {
        //Check if element contains category class
        if (element.classList.contains(value)) {
          //display element based on category
          element.classList.remove("hide");
        } else {
          //hide other elements
          element.classList.add("hide");
        }
      }
    });
  }
  
  //Search button click
  document.getElementById("search").addEventListener("click", () => {
    //initializations
    let searchInput = document.getElementById("search-input").value;
    let elements = document.querySelectorAll(".product-name");
    let cards = document.querySelectorAll(".card");
  
    //loop through all elements
    elements.forEach((element, index) => {
      //check if text includes the search value
      if (element.innerText.includes(searchInput.toUpperCase())) {
        //display matching card
        cards[index].classList.remove("hide");
      } else {
        //hide others
        cards[index].classList.add("hide");
      }
    });
  });
  
  //Initially display all products
  window.onload = () => {
    filterProduct("all");
  };