function getDateTime() {
  var now = new Date();
  return ("0" + now.getDay()).slice('-2') + '/' + 
         ("0" + now.getMonth()).slice('-2') + '/' + 
         now.getFullYear() +
   " " + ("0" + now.getHours()).slice('-2') + ":" + 
         ("0" + now.getMinutes()).slice('-2') + ":" + 
         ("0" + now.getSeconds()).slice('-2');
}

function wizard_before_filter() {
  $('.wizard').slideUp(function () {
    $(this).remove();
  });
}

function timer__show() {
  wizard_before_filter();
 /* $.get(TIMER_URL, function (data) {
    $(data).modal(MODAL_OPTIONS);
  });*/
}

function setDateTimeToTimer() {
  setTimeout(setDateTimeToTimer, 1000);
  $('#timer-current-time').html(getDateTime());
}

function show_about() {
  wizard_before_filter();
  $.get(ABOUT_URL, function(data) {
    $(data).modal(MODAL_OPTIONS);
  });
}

$(document).ready(function() {
  if (window.location.hash == "")
    window.location.hash = "!/";
  setDateTimeToTimer();
});
