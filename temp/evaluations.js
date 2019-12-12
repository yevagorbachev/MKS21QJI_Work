//Amanda Zheng and Yevgeniy Gorbachev
//Softdev pd 1
//K27 -- Sequential Progression
//12-11-2019

const select_field = document.getElementById("select");
const input_field = document.getElementById("input");
const evaluation_trigger = document.getElementById("eval");
const result_field = document.getElementById("result");

evaluation_trigger.addEventListener("click", () => setOutput());

const setOutput = function() {
    
}

var selectFunc = function(fname, argument) {
    switch (fname) {
        case "fact":
            return fact(argument);
        case "fib":
            return fib(argument);
        case "gcd":
            return gcd(argument);
        case "selectRandom":
            return selectRandom(argument);
    }
}

// Functions
var fact = function(n) {
    if (n <= 1) {
        return 1;
    }
    return n * fact(n-1);
}

var fib = function(n, prev = [0,1,1]) {
    if (prev[n]) {
        return prev[n];
    }
    prev[n] = fib(n-1, prev) + fib(n-2, prev);
    return prev[n];
}

var gcd = function(a, b) {
    if (a % b == 0) {
        return b;
    }
    return gcd(b, a % b);
}

var selectRandom = function(array, delimiter = ",") {
    if ((typeof array) == String) {
        array = array.split(delimiter)
    }
    return array[Math.floor(Math.random()*array.length)];
}
