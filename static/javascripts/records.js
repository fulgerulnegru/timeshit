function records__toggle(client, project, task, url) {
  console.log(client, project, task);
  var data="task="+task;
  $.ajax({
    url: url,
    data: data,
    type: "post",
    success: function (response) {
      console.log(response);
    }
  });
}

function startTimer() {
  var button = $('#timer-startstop');
  $(button).addClass('started').removeClass('primary').addClass('error')
  $(button).html('Stop');
  $('#timer-body select').attr('disabled', 'disabled');

  var client = $('#timer-client').val();
  var project = $('#timer-project').val();
  var task = $('#timer-task').val();
  records__toggle(client, project, task, RECORDS_START);
}

function stopTimer() {
  var button = $('#timer-startstop');
  $(button).removeClass('started').removeClass('error').addClass('primary')
  $(button).html('Start');
  $('#timer-body select').removeAttr('disabled');
  var client = $('#timer-client').val();
  var project = $('#timer-project').val();
  var task = $('#timer-task').val();
  records__toggle(client, project, task, RECORDS_STOP);
}

function toggleTimer(evt) {
  evt && evt.preventDefault();
  var target = $(evt.target);

  if ($(target).hasClass('started')) {
    stopTimer();
  } else {
    startTimer();
  }
}

function setProjects(client) {
  var options = $('#timer-project option');
  $(options).attr('disabled', 'disabled');
  $(options).removeAttr('selected');

  var active = $('#timer-project option[client=' + client + ']');
  $(active).removeAttr('disabled');
  if ($(active).length) {
    var first = $(active).filter(':first');
    $(first).attr('selected', 'selected');
    setTasks($(first).val());
  } else {
    var task_options = $('#timer-task option');
    $(task_options).attr('disabled', 'disabled');
    $(task_options).removeAttr('selected');
  }
}

function setTasks(project) {
  var options = $('#timer-task option');
  $(options).attr('disabled', 'disabled');
  $(options).removeAttr('selected');

  var active = $('#timer-task option[project=' + project + ']');
  $(active).removeAttr('disabled');
  if ($(active).length) {
    var first = $(active).filter(':first');
    $(first).attr('selected', 'selected');
  }
}

function setTimerFields(evt, initial) {
  var client = $('#timer-client option:selected');
  var project = $('#timer-project option:selected');
  var task = $('#timer-task option:selected');
  if ($(client).val() != $(project).attr('client') || initial) {
    setProjects($(client).val());
  } else if ($(project).val() != $(task).attr('project')) {
    setTasks($(project).val());
  }
}

$(document).ready(function() {
  $('#timer-startstop').click(toggleTimer);
  setTimerFields(undefined, true);
  $('#timer-body select').change(setTimerFields);
});
