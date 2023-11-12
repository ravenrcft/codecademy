/*jshint multistr:true */

text = "blah Bob blah Bob blah Bob blah Bob \
blah Bob blah Bob blah Bob blah Bob blah Bob \
blah Bob blah Bob blah Bob ";

var myName = "bob";
var hits = [];

for(var i = 0; i < text.length; i++) {
    if (text[i] === 'B')    {
        for(var j = i; j < (myName.length + i); j++)    {
            hits.push(text[j]);
        }
    }
}

if (hits.length === 0)  {
    console.log("Your name wasn't found!");
}
else    {
    console.log(hits);
}