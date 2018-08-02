function baz() {
    var x = 1;
    return {
        foo: function foo() { return ++x; },
        bar: function bar() { return --x; }
  };
}
 
var closures = baz();
 
console.log(
    closures.foo(), // 2
    closures.bar(), // 1
    closures.foo()  // 2
);
