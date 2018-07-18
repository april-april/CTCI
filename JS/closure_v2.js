function createCounter() {
    let count = 0;
    return function() {
        return ++count;
    };
}

let counter = createCounter();

console.log('Counter 1: ' + counter())
console.log('Counter 1: ' + counter())
console.log('Counter 1: ' + counter())

let counter2 = createCounter()
console.log('Counter 2 ' + counter2())
console.log('Counter 2 ' + counter2())

console.log(counter())
