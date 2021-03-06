// Seg Fault-- Damian Wasilewicz and Sajed Nahian
//
// SoftDev1 pd6
//
//K #30: Sequential Progression III: Season of the Witch
//
// 2018-12-21
// Phase III

/*
Retrieves list and button, adds event listener to button that creates new list item,
increments var num, and appends new item to list
*/
var list = document.getElementById("thelist")
var button = document.getElementById("b")
var num = 8;
button.addEventListener ('click', function (e) {
    var item = createListItem("item " + num)
    num++;
    list.appendChild(item)
})

/*
@argument (itemText)-takes in string that will appear on item in browser
@return item
*/
var createListItem = function (itemText) {
  var item = document.createElement("li")
  item.innerHTML = itemText
  item.addEventListener('mouseover', mouseOver)
  item.addEventListener('mouseout', mouseOut)
  item.addEventListener('click', clickItem)
  return item
}
/* functions that determine what text appears in heading, depending on whether the mouse
is on an item or off */
var heading = document.getElementById("h")
var items = document.getElementsByTagName("li")

var mouseOver = function(e) {
  heading.innerHTML = e.target.innerHTML;
}

var mouseOut = function() {
  heading.innerHTML = "Hello World!"
}

var clickItem = function(e) {
  e.target.remove()
  heading.innerHTML = "Hello World!"
}

for (var i = 0; i < items.length; i++) {
  items[i].addEventListener('mouseover', mouseOver)
  items[i].addEventListener('mouseout', mouseOut)
  items[i].addEventListener('click', clickItem)
}

// Phase IV
/*upon clicking fibb button, values at increasing indexes of the fibbonaci sequence appears
*/
var fibList = document.getElementById("fiblist")
var fibButton = document.getElementById("fb")
var nextFib = 1;

var getFibNumber = function(num) {
  if (num < 2) {
    return num <= 0 ? 0 : 1
  }
  return getFibNumber(num - 1) + getFibNumber(num - 2)
}

fibButton.addEventListener('click', function () {
  var fibListElement = document.createElement('li')
  fibListElement.innerHTML = getFibNumber(nextFib++)
  fibList.appendChild(fibListElement)
})

