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

            location.reload();
        },
        error: function (jqXHR, textStatus, errorThrown) {
            // Runs when any error is returned
            // TODO: Check responseJSON
            console.log(jqXHR.responseText);
            if (errorThrown === 'Bad Request') {
                $.ajax({
                    url: '/app/pom_exists',
                    type: 'get',
                    cache: false,
                    dataType: 'html',
                    contentType: 'text/html',
                    data: data,
                    success: function (data, textStatus, jqXHR) {
                        // Runs only when a 200 OK is returned

                        // console.log(data);
                    }
                });
            }
        },
        complete: function (jqXHR, textStatus) {
            // Runs whether or not an error is returned
        }
    });
}

$(document).ready(function () {
    $('form.pom-form').on('submit', function (e) {
        e.preventDefault();
    });
});