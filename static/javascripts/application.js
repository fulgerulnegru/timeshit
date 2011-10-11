function wizard_before_filter() {
  $('.wizard').slideUp(function () {
    $(this).remove();
  });
}

/*function timer__show() {
  wizard_before_filter();
  $.get(TIMER_URL, function (data) {
    $(data).modal(MODAL_OPTIONS);
  });
}*/

$(document).ready(function() {
  window.location.hash = "!/";
});
