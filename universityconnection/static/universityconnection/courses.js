$('#course').css("background-color", "lightgray");
$('#course').css("color", "black");
$('#course').hide();
$('#course').show(400);

var u = $("#plays").text();
/*for (i = 0; i < )
var x = document.getElementsByClassName("course-title")[0].getAttribute("value");
console.log(x);



/*var aaa = [1,1,2,2,2,3];

for (var i = 0; i<=1; i++){
    var x = document.getElementsByClassName("course-title-id")[i].id;
    var y = document.getElementsByClassName("course-title-id")[i];
}


const getUserData = () => {
    axios.get('http://127.0.0.1:8000/api/myuser/').then(response => {
        response.data.map(element => {
            let user = element.user;
            let title = element.title;
            let course = element.course;
            let current_user_id = u;
            let text = "<div class='titleCourse'><h3>" + course + "</h3></div>";
            if (user == current_user_id) {
                let filterCourse = course;

            }
        });
    });
};

getUserData();

var fc = [];

const getFiles = () => {
    axios.get('http://127.0.0.1:8000/api/files').then(response => {
        response.data.map(element => {
                let title = element.title;
                let course = element.course;
                //console.log(course);
                fc.push(course);
            });
        });
};


getFiles();


var aa = [];

$(".course-title-id").html(function () {
var a = $(this).html();
aa.push(a);
//console.log(a);
if (a == fc) {
    
};
console.log("vamos");
});

const getTest = () => {
    axios.get('http://127.0.0.1:8000/api/files').then(response => {
        response.data.map(element =>{
            let course = element.course;
            let title = element.title;
            let c_id = $(".course-title-id").html();
            console.log(title);
            if (c_id == course){
                $(".course-title").append(title);
            }
        });
    });
}


//getTest();


for (var i=0; i < aa.length; i++){
    ax = aa[i];
if (fc == ax) {
      console.log("exito");
    }
else {
        console.log("not");
    }
}

/*
const getFileData = () => {
    axios.get('http://127.0.0.1:8000/api/files').then(response => {
        response.data.map(element =>{
          let title = element.title;
          let course = element.course;
          //console.log(course);
          //if (ct == course)
        
          //if (user == current_user_id){
            //$('#displayall').append(text);
          //}  
        });
    });
};

getFileData();*/

