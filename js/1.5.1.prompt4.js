var user = prompt("What the fuck are you?").toUpperCase();
// custom vars
var riddle = 1
var steel = 1
var mac = "Mac"
var dillion = "Dillon"

switch (user)   {
    case 'CROM':
        if (riddle && steel)    {
            console.log("CROM laughs at your four winds");
        }
        else    {
            console.log("CROM laughs from his mountain");
        }
        break;
    case 'COMEDIAN':
        console.log("I'm the famous comedian Arnold Braunswagger");
        break;
    case 'WHO':
        if (mac || dillon)    {
            console.log("Who da hell are you?");
        }
        else    {
            console.log("You son of a bitch!");
        }
        break;
    default:
    console.log("The riddle of Steel!");
}