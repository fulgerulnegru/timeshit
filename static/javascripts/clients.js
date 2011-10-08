function clients__before_filter() {
  $('.wizard').slideUp(function () {
    console.log(this);
    $(this).remove();
  });
  $('.modal-backdrop').slideUp(function () {
    $(this).remove();
  });
}


CLIENTS_VALIDATION_OPTIONS = {
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

function clients__index() {
  clients__before_filter();  
  $.get(CLIENTS_INDEX, function (data) {
    var modal = $(data).modal(MODAL_OPTIONS);
  });
}

function clients__new() {
  clients__before_filter();
  $.get(CLIENTS_NEW, function (data) {
    var form = $(data).modal(MODAL_OPTIONS).find('#new-client-form');
    $(form).timeshitForm(CLIENTS_VALIDATION_OPTIONS);
  });
}

function clients__create(evt) {
  evt.preventDefault();
  $('#new-client-form').submit();
}

function clients__edit(id) {
  clients__before_filter();
  $.get(CLIENTS_EDIT(id), function(data) {
    var form = $(data).modal(MODAL_OPTIONS).find('#edit-client-form');
    $(form).timeshitForm(CLIENTS_VALIDATION_OPTIONS);
  });
}

function clients__update(evt) {
  evt.preventDefault();
  $('#edit-client-form').submit();
}

function clients__show(id) {
  clients__before_filter()
  $.get(CLIENTS_SHOW(id), function(data) {
    $(data).modal(MODAL_OPTIONS);
  });
}

function clients__delete(id) {
  if (confirm("Are you sure you want to delete it ?")) {
    $.get
  }
}

$(document).ready(function() {
  $('#create-client-button').live('click', clients__create);
  $('#update-client-button').live('click', clients__update);
});

