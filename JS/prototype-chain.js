// prototype chain example from MDN

let gold = {a: 1};
console.log(gold.a);
console.log(gold.z)

let blue = Object.create(gold);
blue.b = 2;
console.log(blue.b + ': ' + 'value of b');
console.log(blue.a + ': ' + 'value of a');

let Person = function(name) {
    this.name = name;
    this.canTalk = true;
};
  
Person.prototype.greet = function() {
    if (this.canTalk) {
      console.log('Hi, I am ' + this.name);
    }
};
  
let Employee = function(name, title) {
    Person.call(this, name);
    this.title = title;
};

Employee.prototype = Object.create(Person.prototype)

Employee.prototype.greet = function() {
    if (this.canTalk) {
      console.log('Hi, I am ' + this.name + ', the ' + this.title);
    }
};

let Customer = function(name) {
    Person.call(this, name);
};

Customer.prototype = Object.create(Person.prototype);

let Mime = function(name) {
    Person.call(this, name);
    this.canTalk = false;
};

Mime.prototype = Object.create(Person.prototype);

let bob = new Employee('Bob', 'Builder');
let joe = new Customer('Joe');
let rg = new Employee('Red Green', 'Handyman');
let mike = new Customer('Mike');
let mime = new Mime('Mime');

bob.greet();
// Hi, I am Bob, the Builder

joe.greet();
// Hi, I am Joe

rg.greet();
// Hi, I am Red Green, the Handyman

mike.greet();
// Hi, I am Mike

mime.greet();
  