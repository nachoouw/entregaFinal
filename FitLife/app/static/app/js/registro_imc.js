// notacion abreviada
$(function () {
  $("#submit-form").click(function (event) {
    event.preventDefault();

    var nombre = $("#nombre").val();
    var peso = $("#peso").val();
    var estatura = $("#estatura").val();

    function calcular_imc(p, e) {
      return Math.trunc(p / e ** 2);
    }

    var imc = calcular_imc(peso, estatura);

    function clasificar_imc(imc) {
      var entrenamiento = "No determinada";

      var valor_imc= parseFloat(imc)
      
      if (valor_imc <  16 && valor_imc>0) {
        entrenamiento = "Tipo 1";
      } else if (16 <= valor_imc && valor_imc< 16.99) {
        entrenamiento = "Tipo 1 ";
      } else if (17 <= valor_imc && valor_imc < 18.49) {
        entrenamiento = "Tipo 1 y 2";
      } else if (18.5 <= valor_imc && valor_imc < 24.99) {
        entrenamiento = "Tipo 2";
      } else if (25 <= valor_imc && valor_imc < 29.99) {
        entrenamiento = "Tipo 2 y 3";
      } else if (30 <= valor_imc && valor_imc < 34.99) {
        entrenamiento = "Tipo 3";
      } else if (35 <= valor_imc && valor_imc < 40) {
        entrenamiento = "Tipo 3 o 4";
      } else if (41 <= valor_imc ) {
        entrenamiento = "Tipo 4";
      } else {
        greeting = "error";
      }

      return entrenamiento;
    }

    var clasificacion = clasificar_imc(imc)

    var fila = '<tr><th>'+nombre+'</th><th>'+peso+'</th><th>'+estatura+'</th><th>'+imc+'</th><th>'+clasificacion+'</th></tr>';

    $('#tablaprueba>tbody').append(fila);
  
  });
});


