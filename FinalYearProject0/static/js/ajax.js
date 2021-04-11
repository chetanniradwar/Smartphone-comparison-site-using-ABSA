$(".emoji").click(function () {
    
    var idname = this.id;
    
    $.ajax({
        type :"GET" ,
      url: "displayreviews",
      
      data: {
        'idname': idname
      },
     
      success: function (review_list) {
        
          $(".modal-body").empty();
          // console.log(reviewlist[0])
          
          var i;
          for (i = 0; i < review_list.length; i++) {
          $(".modal-body").append(`<p>${review_list[i]}</p><hr>`);
          // console.log(reviewlist[i]);
          // $(".modal-body").text(reviewlist);
          }
        }
    
  });

});


//This is loding gif
$(window).load(function() {

  $(".se-pre-con").fadeOut("slow");;
});

$("#ok").click(function(){
  $("#hidder").css("filter","blur(3px)");
  $(".se-pre-con").show();

});