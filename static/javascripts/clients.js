function clients__index() {
  $.get(CLIENTS_INDEX, function (data) {
    var modal = $(data).modal(MODAL_OPTIONS);
  });
}

function clients__new() {
  $.get(CLIENTS_NEW, function (data) {
    $(data).modal(MODAL_OPTIONS);
  });
}

