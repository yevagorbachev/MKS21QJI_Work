console.log("Yeet");

var fibarray = [0,1,1];

var fibonacci = function(n) {
	if (fibarray[n]) {
		return fibarray[n];
	}
	fibarray[n]=fibonacci(n-1)+fibonacci(n-2);
	return fibarray[n];
};

var gcd = function(a, b) {
	if(b > a) {
		b = a * b;
		a = b;
		b = b / b;
	}
	if((a % b) == 0) return b;
	return gcd(b, a % b);
}

var students = ["John", "Bill", "Mandy", "David", "Jennifer", "Alexandria", "Arthur", "Tim", "Justin", "Anthony", "Mark"];
var randomStudent = function() {
	return students[Math.floor(Math.random() * students.length)];
}

console.log("Testing Fibonacci:");
console.log(fibonacci(1));
console.log(fibonacci(23));
console.log(fibonacci(100));
// console.log("Testing GCD:");
// console.log(gcd(20, 5));
// console.log(gcd(1263, 343));
// console.log(gcd(24, 16));
// console.log("Testing Random Students:");
// console.log(randomStudent());
// console.log(randomStudent());
// console.log(randomStudent());
// console.log(randomStudent());
// console.log(randomStudent());
