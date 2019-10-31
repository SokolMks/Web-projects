function addProduct() {
  request = {
    url: "post/",
    type: "POST",
    data: {
      name: $("#addName").val(),
      description: $("#addDesc").val(),
      price: $("#addPrice").val()
    },
    success: function (response){
      alert("Please update the page to see the change");
      var newProduct = "<li id='" + response.id + "'>" + response.name + " <button class='delBut' type=button>Delete</button></li>"
      $("#products").append(newProduct)
      $("li").click(getDetails)
    },
    error:  printError
  }
  $.ajax(request)
}
function updatePage(response) {
  alert("Please update the page to see the change");
  var newProduct = "<li id='" + response.id + "'>" + response.name + " <button class='delBut' type=button>Delete</button></li>";
  $("#products").append(newProduct);
}
function printError() {
  alert("Error");
}

function deleteProduct(){
  id = $(this).parent().attr("id")
  request = {
    url: "delete/" + id + "/",
    type: " DELETE",
    success: delMessage,
    error: printError
  }
  $.ajax(request)
  $(this).parent().remove()
}
function delMessage(){
  alert("Selected product was deleted");
}

function getDetails(){
  id = $(this).attr("id")
  request = {
    url: "details/" + id,
    type: "GET",
    success: function (response){
      $(".currentProduct").attr("id", response.id)
      $("#newName").val(response.name)
      $("#newDesc").val(response.desc)
      $("#newPrice").val(response.price)
    },
    error: printError
  }
  $.ajax(request)
}

function updateProduct(){
  id = $(".currentProduct").attr("id")
  request = {
    url: "update/" + id + "/",
    type: "PUT",
    data: {
      id: $(".currentProduct").attr("id"),
      name: $("#newName").val(),
      description: $("#newDesc").val(),
      price: $("#newPrice").val()
    },
    success: function (response) {
      $("#" + response.id).text(response.name)
      $("#" + response.id).append("<button class='delBut' type=button>   Delete</button>")
      $(".delBut").click(deleteProduct)
    },
    error: printError
  }
  $.ajax(request)
}

$(function() {
    $("#addProduct").click(addProduct)
    $(".delBut").click(deleteProduct)
    $("li").click(getDetails)
    $("#update").click(updateProduct)
})
