const head = document.getElementById("heading");
const itemList = document.getElementById("item-list");
const itemListButton = document.getElementById("item-list-button");
const fibList = document.getElementById("fib-list");
const fibListButton = document.getElementById("fib-list-button");

const addLiEvents = (element) => {
    element.addEventListener('click', removeItem);
    element.addEventListener('mouseover', changeHeading(element.innerText));
    element.addEventListener('mouseout', changeHeading("Hello World!"));
}

const updateInitialList = () => {
    let list_elements = itemList.getElementsByTagName("li");
    for (let i = 0; i < list_elements.length; i++) {
        let element = list_elements[i];
        addLiEvents(element);
    }
}

const changeHeading = (text) => {
    let ret = (e) => {
        head.innerText = text;
    }
    return ret;
}

// removes item from arbitrary list
const removeItem = (e) => {
    e.target.parentNode.removeChild(e.target);
}

// adds item to arbitrary list. Content is given by func 
const addItem = (list, func, updater = () => 0) => {
    let ret = () => {
        let toAdd = document.createElement("li");
        toAdd.appendChild(document.createTextNode(func()));
        updater(toAdd);
        list.appendChild(toAdd);
    }
    return ret;
}

// function to return nth fib number (0 index)
fibn = [0, 1, 1]
const fib = (n) => {
    if (fibn[n] != undefined) {
        return fibn[n];
    }
    fibn[n] = fib(n - 1) + fib(n - 2);
    return fibn[n];
}

//EVENTS
updateInitialList();
itemListButton.addEventListener("click", addItem(itemList, () => "item " + (itemList.childElementCount), addLiEvents));
fibListButton.addEventListener("click", addItem(fibList, () => fib(fibList.childElementCount)));