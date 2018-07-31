let filter_poms = (function () {

    this.pomodoros = [];
    let that = this;

    $.ajax({
        url: '/api/poms',
        type: 'GET',
        cache: false,
        dataType: 'json',
        contentType: 'application/json',
        success: function (data, textStatus, jqXHR) {
            // Runs only when a 200 OK is returned
            // console.log('success');
            // console.log(data);
            that.pomodoros = data;
        },
        error: function (jqXHR, textStatus, errorThrown) {
            // Runs when any error is returned

            // console.log('error');
            // console.log(jqXHR);
            // console.log(textStatus);
            // console.log(errorThrown);
        }
    });

    let pomodoro = Backbone.Model.extend({
        // The initialize function is called when an intance is created
        initialize: function () {
            console.log("A new pomodoro has been created.");
        }
    });

    // _.each(pomodoros, function (value, key) {
    //     console.log(key + ": " + value);
    // });

    $(document).ready(function () {
        $('#pom-table').DataTable({
            autoWidth: false,
            columnDefs: [
                {
                    name: "derp",
                    className: 'wrap',
                    data: 'agentFacilityName',
                    render: function (data, type, full) {
                        return data +' ('+ row[3]+')';
                    }
                },
                {
                    name: "derp",
                    className: 'wrap',
                    data: 'agentFacilityName',
                    render: function (data, type, full) {
                        return data +' ('+ row[3]+')';
                    }
                }
            ]
        });
    });
}());