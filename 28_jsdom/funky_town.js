//Amanda Zheng and Yevgeniy Gorbachev
//Softdev pd 1
//K27 -- Sequential Progression
//12-11-2019
var fact = function(n){
    if(n < 2){
        return 1;
    }
    return n * fact(n-1);
}

var fib = function(n, prev = [0,1,1]){
    if (prev[n]){
        return prev[n];
    }
    prev[n] = fib(n-1, prev) + fib(n-2, prev);
    return prev[n];
}

var gcd = function(a,b){
    if(a % b == 0){
        return b;
    }
    return gcd(b, a % b);
}

var selectRandom = function(array){
    if ((typeof array) == String) {
        array = array.split(",")
    }
    return array[Math.floor(Math.random()*array.length)];
}
