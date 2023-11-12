var friends = {};

friends.bill = {
    firstName:"Bill",
    lastName:"steve",
    number:'(545)456-4568',
    address: ['1545','Stone way','Town','USA']
    };
friends.steve = {
    firstName:"Steve",
    lastName:"bill",
    number:'(505)456-4554',
    address: ['7478','Rockwater Rd','Townville','USA']
    };

var list = function (obj)  {
    for (var prop in obj)   {
        console.log(prop);
    }
};

var search = function(name)  {
    for (var prop in friends)   {
        if (friends[prop].firstName === name)   {
            console.log(friends[prop]);
            return friends[prop];
        }
    }
};