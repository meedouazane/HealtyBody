$(document).ready(function () {
    $('#signup-form').submit(function (event) {
        event.preventDefault();
        const username = $('#username').val();
        const first_name = $('#first_name').val();
        const last_name = $('#last_name').val();
        const email = $('#email').val();
        const sex = $('#Sex').val();
        const password = $('#password').val();

        $.ajax({
            method: 'POST',
            url: 'http://127.0.0.1:5000/users/add/',
            dataType: 'json',
            contentType: 'application/x-www-form-urlencoded',
            data: $('#signup-form').serialize(),
            success: function (json) {
                $('#user_create').text('Your account has been successfully created');
                $('#username').val('');
                $('#first_name').val('');
                $('#last_name').val('');
                $('#email').val('');
                $('#Sex').val('');
                $('#password').val('');
            },
            error: function (json) {
                $('#user_create').text('Error');
            }
        });
    });

    $('#login-form').submit(function (event) {
    event.preventDefault();
    const username = $('#username1').val();
    let password = $('#password1').val();
    password = md5(password)
    console.log(password)

    $.ajax({
        method: 'GET',
        url: 'http://127.0.0.1:5000/users/',
        dataType: 'html',
        contentType: 'application/x-www-form-urlencoded',
        data: {
            username: username,
            password: password
        },
        success: function (response) {
               window.location.href = 'http://127.0.0.1:5000/users/?username=' + encodeURIComponent(username) + '&password=' + encodeURIComponent(password);
        },
        error: function () {
            $('#login_user').text('Invalid username or password');
        },
    });
});
});
