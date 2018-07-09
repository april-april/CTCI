//example of closure
var message = 'The British are coming.';
function sayMessage(){
    alert(message);  // here we have access to message,
    // even though it's declared outside this function!
};

//example #2
var getUniqueId = (function(){
    var nextGeneratedId = 0;
    return function(element) {
        if (!element.id) {
            element.id = 'generated-uid-' + nextGeneratedId;
            nextGeneratedId++;
        }
        return element.id;
    };
})();