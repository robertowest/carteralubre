// Call the dataTables jQuery plugin

$(document).ready(function() {
  $('#dataTable').DataTable({
    "language": {
      "decimal":        "",
      "emptyTable":     "No hay datos disponibles en la tabla",
      "info":           "Mostrando _START_ a _END_ de _TOTAL_ registros",
      "infoEmpty":      "No hay registros disponibles",
      "infoFiltered":   "(filtrado de _MAX_ registros)",
      "infoPostFix":    "",
      "thousands":      ",",
      "lengthMenu":     "Mostrar _MENU_ registros",
      "loadingRecords": "Cargando ...",
      "processing":     "Procesando ...",
      "search":         "Buscar:",
      "zeroRecords":    "No se encontraron registros",
      "paginate": {
          "first":      "Primero",
          "last":       "Último",
          "next":       "Siguiente",
          "previous":   "Anterior"
      },
      "aria": {
          "sortAscending":  ": activar para ordenar la columna ascendente",
          "sortDescending": ": activar para ordenar la columna descendente"
      }
    },
    "lengthMenu": [ 10, 15, 20, 25 ],
    "pageLength": 15,
    "recordsTotal": 100,
    "recordsFiltered": 100,    
  });
});

/*
$(document).ready(function() {
  $('#dataTable').DataTable( {
    "language": {},
    "lengthChange": false,
    "responsive": true,
    "scrollX": true,
    "searching": true,
    "order": [[ 1, "asc" ]],
  });
});
*/