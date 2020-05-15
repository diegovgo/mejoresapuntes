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


  function openArchiveForm() {
    document.getElementById("archivosForm").style.display = "block";
  }
  
  function closeArchiveForm() {
    document.getElementById("archivosForm").style.display = "none";
  }


/*  const titles = []

var userCourses;

let Loop = () => {
  for (var i = 0 ; i < userCourses.length; i++) {
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

const CourseData = () => {
    axios.get('http://127.0.0.1:8000/api/myuser').then(response => {
        response.data.filter(element =>{
          let user = element.user;
          let c_u = $("#plays").html();
          let courses = element.course;
          if (user == c_u) {
            userCourses = courses;
            console.log(courses);
          }
        });
        Loop2();
        UserCourses.forEach(element => {
          if ($("option").val()){
            $("option").removeClass();
          }

        })
      });
};
const sendData = () => {
    axios.post('http://127.0.0.1:8000/api/notas');
}

CourseData();





/*
$("option").addClass(function() {
   let option = $(this).val();
   if (option == user_courses){
     $(this).removeClass();
   }});
*/
    





//getData();


$('#apuntes').removeClass();
$('#apuntes').addClass("nav-item active");
$('#apuntes').css("background-color", "lightgray");
$('#apuntes').hide();
$('#apuntes').show(400);


//getNote.addEventListener('click', getData);