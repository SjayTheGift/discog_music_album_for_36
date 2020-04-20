$(document).ready(function() {
    var register_form = $('#register_form');
    var login_form = $('#login_form');

    //Register form
    register_form.on('submit', function(event) {
      event.preventDefault();
        $.ajax({
              type: 'POST',
              url: 'http://127.0.0.1:8000/rest-auth/registration/',
              data: {
                    email : $("#email").val(),
                    password1 : register_form.find('input[name="password1"]').val(),
                    password2 : register_form.find('input[name="password2"]').val(),
                    csrfmiddlewaretoken : register_form.find('input[name="csrfmiddlewaretoken"]').val(),
              },
              dataType: 'json',

              success : function(data){
                    window.location = "/signup/";
              },

              error : function(data){
                    $.each(data.responseJSON, function (key, value) {
                        let input = '#register_form input[name=' + key + ']';
                        $(input).addClass( "is-invalid" );
                        $(input).siblings("span").append("<p>" + value+ "</p>").css("color", "red")

                        if (key === "non_field_errors"){
                            let input2 = '#register_form input[name=password1]';
                            let input3 = '#register_form input[name=password2]';
                            $(input2).addClass( "is-invalid" );
                            $(input2).siblings("span").append("<p>" + value+ "</p>")
                            $(input3).addClass( "is-invalid" );
                        }
                    });

                    register_form.trigger("reset");

              },
         });

    });



    //Login form
    login_form.on('submit', function(event) {
      event.preventDefault();
        $.ajax({
              type: 'POST',
              url: 'http://127.0.0.1:8000/rest-auth/login/',
              data: {
                    email : $("#email").val(),
                    password : login_form.find('input[name="password"]').val(),
                    csrfmiddlewaretoken : login_form.find('input[name="csrfmiddlewaretoken"]').val(),
              },
              dataType: 'json',

              success : function(data){
                    window.location = "/albums/";
              },

              error : function(data){
                    $.each(data.responseJSON, function (key, value) {
                        let input = '#login_form input[name=' + key + ']';
                        $(input).addClass( "is-invalid" );
                        $(input).siblings("span").append("<p>" + value+ "</p>").css("color", "red")
                         console.log(key)
                         console.log(value)
                        if (key === "non_field_errors"){
                            let input_email = '#login_form input[name=email]';
                            let input_password = '#login_form input[name=password]';

                            $(input_email).addClass( "is-invalid" );
                            $(input_password).addClass( "is-invalid" );

                            $(input_email).siblings("span").append("<p>" + value+ "</p>").css("color", "red")
                            $(input_password).siblings("span").append("<p>" + value+ "</p>").css("color", "red")
                        }

                  });
              },
         });

    });


    //logout
    $('#logout').click(function(){
        $.ajax({
              type: 'POST',
              data:{
                csrfmiddlewaretoken: $('#logout_form').find('input[name="csrfmiddlewaretoken"]').val(),
              },
              url: '/rest-auth/logout/',
              dataType: 'json',
              success : function(data){
                    window.location = "/logout/";
              },
         });
    });



});