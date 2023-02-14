function fib(n) {
  let sqrt5 = Math.sqrt(5)
  return (Math.pow(1 + sqrt5, n) - Math.pow(1 - sqrt5, n)) / (Math.pow(2, n) * sqrt5);
}

console.log(fib(0));
console.log(fib(1));
console.log(fib(2));
console.log(fib(3));
console.log(Math.trunc(fib(4)));
