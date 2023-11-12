var nyc = {
    fullName: "New York City",
    mayor: "Bill de Blasio",
    population: 8000000,
    boroughs: 5
};

// write a for-in loop to print the value of nyc's properties

var w = "fullName";
var x = "mayor";
var y = "population";
var z = "boroughs";

for (var w in nyc)  {
    console.log(nyc[w]);
}