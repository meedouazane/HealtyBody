$(document).ready(function () {
    // Function to get the base URL dynamically
    function getBaseUrl() {
        // Get the current hostname and port
        var host = window.location.hostname;
        var port = window.location.port;
        // Construct the base URL
        var baseUrl = 'http://' + host;
        if (port) {
            baseUrl += ':' + port;
        }
        return baseUrl;
    }

    $('#signup-form').submit(function (event) {
        event.preventDefault();
        const baseUrl = getBaseUrl(); // Get the base URL
        $.ajax({
            method: 'POST',
            url: baseUrl + '/users/add/', // Construct the URL using the base URL
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
        const baseUrl = getBaseUrl(); // Get the base URL
        const username = $('#username1').val();
        let password = $('#password1').val();
        password = md5(password)
        console.log(password)

        $.ajax({
            method: 'GET',
            url: baseUrl + '/users/',
            dataType: 'html',
            contentType: 'application/x-www-form-urlencoded',
            data: {
                username: username,
                password: password
            },
            success: function (response) {
                window.location.href = baseUrl + '/users/?username=' + encodeURIComponent(username) + '&password=' + encodeURIComponent(password);
            },
            error: function () {
                $('#login_user').text('Invalid username or password');
            },
        });
    });
});
