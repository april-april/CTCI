function Product(name, price) {
    this.name = name;
    this.price = price;
  }
  
  function Food(name, price) {
    Product.call(this, name, price);
    this.category = 'food';
  }
  
  function Toy(name, price) {
    Product.call(this, name, price);
    this.category = 'toy';
  }
  
  var pizza = new Food('peppppporoni', 5);
  var fun = new Toy('car', 30);


  // --------------------------------------------

  function greet() {
    var reply = [this.animal, 'typically sleep between', this.sleepDuration].join(' ');
    console.log(reply);
  }
  
  var obj = {
    animal: 'cats', sleepDuration: '12 and 16 hours'
  };
  
  greet.call(obj);  // cats typically sleep between 12 and 16 hours