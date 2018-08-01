Filter_Poms_App = function () {

    let pomodoros = [];
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
            console.log(that.pomodoros);

            $(document).ready(function () {
                that.table = $('#pom-table').DataTable({
                    columnDefs: [
                        {
                            name: "Date"
                        },
                        {
                            name: "Title"
                        },
                        {
                            name: "Flags"
                        },
                        {
                            name: "Start Time"
                        },
                        {
                            name: "End Time"
                        },
                        {
                            name: "Distractions"
                        },
                        {
                            name: "Pom Success"
                        },
                        {
                            name: "Description"
                        }
                    ]
                });

                _.each(that.pomodoros, function (value, key) {
                    that.table.row.add([
                        value.created,
                        value.task,
                        '', // TODO: Need to retrieve and add flags still
                        value.start_time,
                        value.end_time,
                        value.distractions,
                        value.pom_success,
                        value.review
                    ]).draw(false);
                });
            });
        },

        error: function (jqXHR, textStatus, errorThrown) {
            // Runs when any error is returned

            // console.log('error');
            // console.log(jqXHR);
            // console.log(textStatus);
            // console.log(errorThrown);
        }
    });

     let Pomodoro = new function () {

        let Model = Backbone.Model.extend({
            // The initialize function is called when an instance is created
            initialize: function () {
                console.log("A new pomodoro has been created.");
            }
        });

        let Collection = Backbone.Collection.extend({
            model: this.Model
        });

        let View = Backbone.View.extend({

            tagName: "div"
        });
    };

    let Filters = new function () {

        let Model = Backbone.Model.extend({
            // The initialize function is called when an instance is created
            initialize: function () {
                console.log("A new pomodoro has been created.");
            }
        });

        let View = Backbone.View.extend({

            tagName: "div",

            events: {
                "click .success_filter": "onClickSuccessFilter",
                "click .distractions_filter": "onClickDistractionsFilter"
            },

            onClickSuccessFilter: function (e) {
                // We can stop this event from being passed to any other handler in the chain
                e.stopPropagation();
                // that.table.clear();
                console.log(e);
                if (e.currentTarget.checked) {
                    _.each(that.pomodoros, function (value, key) {
                        table.rows().every(function (rowIdx, tableLoop, rowLoop) {
                            let data = this.data();
                            let row = that.table.row($(this).parents('tr'));
                            console.log(data);
                            row.remove();
                            that.table.draw();
                        });
                        //         if (value.pom_success === 1) {
                        //             that.table.row.add([
                        //                 value.created,
                        //                 value.task,
                        //                 '', // TODO: Need to retrieve and add flags still
                        //                 value.start_time,
                        //                 value.end_time,
                        //                 value.distractions,
                        //                 value.pom_success,
                        //                 value.review
                        //             ]).draw(false);
                        //         }
                        //     });
                        // } else {
                        //     _.each(that.pomodoros, function (value, key) {
                        //         if (value.pom_success === 0) {
                        //             that.table.row.add([
                        //                 value.created,
                        //                 value.task,
                        //                 '', // TODO: Need to retrieve and add flags still
                        //                 value.start_time,
                        //                 value.end_time,
                        //                 value.distractions,
                        //                 value.pom_success,
                        //                 value.review
                        //             ]).draw(false);
                        //         }
                    });
                    that.table.draw();
                }

                console.log("Success Filter Clicked");
            },

            onClickDistractionsFilter: function (e) {
                // We can stop this event from being passed to any other handler in the chain
                e.stopPropagation();
                that.table.clear();
                _.each(that.pomodoros, function (value, key) {
                    if (value.distractions !== 0) {
                        that.table.row.add([
                            value.created,
                            value.task,
                            '', // TODO: Need to retrieve and add flags still
                            value.start_time,
                            value.end_time,
                            value.distractions,
                            value.pom_success,
                            value.review
                        ]).draw(false);
                    }
                });
                that.table.draw();

                console.log("Distractions Filter Clicked");
            }
        });

        this.Component = Backbone.View.extend({
            initialize: function () {
                this.model = new Model();
                this.view = new View();

                this.model.listenTo(this.view, 'click:clear', this.model.reset);
                this.model.listenTo(this.view, 'click:group', this.model.set_groups);
                this.model.listenTo(this.view, 'click:state', this.model.set_states);
                this.model.listenTo(this.view, 'click:incomplete', this.model.set_incomplete);
                this.model.listenTo(this.view, 'change:type', this.model.set_type);
                this.model.listenTo(this.view, 'change:search', this.model.set_search);
                this.view.listenTo(this.model, 'change', this.view.on_change_model);

                this.listenTo(this.model, 'change', _.partial(this.trigger, 'change', _));
                this.listenTo(this.view, 'click:clear', _.partial(this.trigger ,'click:clear'));
            }
        });
    };

    this.Application = Backbone.View.extend({
        initialize: function () {
            this.filters = new Filters.Component();
            this.pomodoro = new Pomodoro.Component();
        }
    });

    let app = new Application();
}();