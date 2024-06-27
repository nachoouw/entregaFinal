// Inicializar carrito
let carrito = [];

function seleccionarProducto() {
    var productoSeleccionado = $("#productos option:selected").text();
    
    agregarProductoAlCarrito(productoSeleccionado);
    
    var nuevoElemento = $("<li></li>").text(productoSeleccionado);
    
    $("#lista-productos").append(nuevoElemento);
}



function renderizarCarrito() {
    const carritoElemento = $("#carrito");
    carritoElemento.empty();

    carrito.forEach(producto => {
        const li = $("<li>").addClass("list-group-item").text(`${producto.nombre}`);
        carritoElemento.append(li);
    });
}


// Función para agregar un producto al carrito
function agregarProductoAlCarrito(nombre) {
    const producto = {
        nombre: nombre,
    };
    carrito.push(producto);
    renderizarCarrito();
}

// Función para eliminar un producto del carrito
function eliminarProductoDelCarrito(nombre) {
    carrito = carrito.filter(producto => producto.nombre !== nombre);
    renderizarCarrito();
}



// Evento al hacer clic en 'Vaciar Carrito'
$("#vaciarCarrito").click(function() {
    carrito = [];
    renderizarCarrito();
});