$("#verify_btn").click(function () {
    alert('fired');
    var idname = this.id;
    
    $.ajax({
        type :"GET" ,
      url: "displayreviews",
      
      data: {
        'idname': idname
      },
     
      success: function (reviewlist) {
        
          alert(reviewlist[0]);
          console.log(reviewlist[1])
        }
    
  });

});