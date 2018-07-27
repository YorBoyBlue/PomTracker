<form class="pom-form">
    <div class="row">
        % if message:
            <div class="alert alert-warning" style="width: 100%">
                <strong>Oops!</strong> ${message}
            </div>
        % endif
        <div class="col-xl-6 col-lg-4 col-md-12 col-sm-12">
            <div class="row">
                <h2>Pomodora:</h2>
            </div>
            <br><br>
            <div class="row">
                <h5 style="padding-top: 5px; margin-right: 5px">Time Block:</h5>
                % if time_block:
                    <select style="width: auto" class="custom-select" name="time_block">
                        % for time in time_blocks:
                            <option ${'selected' if (time == time_block) else ''}>${time}</option>
                        % endfor
                    </select>
                % else:
                    <select style="width: auto" class="custom-select" name="time_block">
                        % for time in time_blocks:
                            <option>${time}</option>
                        % endfor
                    </select>
                % endif
            </div>
            <br><br>
            <div class="row">
                <div style="float: left; margin-right: 30px">
                    <h5>Flags:</h5>
                    % if flags:
                        % for flag in flag_types:
                        <% flag_name = flag[0] %>
                            <input type="checkbox" name="flags"
                                   value="${flag[0]}" ${'checked' if (flag_name in flags) else ''}> ${flag[0]}<br>
                        % endfor
                    % else:
                        % for flag in flag_types:
                            <input type="checkbox" name="flags" value="${flag[0]}"> ${flag[0]}<br>
                        % endfor
                    %  endif
                </div>
                <div class="distractions">
                    <h5>Distractions:</h5>
                    % if distractions:
                        <input class="distractions_check top" type="checkbox" name="distractions"
                               value="1" ${'checked' if ('1' in distractions) else ''}>
                        <input class="distractions_check" type="checkbox" name="distractions"
                               value="2" ${'checked' if ('2' in distractions) else ''}><br>
                        <input class="distractions_check middle" type="checkbox" name="distractions"
                               value="3" ${'checked' if ('3' in distractions) else ''}><br>
                        <input class="distractions_check bottom" type="checkbox" name="distractions"
                               value="4" ${'checked' if ('4' in distractions) else ''}>
                        <input class="distractions_check" type="checkbox" name="distractions"
                               value="5" ${'checked' if ('5' in distractions) else ''}>
                    % else:
                        <input class="distractions_check top" type="checkbox" name="distractions" value="1">
                        <input class="distractions_check" type="checkbox" name="distractions" value="2"><br>
                        <input class="distractions_check middle" type="checkbox" name="distractions" value="3"><br>
                        <input class="distractions_check bottom" type="checkbox" name="distractions" value="4">
                        <input class="distractions_check" type="checkbox" name="distractions" value="5">
                    % endif
                </div>
            </div>
        </div>
        <div class="col-xl-6 col-lg-8 col-md-12 col-sm-12 form-text">
            <div class="row">
                <h5 class="title">Title:</h5>
                % if task:
                    <textarea rows="3" cols="50" type='text' name='task'>${task}</textarea>
                % else:
                    <textarea rows="3" cols="50" type='text' name='task'></textarea>
                % endif
                <h5 style="margin-top: 10px">Description:</h5>
                % if review:
                    <textarea rows="6" cols="50" type='text' name='review'>${review}</textarea>
                % else:
                    <textarea rows="6" cols="50" type='text' name='review'></textarea>
                % endif
            </div>
            <br>
            <div class="row">
                <div class="col-xl-8 col-lg-8 col-md-8 col-sm-6" style="padding-left: 0">
                    % if pom_success:
                        <input style="margin-top: 5px; margin-right: 5px" type="checkbox" name="pom_success"
                               value="1" ${'checked' if (pom_success == '1') else ''}> Was this pom successful? <br>
                    % else:
                        <input style="margin-top: 5px; margin-right: 5px" type="checkbox" name="pom_success"
                               value="1"> Was this pom successful? <br>
                    % endif
                </div>
                <div class="col-xl-4 col-lg-4 col-md-4 col-sm-6" style="padding-right: 0">
                    <input style="width: 170px" class="btn btn-primary main-button float-right" role="button"
                           value='Submit Pomodora' onclick="submitPom()">
                </div>
            </div>
        </div>
    </div>
</form>