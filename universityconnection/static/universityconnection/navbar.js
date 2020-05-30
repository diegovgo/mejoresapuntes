
$(document).ready(function(){
  $("#navbar").find('a').hover(function(){
    $(this).css("background-color", "lightgray");
    $(this).css("color", "black");
    }, function(){
    $(this).css("background-color", "#333");
    $(this).css("color", "white");
  });
});