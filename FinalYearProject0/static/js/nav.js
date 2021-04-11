

// $(".burger").-toggle(
//     // alert("The paragraph was clicked.");
//     // $("nav ul").show();
//     function(){$("nav ul").css({"display":"block"});},
//     function(){$("nav ul").css({"display":"none"});}

//   });
$(document).ready(function(){
    $(".burger").click(function(){
        if($("nav ul").css("display")=="none")
{
        $("nav ul").css("display", "flex");
}
else{
        $("nav ul").css("display", "none");
}
    });
  });
// function myFunction() {
//     var x = document.getElementsByTagName("ul");
//     if (x.style.display === "none") {
//       x.style.display = "flex";
//     } else {
//       x.style.display = "none";
//     }
//   }