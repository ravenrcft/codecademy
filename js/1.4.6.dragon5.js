// Setting vars for slaying
var slaying = true;
var youHit = Math.floor(Math.random() * 2);
var damageThisRound = Math.floor(Math.random()*5 + 1);
var totalDamage = 0;

// while loops + if statements
while (slaying) {
    if (youHit) {
        console.log("Hit!" + damageThisRound + "DMG");
        totalDamage += damageThisRound;
        
        if (totalDamage >= 4)   {
            console.log("Dragon slayed");
            slaying = false;
        }
        else {
            youHit = Math.floor(Math.random() * 2);
        }
    }
    else (youHit = 0);   {
        console.log("The dragon has dick slapped you");
    }
    slaying = false;
}
