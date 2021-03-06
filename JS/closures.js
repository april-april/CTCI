//example of closure
var message = 'The British are coming.';
function sayMessage(){
    alert(message);  // here we have access to message,
    // even though it's declared outside this function!
};

//example #2 
//putting nextGeneratedId in an IIFE makes
// nextGeneratedId private and not available in the global scope
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