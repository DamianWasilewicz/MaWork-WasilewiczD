// SegFault - Damian Wasilewicz & Sajed Nahian
// SoftDev1 pd6
// K#28 -- Sequential Progression
// 2018-12-18

/**
  * Function that returns the nth value in the fibonacci sequence
  * @param {num} index of value in fib sequence
  * @return {num} nth value in fib sequence
  */

var fibb = (num) => {
  if (num == 0) {
      return 1
  }
    else {
      return (fibb(num - 1)*num)
    }
}
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
}

/**
  * Helper, list of names
  */
var list = ["Damian W.", "Sajed N.", "Tim M.", "Hello", "Jello", "Bello"]
/**
  * Function returns random student name from list of names
  * @return Random Student Name
  */
var randomStudent = () => {
  var number = Math.ceil(Math.random() * (list.length)) - 1
  return list[number]
}
