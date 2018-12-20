//Poppyseeds - Damian Wasilewicz & Sophia Xia
// SoftDev1 pd6
// K#29 - Sequential Progression II: Electric Boogaloo...
//2018-12-19
/**
  * Function that returns the nth value in the fibonacci sequence
  * @param {num} index of value in fib sequence
  * @return {num} nth value in fib sequence
  */

var fibb = (num) => {
  if (num == 0) {
      return 1;
  }
    else if(num == 1) {
      return 1;
    }
    else {
     return fibb(num - 1) + fibb(num -2);
    }
};
/**
  * Function that makes use of Euclid's algorithm to find the greatest
  * common denominator of two integers
  * @params {num} a - first number
  * @params {num} b - second number
  * @return {num} greatest common denominator of a and b
  */
var gcd = (a, b) => {
  if (a < b){
    var c = b
    b = a
    a = c
  }
  var r = a % b
  if (r == 0) {
    return b;
  }
  else {
     return gcd(b, r);
  }
};

/**
  * Helper, list of names
  */
var list = ["Damian W.", "Sajed N.", "Tim M.", "Hello", "Jello", "Bello"]
/**
  * Function returns random student name from list of names
  * @return Random Student Name
  */
  var randstu = function(){
      var num = Math.floor(Math.random() * list.length);
      console.log(list[num])
      return list[num];
  };


/**
  When calling function with parameters, use anonymous function to call desired function
  within event listener
  */
  var f_tag = document.getElementById("fibbresults");
  var g_tag = document.getElementById("gcdresults");
  var s_tag = document.getElementById("sturesults");

  document.getElementById("buta").addEventListener("click", function() {
    console.log(fibb(10));
    f_tag.innerHTML = fibb(10);
  });

  document.getElementById("butb").addEventListener("click", function() {
    console.log(gcd(5,10));
    g_tag.innerHTML = gcd(5,10);
  });

  document.getElementById("butc").addEventListener("click", function() {
    randstu();
    s_tag.innerHTML = randstu();
  });
