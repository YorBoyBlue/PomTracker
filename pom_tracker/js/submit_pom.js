$(document).ready(function () {
    $('form.pom-form').on('submit', function (e) {
        e.preventDefault();
    });
});

function submitPom() {
    let data = $('form.pom-form').serialize();
    $.ajax({
        url: '/api/poms',
        type: 'post',
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
            console.log(error_data.data['form_data']);
            if (error_data.error === 'PomExistsError') {
                $.ajax({
                    url: '/app/pom_exists',
                    type: 'post',
                    cache: false,
                    dataType: 'html',
                    contentType: 'text/html',
                    data: error_data.data,
                    processData: false,
                    success: function (data, textStatus, jqXHR) {
                        // Runs only when a 200 OK is returned
                        $('form.pom-form').replaceWith(data);
                        // console.log('success');
                    },
                    error: function (jqXHR, textStatus, errorThrown) {
                        // console.log('error');
                    }
                });
            }
            if (error_data.error === 'ValidationError') {
                $.ajax({
                    url: '/app/pom_exists',
                    type: 'post',
                    cache: false,
                    dataType: 'html',
                    contentType: 'text/html',
                    data: error_data.data,
                    processData: false,
                    success: function (data, textStatus, jqXHR) {
                        // Runs only when a 200 OK is returned
                        $('form.pom-form').replaceWith(data);
                        // console.log('success');
                    },
                    error: function (jqXHR, textStatus, errorThrown) {
                        // console.log('error');
                    }
                });
            }
        },
        complete: function (jqXHR, textStatus) {
            // Runs whether or not an error is returned
        }
    });
}