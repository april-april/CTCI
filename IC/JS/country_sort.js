let cities = [
    { country: 'USA', name: 'San Francisco' },
    { country: 'Canada', name: 'Toronto' },
    { country: 'France', name: 'Paris' },
    { country: 'USA', name: 'New York' }
];

let countrySort = {};
cities.forEach(function(city) {
    
    if (!countrySort[city.country]) {
        countrySort[city.country] = [];
    }
    countrySort[city.country].push(city.name);
});

console.log(countrySort);
