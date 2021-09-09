function showImages() {

  $(".page").click(function() {
    $(".page").css("color", "black");
    $(this).css('color', 'red');
    var index = $(this).attr("class").split(" ")[1].split("-")[1];
    var i = 0;
    var result = "";
    var images = $('#images').data();
    images_array = images.name.substring(1, images.name.length - 1).split(', ')
    for (i = (index - 1) * 10; i <= (index - 1) * 10 + 9; i++)
      result += '<div class="gridItem"> <img style="width:100%;height: 250px" src="../static/images1/' + images_array[i].substring(1, images_array[i].length - 1) + '" /></div>'
    document.getElementById("gridImages").innerHTML = result;
  });

}

function showBorder()
{console.log(document.getElementById("autocomplete").innerHTML.length);
  if(document.getElementById("autocomplete").innerHTML.length<=3)
      document.getElementById("autocomplete").style.border = "none";
  else
  {
    document.getElementById("autocomplete").style.border  = " 0.5px solid gray";
    document.getElementById("autocomplete").style.borderTop  = "none";
  }
}

function getSuggest(i) {

  document.getElementById("textInput").value = document.getElementsByClassName("suggest")[i].innerHTML;
}

function autoComplete(query) {
  $.ajax({
    method: "POST",
    url: "/",
    data: JSON.stringify({
      "query": query,
    }),
    contentType: "application/json",
    dataType: 'json',

    success: function(res) {
      var i = 0;
      var p = "";
      for (i = 0; i < res['a'].length; i++) {
        p += "<p class='suggest' onclick = 'getSuggest(" + i + ")' >" + res['a'][i] + "</p>";

      }
      document.getElementById("autocomplete").innerHTML = p;
      showAutoComplete();
    }
  });
}

function hideAutoComplete() {
  setTimeout(function() {

  document.getElementById("autocomplete").style.visibility = "hidden";
}, 100);
}

function showAutoComplete() {
  showBorder();
  document.getElementById("autocomplete").style.visibility = "visible";

}

function submitCorrect()
{
  document.getElementById("textInput").value = document.getElementById("correction").innerHTML;
  document.getElementById("textForm").submit();
}

function relevanceFeedBack(imgName) {
  var query = document.getElementById("userQuery").innerHTML;
  $.ajax({
    method: "POST",
    url: "/",
    data: JSON.stringify({
      "imgName": imgName,
      "txtQuery": query,
    }),
    contentType: "application/json",
    dataType: 'json',

    success: function() {
    console.log(imgName);
    }
  });
}

$(document).ready(function() {


  var images = $('#images').data();
  images_array = images.name.substring(1, images.name.length - 1).split(', ')
  showImages();
  $(".actions").click(function() {
    var choice = $(this).attr("class").split(" ")[1];
    var recent = document.getElementsByClassName("page")[document.getElementsByClassName("page").length - 1].innerHTML;
    var nine = 9;
    if (choice == "next") {
      var recent = parseInt(recent) + 1;
    } else {

      var recent = parseInt(recent) - 19;
    }
    // console.log(recent);
    // console.log('length');
    if (recent == 1) {
      $(".prev").css("visibility", "hidden");
      $(".next").css("visibility", "visible");
    } else if (recent + 9 == parseInt(images_array.length / 10)) {
      // if (images_array.length % 10 !=0)
      // {
      //   recent = parseInt(images_array.length / 10) +1;
      //   nine =0;
      // }
      $(".prev").css("visibility", "visible");
      $(".next").css("visibility", "hidden");
    } else {
      $(".prev").css("visibility", "visible");
      $(".next").css("visibility", "visible");

    }
    document.getElementById("numberContainer").innerHTML = "";
    for (var i = recent; i <= recent + nine; i++)
      document.getElementById("numberContainer").innerHTML += '<p class="page number-' + i + '">' + i + '</p>';
    showImages();
    document.getElementsByClassName("page")[0].click();
  });

});
