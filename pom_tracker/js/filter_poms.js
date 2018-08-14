Filter_Poms_App = function () {

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
            }
        });

        let Collection = Backbone.Collection.extend({

            model: Model,

            fetch: function () {

                let self = this;

                $.ajax({
                    url: "/api/poms",
                    type: "GET",
                    cache: false,
                    dataType: "json",
                    contentType: "application/json",

                    success: function (data, textStatus, jqXHR) {
                        console.log(data);
                        self.set(self.parse(data));
                        self.trigger("init_table");
                    },

                    error: function (jqXHR, textStatus, errorThrown) {
                        // console.log(jqXHR);
                        // console.log(textStatus);
                        console.log(errorThrown);
                    }
                });
            },

            parse: function (data) {
                dataset = [];
                _.each(data, function (value, key) {
                    let flags = "";
                    _.each(value.flags, function (value, key) {
                        flags += (value + "<br>");
                    });
                    dataset.push(
                        {
                            date: value.created,
                            title: value.task,
                            flags: flags,
                            start_time: value.start_time,
                            end_time: value.end_time,
                            distractions: value.distractions,
                            pom_success: value.pom_success,
                            description: value.review
                        }
                    )
                });
                return dataset;
            }
        });

        let View = Backbone.View.extend({
            el: "#pom-table",

            tagName: "table",

            table: null,

            initialize: function () {

                this.table = this.$el.DataTable({
                    columns: [
                        {
                            data: "date",
                            title: "Date"
                        },
                        {
                            data: "title",
                            title: "Title"
                        },
                        {
                            data: "flags",
                            title: "Flags"
                        },
                        {
                            data: "start_time",
                            title: "Start Time"
                        },
                        {
                            data: "end_time",
                            title: "End Time"
                        },
                        {
                            data: "distractions",
                            title: "Distractions"
                        },
                        {
                            data: "pom_success",
                            title: "Pom Success"
                        },
                        {
                            data: "description",
                            title: "Description"
                        }
                    ]
                });
            },

            populate_table: function (pomodoros) {
                this.table.clear();
                this.table.rows.add(pomodoros);
                this.table.draw();
            }
        });

        this.Component = Backbone.View.extend({
            initialize: function () {
                this.model = new Model();
                this.collection = new Collection();
                this.view = new View();
            },

            fetch: function () {
                this.collection.fetch();
            }
        });
    };

    let Filter = new function () {

        let Model = Backbone.Model.extend({

            defaults: {
                date_filter: "",
                success_filter: false,
                distractions_filter: false
            },

            set_date_filter: function (value) {
                this.set("date_filter", value);
            },

            set_success_filter: function () {
                let value = this.get("success_filter");
                let toggle = !value;
                this.set("success_filter", toggle);
            },

            set_distractions_filter: function () {
                let value = this.get("distractions_filter");
                let toggle = !value;
                this.set("distractions_filter", toggle);
            }
        });

        let View = Backbone.View.extend({
            el: "#filters",

            tagName: "div",

            events: {
                "change .date_filter": "onClickDateFilter",
                "click .success_filter": "onClickSuccessFilter",
                "click .distractions_filter": "onClickDistractionsFilter"
            },

            onClickDateFilter: function (e) {
                this.trigger("filter:date", e.currentTarget.value);
            },

            onClickSuccessFilter: function () {
                this.trigger("filter:success");
            },

            onClickDistractionsFilter: function () {
                this.trigger("filter:distractions");
            }
        });

        this.Component = Backbone.View.extend({
            initialize: function () {
                this.model = new Model();
                this.view = new View();

                this.model.listenTo(this.view, "filter:date", this.model.set_date_filter);
                this.model.listenTo(this.view, "filter:success", this.model.set_success_filter);
                this.model.listenTo(this.view, "filter:distractions", this.model.set_distractions_filter);
            }
        });
    };

    this.Application = Backbone.View.extend({
        initialize: function () {
            this.filters = new Filter.Component();
            this.pomodoro = new Pomodoro.Component();

            this.listenTo(this.filters.model, "change", this.execute);
            this.listenTo(this.pomodoro.collection, "init_table", this.init_table);

            this.pomodoro.fetch();
        },

        init_table: function () {
            let pomodoros = _.pluck(this.pomodoro.collection.models, "attributes");
            console.log(pomodoros);
            this.pomodoro.view.populate_table(pomodoros);
        },

        execute: function () {
            let pomodoros = _.pluck(this.pomodoro.collection.models, "attributes");
            let filters = this.filters.model.attributes;
            pomodoros = this.apply_filters(filters, pomodoros);
            this.pomodoro.view.populate_table(pomodoros);
        },

        apply_filters: function (filters, pomodoros) {

            let filtered_pomodoros = pomodoros;

            _.each(filters, function (value, key) {
                switch (key) {
                    case "date_filter":
                        if (value !== "") {
                            filtered_pomodoros = _.filter(filtered_pomodoros, function (o) {
                                return o.date === value;
                            });
                        }
                        break;
                    case "success_filter":
                        if (value === true) {
                            filtered_pomodoros = _.filter(filtered_pomodoros, function (o) {
                                return o.pom_success === 0;
                            });
                        }
                        break;
                    case "distractions_filter":
                        if (value === true) {
                            filtered_pomodoros = _.filter(filtered_pomodoros, function (o) {
                                return o.distractions > 0;
                            });
                        }
                        break;
                    default:
                        console.log("ERROR: Bad Filter Name!");
                }
            });

            return filtered_pomodoros;
        }
    });

    let app = new Application();
}();
