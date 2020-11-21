$(document).ready(function(){
  $('.ui.dropdown').dropdown();
});

function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}

$(document).ready(function() {
  $('#bot').submit(function(event) {
    var formData = {
        'message': $('#msg').val()
    };
    $('.chats').append('<div class="ui container grid"> <div class="right floated eight wide column"><div class="ui floating message"><p>' + $('#msg').val() + '</p></div></div></div>');
    $('#msg').val('')
    $.ajax({
        type        : 'POST', // define the type of HTTP verb we want to use (POST for our form)
        url         : '/bot-message/', // the url where we want to POST
        data        : formData,
        dataType    : 'json', // what type of data do we expect back from the server
        encode      : true
    })
    .done(function(data) {
        for (var i=0; i<data.messages.length; i++) {
            $('.chats').append('<div class="ui container grid"> <div class="left floated eight wide column"><div class="ui floating message"><p>' + data.messages[i] + '</p></div></div></div>');
        }
    });
    // stop the form from submitting the normal way and refreshing the page
    event.preventDefault();
  });
});