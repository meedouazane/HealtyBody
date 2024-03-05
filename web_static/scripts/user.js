$(document).ready(function () {
     $('#logout').click(function() {
        window.location.href = 'http://127.0.0.1:5000/';
    });
    function updateUserInfo(username) {
        $.ajax({
            method: 'GET',
            url: 'http://127.0.0.1:5000/user/info/?username=' + encodeURIComponent(username),
            dataType: 'json',
            contentType: 'application/x-www-form-urlencoded',
            success: function (json) {
                $('#name').html('<p>BMI Chart for : ' + json.first_name + ' ' + json.last_name + '</p>');
            },
            error: function (json) {
                $('#Submit').text('Error');
            }
        });
    }
    const formUsername = $('#bmi-form').data('username');
    const dob = $('#bmi-form').data('dob');
    const today = new Date();
    const birthYear = dob ? new Date(dob).getFullYear() : null;
    const Year = today ? new Date(today).getFullYear() : null;
    updateUserInfo(formUsername);
    $('#bmi-form').submit(function (event) {
        event.preventDefault();
        const weight = $('#Weight').val();
        const height = $('#Height').val();
        const Age = Year - birthYear;
        console.log("Age:", Age);
        const activity = $('#activity').val();
        const bmr = 10 * weight + 6.25 * height - 5 * Age + 5;
        const generalProteinRequirements = 0.8 * weight;
        const proteinRequirementsMuscleBuilding = 1.5 * weight;
        const proteinRequirementsWeightLoss = 1.8 * weight;
        const watered = (33 * weight) / 1000;

        $('#info').html(
            '<h2>Nutritional Information </h2>' +
            '<li>Total Daily Caloric Needs                : ' + bmr.toFixed(2) + ' Kcal</li>' +
            '<li>General Protein Requirements             : ' + generalProteinRequirements.toFixed(2) + ' grams of protein</li>' +
            '<li>Protein Requirements for Muscle Building : ' + proteinRequirementsMuscleBuilding.toFixed(2) + ' grams of protein</li>' +
            '<li>Protein Requirements for Weight Loss     : ' + proteinRequirementsWeightLoss.toFixed(2) + ' grams of protein</li>' +
            '<li>Daily Water Intake                       : ' + watered.toFixed(2) + ' L</li>'
        );
        $.ajax({
            method: 'POST',
            url: 'http://127.0.0.1:5000/users/bmi/?username=' + encodeURIComponent(formUsername) + '&height=' + encodeURIComponent(height) + '&weight=' + encodeURIComponent(weight),
            dataType: 'json',
            contentType: 'application/x-www-form-urlencoded',
            success: function (json) {
               $('#Weight').val('');
               $('#Height').val('');
               $('#Age').val('');
            },
            error: function (json) {
                $('#Submit').text('Error');
            }
        });
        updateUserInfo(formUsername);
    });
});
