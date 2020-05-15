console.log('done btchhhhh')


$("select[name='course']").empty();
$(".mycoursesform").clone().appendTo("select[name='course']");


var current_user_id = $("select[name='plays']").val();

function openNoteForm() {
    document.getElementById("apuntesForm").style.display = "block";
  }
  
  function closeNoteForm() {
    document.getElementById("apuntesForm").style.display = "none";
  }


/*const getData = () => {
    axios.get('http://127.0.0.1:8000/api/notas').then(response => {
        response.data.map(element =>{
          let title = element.title;
          //let user = element.user;
          //let current_user_id = $("select[name='plays']").val();
          //let text = "<li>"+title+"</li>"
          //if (user == current_user_id){
            //$('#titles').append(text);
          }  
        });
    });
};
const sendData = () => {
    axios.post('http://127.0.0.1:8000/api/notas');
}


getData();

*/

$('#notas').removeClass();
$('#notas').addClass("nav-item active");
$('#notas').css("background-color", "lightgray");
$('#notas').hide();
$('#notas').show(400);


//getNote.addEventListener('click', getData);