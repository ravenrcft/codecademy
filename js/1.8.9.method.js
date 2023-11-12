function Rabbit(adjective) {
    this.adjective = adjective;
    this.describeMyself = function() {
        console.log("I am a " + this.adjective + " rabbit");
    };
}

// now we can easily make all of our rabbits
// var objectName = new constructorName(value for each property);

var rabbit1 = new Rabbit("fluffy");
var rabbit2 = new Rabbit("happy");
var rabbit3 = new Rabbit("sleepy")

// objectName.methodName( );
rabbit1.describeMyself();
rabbit2.describeMyself();
rabbit3.describeMyself();