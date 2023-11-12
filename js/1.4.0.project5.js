/*jshint multistr:true */

text = "blah Bob blah Bob blah Bob blah Bob \
blah Bob blah Bob blah Bob blah Bob blah Bob \
blah Bob blah Bob blah Bob ";

var myName = "bob";
var hits = [];

for(var i = 0; i <text.length; i++) {
    if (text[i] === 'B')    {
        for(var j = i; j < (myName.length + i); j++)    {
            hits.push(text[j]);
        }
    }
}