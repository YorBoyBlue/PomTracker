$(document).ready(function () {
    $('form.pom-form').on('submit', function (e) {
        e.preventDefault();
    });
});

function submitPom() {
    let data = $('form.pom-form').serialize();
    console.log(data);
    $.ajax({
        url: '/api/poms',
        type: 'POST',
        cache: false,
        dataType: 'html',
        contentType: 'application/x-www-form-urlencoded',
        data: data,
        success: function (data, textStatus, jqXHR) {
            // Runs only when a 200 OK is returned
            // Reload page when pom was submitted successfully
            location.reload();
        },
        error: function (jqXHR, textStatus, errorThrown) {
            // Runs when any error is returned

            let error_data = $.parseJSON(jqXHR.responseText).title;
            console.log(error_data);
            console.log(error_data.data);
            console.log(error_data.data.form_data);
            $.ajax({
                url: '/app/pom_exists',
                type: 'POST',
                cache: false,
                dataType: 'html',
                contentType: 'application/json',
                processData: false,
                data: JSON.stringify(error_data.data),
                success: function (data, textStatus, jqXHR) {
                    // Runs only when a 200 OK is returned
                    $('form.pom-form').replaceWith(data);
                    // console.log('success');
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    // console.log('error');
                }
            });
        },
        complete: function (jqXHR, textStatus) {
            // Runs whether or not an error is returned
        }
    });
}