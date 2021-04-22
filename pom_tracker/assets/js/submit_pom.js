$(document).ready(function () {
    $('form.pom-form').on('submit', function (e) {
        e.preventDefault();

        let form_data = $('form.pom-form').serialize();
        $.ajax({
            url: '/pomodoro/today',
            type: 'POST',
            cache: false,
            dataType: 'html',
            contentType: 'application/x-www-form-urlencoded',
            data: form_data,

            success: function (data, textStatus, jqXHR) {
                location.reload();
            },

            error: function (jqXHR, textStatus, errorThrown) {
                let error_data = null;
                let error_message = null;

                try {
                    error_data = $.parseJSON(jqXHR.responseText).title;
                } catch ($exception) {
                    // Do nothing
                }

                if (error_data && error_data.error) {
                    error_message = error_data.message ? error_data.message : null;
                }

                error_message = error_message ? error_message : errorThrown;

                $('#validation-error').html('Oops!' + error_message).show();
            }
        });
    });
});