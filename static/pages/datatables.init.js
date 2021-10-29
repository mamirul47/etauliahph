/*
 Template Name: Annex - Bootstrap 4 Admin Dashboard
 Author: Mannatthemes
 Website: www.mannatthemes.com
 File: Datatable js
 */

$(document).ready(function() {
    $('#datatable').DataTable();

    //Buttons examples
    var table = $('#datatable-buttons').DataTable({
        lengthChange: false,
        buttons: ['copy', 'excel', 'pdf', 'colvis']
    });

    table.buttons().container()
        .appendTo('#datatable-buttons_wrapper .col-md-6:eq(0)');

    $('#datatable_soalanAudit').DataTable({
        "language": {
            "lengthMenu": "Papar _MENU_ rekod dalam satu halaman",
            "zeroRecords": "Tiada rekod dijumpai",
            "info": "Halaman _PAGE_ daripada _PAGES_",
            "infoEmpty": " ",
            "infoFiltered": "(Tapisan daripada _MAX_ rekod keseluruhan)",
            "search": "Carian",
            "paginate": {
                "previous": "Sebelum",
                "next": "Seterusnya"
            },
        },
        "lengthChange": false,
        "pageLength": 5,
        "order": [
            [0, "asc"]
        ],
        "ordering": true,

    });

});