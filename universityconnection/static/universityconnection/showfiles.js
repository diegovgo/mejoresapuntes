console.log('done btchhhhh')

$("select[name='apuntes']").empty();
$(".myapuntessform").clone().appendTo("select[name='apuntes']");

var current_user_id = $("select[name='plays']").val();

function openNoteForm() {
    document.getElementById("apuntesForm").style.display = "block";
  }
  
  function closeNoteForm() {
     document.getElementById("apuntesForm").style.display = "none";
  }


  function openArchiveForm() {
    document.getElementById("archivosForm").style.display = "block";
  }
  
  function closeArchiveForm() {
    document.getElementById("archivosForm").style.display = "none";
  }


/*  const titles = []

var userapuntess;

let Loop = () => {
  for (var i = 0 ; i < userapuntess.length; i++) {
  console.log(i);
  console.log(1);
}
}
$("option").addClass('hidethisbitch');

let Loop2 = () => {
  option = $("option").val();
  console.log(option);
}

do {
  $("option").removeClass();
}
while ($("option").val() == 1)

const aaba = () => {
  $("option").forEach(element =>{
  console.log(element)
});
}

const apuntesData = () => {
    axios.get('http://127.0.0.1:8000/api/myuser').then(response => {
        response.data.filter(element =>{
          let user = element.user;
          let c_u = $("#plays").html();
          let apuntess = element.apuntes;
          if (user == c_u) {
            userapuntess = apuntess;
            console.log(apuntess);
          }
        });
        Loop2();
        Userapuntess.forEach(element => {
          if ($("option").val()){
            $("option").removeClass();
          }

        })
      });
};
const sendData = () => {
    axios.post('http://127.0.0.1:8000/api/notas');
}

apuntesData();





/*
$("option").addClass(function() {
   let option = $(this).val();
   if (option == user_apuntess){
     $(this).removeClass();
   }});
*/
    





//getData();


$('#apuntes').css("background-color", "lightgray");
$('#apuntes').css("color", "black");
$('#apuntes').hide();
$('#apuntes').show(400);


//getNote.addEventListener('click', getData);