var likes=0, dislikes=0;

//Functions to increase likes and immediately calculate bar widths
function like(){
	likes++;
	calculateBar();
}
function dislike(){
	dislikes++;
	calculateBar();
}

//Calculates bar widths
function calculateBar(){
	var total= likes+dislikes;
    //Simple math to calculate percentages
	var percentageLikes=(likes/total)*100;
	var percentageDislikes=(dislikes/total)*100;

    //We need to apply the widths to our elements
	document.getElementById('likes').style.width=percentageLikes.toString()+"%";
	document.getElementById('dislikes').style.width=percentageDislikes.toString()+"%";
    
    //We add the numbers on the buttons, just to show how to
    document.getElementById('likeButton').value="Like ("+likes.toString()+")";
    document.getElementById('dislikeButton').value="Disike ("+dislikes.toString()+")";

}

calculateBar();
