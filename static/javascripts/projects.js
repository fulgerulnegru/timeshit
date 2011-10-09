function projects__before_filter() {
  $('.wizard').slideUp(function () {
    $(this).remove();
  });
  $('.modal-backdrop').slideUp(function () {
    $(this).remove();
  });
}


PROJECTS_VALIDATION_OPTIONS = {
  rules: {
    name: {required: true, maxlength: 64},
    project: {required: true}
  },
  messages: {
    name: {
      required: 'This field is required',
      maxlength: 'This field has max length 64 characters'
    },
    project: {
      required: 'This field is required',
    }
  }
};

function projects__index() {
  projects__before_filter();  
  $.get(PROJECTS_INDEX, function (data) {
    var modal = $(data).modal(MODAL_OPTIONS);
  });
}

function projects__new() {
  projects__before_filter();
  $.get(PROJECTS_NEW, function (data) {
    var form = $(data).modal(MODAL_OPTIONS).find('#new-project-form');
    $(form).timeshitForm(PROJECTS_VALIDATION_OPTIONS);
  });
}

function projects__create(evt) {
  evt.preventDefault();
  $('#new-project-form').submit();
}

function projects__edit(id) {
  projects__before_filter();
  $.get(PROJECTS_EDIT(id), function(data) {
    var form = $(data).modal(MODAL_OPTIONS).find('#edit-project-form');
    $(form).timeshitForm(PROJECTS_VALIDATION_OPTIONS);
  });
}

function projects__update(evt) {
  evt.preventDefault();
  $('#edit-project-form').submit();
}

function projects__show(id) {
  projects__before_filter()
  $.get(PROJECTS_SHOW(id), function(data) {
    $(data).modal(MODAL_OPTIONS);
  });
}

function projects__delete(id) {
  if (confirm("Are you sure you want to delete it ?")) {
 //   $.get
  }
}

$(document).ready(function() {
  $('#create-project-button').live('click', projects__create);
  $('#update-project-button').live('click', projects__update);
});

