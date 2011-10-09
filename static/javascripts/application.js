$(document).ready(function() {
  $('.modal').live('hidden', function (evt) {
    console.log("okay");
    window.location.hash = "!/";
  })
});
