const head = document.getElementById("heading");
const adder = document.getElementById("add");
const fibo = document.getElementById("fibo");
const thelist = document.getElementById("thelist");
let list_elements = thelist.getElementsByTagName("li");

const updateList = () => {
    list_elements = thelist.getElementsByTagName("li");
    for (let i = 0; i < list_elements.length; i++) {
        let element = list_elements[i];
        element.addEventListener('click', removeItem);
        element.addEventListener('mouseover', changeHeading(element.innerText));
        element.addEventListener('mouseout', changeHeading("Hello World!"));
    }
}

const changeHeading = (text) => {
    let ret = (e) => {
        head.innerText = text;
    }
    return ret;
}

const removeItem = (e) => {
    e.target.parentNode.removeChild(e.target);
    updateList();
}

const addToList = (list, content) => {
    let ret = (e) => {
        list.innerHTML += `<li>${content}</li>`;
    }
    return ret;
}

const fiblist = [0,1,1];
const fib = (n) => {
    if (fiblist[n]) {
        return fiblist[n];
    }
    fiblist[n] = fib(n - 1) + fib(n - 2);
    return fiblist(n);
}

const fact = (n, r=1) => {
    if (n < 2) {
        return r;
    }
    return fact(n - 1, r * n);
}

//EVENTS
updateList();
adder.addEventListener('click', addToList(thelist));
