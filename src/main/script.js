document.getElementById('registrationForm').addEventListener('submit', function(event) {
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    // #############################
    // Checks for Email            #
    // #############################

    if (email.length == 0){
      alert("Email cannot be empty");
      event.preventDefault();
    }

    if (email.includes('@') && email.includes('.')) {
      var atIndex = email.indexOf('@');
      var dotIndex = email.lastIndexOf('.');

      if (atIndex < dotIndex) {
          if (email.indexOf('@', atIndex + 1) === -1) {
              if (email.includes(' ')) {
                  alert("Invalid email: Contains space");
              }
          } else {
              alert("Invalid email: Multiple '@' symbols");
          }
      } else {
          alert("Invalid email: '.' appears before '@'");
      }

    } else {
        alert("Invalid email: Missing '@' or '.'");
        event.preventDefault();
    }

    // #############################
    // Checks for Password         #
    // #############################

    if (password.length == 0){
        alert("Password cannot be empty");
        event.preventDefault();
    }

    if (password.length < 8) {
        alert("Password must be at least 8 characters long");
        event.preventDefault();
    }

    if (password.length > 30) {
        alert("Password must be at most 30 characters long");
        event.preventDefault();
    }
});