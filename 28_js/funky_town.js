// SegFault - Damian Wasilewicz & Sajed Nahian
// SoftDev1 pd6
// K#28 -- Sequential Progression
// 2018-12-18


var fibb = (num) => {
  if (num == 0) {
      return 1
  }
    else {
      return (fibb(num - 1)*num)
    }
}

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


var list = ["Damian W.", "Sajed N.", "Tim M.", "Hello", "Jello", "Bello"]

var randomStudent = () => {
  var number = Math.ceil(Math.random() * (list.length)) - 1
  return list[number]
}
