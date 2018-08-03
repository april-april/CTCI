var person = {
    firstname: 'Default',
    lastname: 'Default',
    greet: function() {
        return 'Hi' + ' ' + this.firstname
    }
}

var thomas = Object.create(person);
console.log(thomas)
console.log(thomas.greet())