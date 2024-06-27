$(document).ready(function(){
  // Desactivar otros checkboxes cuando uno se selecciona
  $('input[type="checkbox"]').on('change', function() {
      $('input[type="checkbox"]').not(this).prop('checked', false);
  });
});


$(document).ready(function() {
  $("#contact-form").validate({
    rules: {
      name : {
        required: true,
        minlength: 3
      },
      email: {
        required: true,
        email: true
      },
      problema: {
          required: true,
      },
      message: {
          required: true,
          minlength: 3
      }
    },
    messages : {
      name: {
        minlength: "el nombre debe tener al menos 3 caracteres"
      },
      email: {
          email: "Debe tener sintaxis de email"
      },
      problema: {
          required: "selecciona el motivo ",
      },
      message: {
          required: "Ingrese el mensaje ",
          minlength: "Largo min 3 caracteres"
      }
    }
  });
});