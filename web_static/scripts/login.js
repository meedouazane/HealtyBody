$(document).ready(function () {
    // Function to determine the current protocol
    function getCurrentProtocol() {
        return window.location.protocol;
    }

    $('#signup-form').submit(function (event) {
        event.preventDefault();
        const protocol = getCurrentProtocol(); // Get the current protocol
        const url = protocol + '//healtybody.onrender.com/users/add/'; // Use the current protocol in the URL
        $.ajax({
            method: 'POST',
            url: url,
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
        const protocol = getCurrentProtocol(); // Get the current protocol
        const username = $('#username1').val();
        let password = $('#password1').val();
        password = md5(password)
        console.log(password)

        const url = protocol + '//healtybody.onrender.com/users/';
        $.ajax({
            method: 'GET',
            url: url,
            dataType: 'html',
            contentType: 'application/x-www-form-urlencoded',
            data: {
                username: username,
                password: password
            },
            success: function (response) {
                const redirectUrl = protocol + '//healtybody.onrender.com/users/?username=' + encodeURIComponent(username) + '&password=' + encodeURIComponent(password);
                window.location.href = redirectUrl;
            },
            error: function () {
                $('#login_user').text('Invalid username or password');
            },
        });
    });
});
