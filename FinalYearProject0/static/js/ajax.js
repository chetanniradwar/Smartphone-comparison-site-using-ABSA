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