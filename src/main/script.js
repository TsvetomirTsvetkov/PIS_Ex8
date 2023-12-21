document.getElementById('registrationForm').addEventListener('submit', function(event) {
      var email = document.getElementById('email').value;
      var password = document.getElementById('password').value;

      if (!validateEmail(email)) {
        alert("Please enter a valid email address");
        event.preventDefault();
      }

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

    function validateEmail(email) {
      // Basic email validation with regular expression
      if (email.includes('@') && email.includes('.')) {
        var atIndex = email.indexOf('@');
        var dotIndex = email.lastIndexOf('.');
        var spaceIndex = email.indexOf(' ');

        // Check if '@' appears before '.'
        if (atIndex < dotIndex) {
          // Check if there's only one '@'
          if (email.indexOf('@', atIndex + 1) === -1) {
            // Check if there's no space in the email
            if (spaceIndex === -1) {
              return "Valid email";
            } else {
              return "Invalid email: Contains space";
            }
          } else {
            return "Invalid email: Multiple '@' symbols";
          }
        } else {
          return "Invalid email: '.' appears before '@'";
        }
    } else {
      return "Invalid email: Missing '@' or '.'";
    }
    }