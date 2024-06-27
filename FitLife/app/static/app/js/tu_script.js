document.getElementById('btn-cargar').addEventListener('click', function() {
    const url = 'https://www.themealdb.com/api/json/v1/1/random.php';
  
    fetch(url)
      .then(response => response.json())
      .then(data => {
        const meal = data.meals[0];
        const nombre = meal.strMeal;
        const imagen = meal.strMealThumb;
        const instrucciones = meal.strInstructions;
  
        const recetaHTML = `
          <div class="receta">
            <img src="${imagen}" alt="${nombre}">
            <div class="contenido">
              <h2>${nombre}</h2>
              <p>${instrucciones}</p>
            </div>
          </div>
        `;
  
        document.getElementById('receta').innerHTML = recetaHTML;
      })
      .catch(error => {
        console.error('Error al obtener los datos:', error);
        document.getElementById('receta').innerText = 'Error al obtener los datos.';
      });
  });
  