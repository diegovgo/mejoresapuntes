const getUniversityData = () => {
    axios.get('https://mejoresapuntes1.herokuapp.com/api/university/').then(response => {
        response.data.map(element => {
            let name = element.name;
            let u_id = element.id;
            let text = "<option value='" + u_id + "'>" + name + "</option>";
            $("select[name='universities']").append(text);
        });
    });
};

$("select[name='university']").change(
    console.log($("select[name='university']").val())
);

$("select[name='university']").change(function () {
    $("select[name='course']").empty();
    $("select[name='career']").empty();
    axios.get('https://mejoresapuntes1.herokuapp.com/api/career/').then(response => {
        response.data.map(element => {
            let name = element.name;
            let u_id = element.university;
            let id = element.id;
            let c_u_id = $("select[name='university']").val();
            CurrentUniversityID = c_u_id;
            let text = "<option value='" + id + "'>" + name + "</option>";
            if (c_u_id == u_id) {
                $("select[name='career']").append(text);
                console.log(name, u_id, c_u_id)
            }
        });
    });
    $('#genderSpan').html($(this).val());
});

var CurrentCareerID;

$("select[name='career']").change(function () {
    $("select[name='course']").empty();
    axios.get('https://mejoresapuntes1.herokuapp.com/api/cursos/').then(response => {
        response.data.map(element => {
            let id = element.id;
            let name = element.name;
            let career_id = element.career;
            let c_career_id = $("select[name='career']").val();
            CurrentCareerID = c_career_id;
            let text = "<option value='" + id + "'>" + name + "</option>";
            if (c_career_id == career_id) {
                $("select[name='course']").append(text);
            };
        });
    });
});


//getUniversityData();
//



//    