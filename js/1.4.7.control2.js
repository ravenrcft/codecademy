var isEven = function(number) {
  // Your code goes here!
  if (number % 2)   {
      return false;
  }
  else if (isNaN(number)) {
      return "Please enter a number";
  }
  else  {
      return true;
  }
};