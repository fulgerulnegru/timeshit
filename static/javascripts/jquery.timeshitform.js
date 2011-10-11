function showErrorsInForm(form, errors) {
  for (i = 0; i < errors.length; ++ i) {
    var field = errors[i][0];
    var message = errors[i][1];
    var input = $(form).find('input[name=' + field + '], select[name=' + field + ']');
    console.log(input);
    var help = '<label for="field_' + field + 
                    '" generated="true" class="error" style="display: inline; ">' + 
                    message + '</label>';
    $(input).next('label.error').remove();
    $(input).after($(help));
  }
}

(function( $ ){
  $.fn.timeshitForm = function(options, trueRedirect) {
    console.log(this);
    trueRedirect && $(this).addClass("trueRedirect");
    this.ajaxForm({
      beforeSubmit: function (formData, jqForm, options) {
        console.log(formData);
        var disabled = $(jqForm).hasClass('disabled');
        if (disabled) {
          return false;
        } else {
          if (! $(jqForm).valid())
            return false;
          if ($(jqForm).hasClass("trueRedirect"))
            return true;
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
            if ($form.hasClass("trueRedirect")) {
              window.location.href = response.object.redirectUrl;
            } else {
              window.location.hash = BASE_URL + "#!" + response.object.redirectUrl;
              $($form).parents('.wizard').remove();
            }
          } else {
            showErrorsInForm($form, response.object);
          }
        }
      }
    }).validate(options);
  }
})( jQuery );
