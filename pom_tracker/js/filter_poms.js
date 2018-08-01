Filter_Poms_App = function () {

    let that = this;
    let pomodoros = [];
    let table = null;

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
            let d = Object.values(data);
            console.log(d);
            that.pomodoros = Object.values(data);
            console.log(that.pomodoros);

            $(document).ready(function () {
                that.table = $('#pom-table').DataTable({
                    // data: that.pomodoros,
                    columns: [
                        {
                            title: "Date"
                        },
                        {
                            title: "Title"
                        },
                        {
                            title: "Flags"
                        },
                        {
                            title: "Start Time"
                        },
                        {
                            title: "End Time"
                        },
                        {
                            title: "Distractions"
                        },
                        {
                            title: "Pom Success"
                        },
                        {
                            title: "Description"
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
            defaults: {
                date: "",
                title: "",
                flags: "",
                start_time: "",
                end_time: "",
                distractions: "",
                pom_success: "",
                description: ""
            },
            // The initialize function is called when an instance is created
            initialize: function () {
                console.log("A new pomodoro has been created.");
            }
        });

        let Collection = Backbone.Collection.extend({
            model: Model
        });

        let View = Backbone.View.extend({

            tagName: "div"
        });

        this.Component = Backbone.View.extend({
            initialize: function () {
                this.model = new Model();
                this.view = new View();

                // this.model.listenTo(this.view, 'click:clear', this.model.reset);
                // this.model.listenTo(this.view, 'click:group', this.model.set_groups);
                // this.model.listenTo(this.view, 'click:state', this.model.set_states);
                // this.model.listenTo(this.view, 'click:incomplete', this.model.set_incomplete);
                // this.model.listenTo(this.view, 'change:type', this.model.set_type);
                // this.model.listenTo(this.view, 'change:search', this.model.set_search);
                // this.view.listenTo(this.model, 'change', this.view.on_change_model);
                //
                // this.listenTo(this.model, 'change', _.partial(this.trigger, 'change', _));
                // this.listenTo(this.view, 'click:clear', _.partial(this.trigger, 'click:clear'));
            }
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
            el: "#filters",

            tagName: "div",

            events: {
                "click .success_filter": "onClickSuccessFilter",
                "click .distractions_filter": "onClickDistractionsFilter"
            },

            onClickSuccessFilter: function (e) {
                // We can stop this event from being passed to any other handler in the chain
                e.stopPropagation();
                if (e.currentTarget.checked) {
                    console.log("Success Filter On");
                } else {
                    console.log("Success Filter Off");
                }
            },

            onClickDistractionsFilter: function (e) {
                // We can stop this event from being passed to any other handler in the chain
                e.stopPropagation();
                if (e.currentTarget.checked) {
                    console.log("Distractions Filter On");
                } else {
                    console.log("Distractions Filter Off");
                }
            }
        });

        this.Component = Backbone.View.extend({
            initialize: function () {
                this.model = new Model();
                this.view = new View();

                // this.model.listenTo(this.view, 'click:clear', this.model.reset);
                // this.model.listenTo(this.view, 'click:group', this.model.set_groups);
                // this.model.listenTo(this.view, 'click:state', this.model.set_states);
                // this.model.listenTo(this.view, 'click:incomplete', this.model.set_incomplete);
                // this.model.listenTo(this.view, 'change:type', this.model.set_type);
                // this.model.listenTo(this.view, 'change:search', this.model.set_search);
                // this.view.listenTo(this.model, 'change', this.view.on_change_model);
                //
                // this.listenTo(this.model, 'change', _.partial(this.trigger, 'change', _));
                // this.listenTo(this.view, 'click:clear', _.partial(this.trigger, 'click:clear'));
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