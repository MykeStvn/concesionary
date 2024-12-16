$(document).ready(function() {
    // Delegación de eventos para los botones de editar
    $('body').on('click', '.btn-warning', function(e) {
        e.preventDefault(); // Prevenir el comportamiento predeterminado del enlace (evitar que se recargue la página)
        var cityId = $(this).data('id');  // Obtener el ID de la ciudad desde el atributo 'data-id'
        editCity(cityId);  // Llamar a la función para editar la ciudad
    });

    // Delegación de eventos para los botones de eliminar
    $('body').on('click', '.btn-danger', function(e) {
        e.preventDefault(); // Prevenir el comportamiento predeterminado del enlace
        var cityId = $(this).data('id');  // Obtener el ID de la ciudad desde el atributo 'data-id'
        deleteCity(cityId);  // Llamar a la función para eliminar la ciudad
    });
});

// Función para editar la ciudad
function editCity(cityId) {
    console.log("Editing city with ID: " + cityId);  // Para depuración
    // Realiza la solicitud AJAX para obtener los datos de la ciudad y llenar el formulario de edición
    $.ajax({
        url: '{% url "get_city_data" %}',  // Aquí debes colocar la URL de tu vista para obtener los datos de la ciudad
        type: 'GET',
        data: { 'id': cityId },
        success: function(response) {
            // Si la solicitud es exitosa, llena el formulario de edición con los datos de la ciudad
            $('#editCityId').val(response.id_city);
            $('#editCityName').val(response.name_city);
            // Muestra el modal de edición
            $('#editCityModal').modal('show');
        },
        error: function() {
            alert("Error al cargar los datos de la ciudad");
        }
    });
}

// Función para eliminar la ciudad
function deleteCity(cityId) {
    // Confirmación antes de eliminar
    if (confirm('¿Está seguro de que desea eliminar esta ciudad?')) {
        $.ajax({
            url: '{% url "delete_city" %}',  // Aquí debes colocar la URL de tu vista para eliminar la ciudad
            type: 'POST',
            data: {
                'id_city': cityId,
                'csrfmiddlewaretoken': '{{ csrf_token }}'  // Asegúrate de incluir el token CSRF
            },
            success: function(response) {
                if (response.status === 'success') {
                    alert('Ciudad eliminada exitosamente');
                    location.reload();  // Recarga la página para reflejar los cambios
                } else {
                    alert('Error al eliminar la ciudad');
                }
            },
            error: function() {
                alert('Error al eliminar la ciudad');
            }
        });
    }
}
