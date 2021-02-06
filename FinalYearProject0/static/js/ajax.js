$(".emoji").click(function () {
    
    var idname = this.id;
    
    $.ajax({
        type :"GET" ,
      url: "displayreviews",
      
      data: {
        'idname': idname
      },
     
      success: function (reviewlist) {
        
          
          console.log(reviewlist[0])
          $(".modal-body").text(reviewlist[0]);
        }
    
  });

});
$(window).load(function() {
  // Animate loader off screen
  $(".se-pre-con").fadeOut("slow");;
});

$("#ok").click(function(){
  $("#hidder").hide();
  $(".se-pre-con").show();

});