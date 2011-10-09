function tasks__before_filter() {
  $('.wizard').slideUp(function () {
    $(this).remove();
  });
}


TASKS_VALIDATION_OPTIONS = {
  rules: {
    name: {required: true, maxlength: 64}
  },
  messages: {
    name: {
      required: 'This field is required',
      maxlength: 'This field has max length 64 characters'
    },
  }
};

function tasks__index() {
  tasks__before_filter();  
  $.get(TASKS_INDEX, function (data) {
    var modal = $(data).modal(MODAL_OPTIONS);
  });
}

function tasks__new() {
  tasks__before_filter();
  $.get(TASKS_NEW, function (data) {
    var form = $(data).modal(MODAL_OPTIONS).find('#new-task-form');
    $(form).timeshitForm(TASKS_VALIDATION_OPTIONS);
  });
}

function tasks__create(evt) {
  evt.preventDefault();
  $('#new-task-form').submit();
}

function tasks__edit(id) {
  tasks__before_filter();
  $.get(TASKS_EDIT(id), function(data) {
    var form = $(data).modal(MODAL_OPTIONS).find('#edit-task-form');
    $(form).timeshitForm(TASKS_VALIDATION_OPTIONS);
  });
}

function tasks__update(evt) {
  evt.preventDefault();
  $('#edit-task-form').submit();
}

function tasks__show(id) {
  tasks__before_filter()
  $.get(TASKS_SHOW(id), function(data) {
    $(data).modal(MODAL_OPTIONS);
  });
}

function tasks__delete(id) {
  if (confirm("Are you sure you want to delete it ?")) {
 //   $.get
  }
}

$(document).ready(function() {
  $('#create-task-button').live('click', tasks__create);
  $('#update-task-button').live('click', tasks__update);
});

