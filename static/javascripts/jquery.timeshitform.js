(function( $ ){
  $.fn.timeshitForm = function(options) {
    this.ajaxForm({
      beforeSubmit: function (formData, jqForm, options) {
        console.log(formData);
        var disabled = $(jqForm).hasClass('disabled');
        if (disabled) {
          return false;
        } else {
          if (! $(jqForm).valid())
            return false;
          $(jqForm).addClass("disabled");
          return true;
        }
      },
      success: function (response, status, xhr, $form) {
        console.log(status);
        console.log($form);
        if (status == "success") {
          console.log(response);
          response = $.parseJSON(response);
          if (response.code == 0) {
            console.log(response.object.redirectUrl);
            window.location.hash = BASE_URL + "#!" + response.object.redirectUrl;
            $($form).parents('.wizard').remove();
          } else {
            // show errors
          }
        }
      }
    }).validate(options);
  }
})( jQuery );
