//Amanda Zheng and Yevgeniy Gorbachev
//Softdev pd 1
//K27 -- Sequential Progression
//12-11-2019

var select_field = document.getElementById('function');
var input_field = document.getElementById('arg');
var button = document.getElementById('eval');
var result_field = document.getElementById('result');

button.onclick = setOutput

var setOutput = function() {
    console.log('evaluating');
    fname = select_field.getAttribute(value);
    console.log(fname);
    argument = input_field.getAttribute(value);
    console.log(argument)
    result = selectFunc(fname, argument);
    result_field.innerText = String(result);
}

var selectFunc = function(fname, argument) {
    switch (fname) {
        case 'fact':
            return fact(argument);
        case 'fib':
            return fib(argument);
        case 'gcd':
            return gcd(argument);
        case 'selectRandom':
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

var gcd = function(a,b) {
    if (a % b == 0) {
        return b;
    }
    return gcd(b, a % b);
}

var selectRandom = function(array) {
    if ((typeof array) == String) {
        array = array.split(",")
    }
    return array[Math.floor(Math.random()*array.length)];
}
