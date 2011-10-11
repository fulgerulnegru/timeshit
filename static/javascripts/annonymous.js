LOGIN_VALIDATION_OPTIONS = {
  rules: {
    'email': {required: true},
    'password': {required: true}
  },
  messages: {
    email: {
      required: 'Please enter an email'
    },
    password: {
      required: 'Please enter a password'
    }
  }
};

function assignValidations() {
  $('#login-form').timeshitForm(LOGIN_VALIDATION_OPTIONS, trueRedirect = true);
}

$(document).ready(function () {
  assignValidations();
});
