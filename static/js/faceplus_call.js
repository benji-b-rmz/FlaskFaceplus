/**
 * Created by benji on 5/30/17.
 */


function clear() {
    $('#faceplus-age').html("");
    $('#faceplus-gender').html("");
    $('#faceplus-race').html("");
    $('#faceplus-glasses').html("");
    $('#faceplus-smiling').html("");
}

$(document).on('click','#submit',function () {

    console.log("clicked on submit!");
    var words = $('#input-url');
    console.log(words);
    //set output to processing gif while we wait for response
    var gif =  "<div class='text-center'> Processing...<br/><img class='text-center' src='https://railsgirlssummerofcode.org/img/blog/2016/l1ghtsab3r-partyparrot.gif'/> </div>";
    $("#faceplus-image").html(gif);
    $.ajax({
        url:'/api/faceplus',
        method: 'POST',
        contentType: 'text/plain',
        data: words,
        success: function(result){
            var response = JSON.parse(result);
            console.log(response);
            if( response.message == "success"){
                $('#faceplus-image').html(
                    '<img src="' + response.url + '" class="response-img"/>'
                );
                $('#faceplus-age').html("<h4>Age: "+response.face[0].attribute.age.value+"</h4>");
                $('#faceplus-gender').html("<h4>Gender: "+response.face[0].attribute.gender.value+"</h4>");
                $('#faceplus-race').html("<h4>Race: "+response.face[0].attribute.race.value+"</h4>");
                $('#faceplus-glasses').html("<h4>Glasses: "+response.face[0].attribute.glass.value+"</h4>");
                $('#faceplus-smiling').html("<h4>Smiling: "+response.face[0].attribute.smiling.value+"</h4>");
            } else if ( response.message == "failed"){
                $('#faceplus-image').html("Something went wrong");
                clear();
            } else {
                $('#faceplus-image').html("Nope");
                clear();
            }
            $("#faceplus-age").html();
        }
    });
});
