const fields = [
    { data: 'id', orderable: false, searchable: false },
    { data: 'name', orderable: true, searchable: true },
    { data: 'surname', orderable: true, searchable: true },
    { data: 'username', orderable: true, searchable: true },
    { data: 'email', orderable: true, searchable: true },
    { data: 'role', orderable: true, searchable: true }
];
$(document).ready(function() {
    // Retrieve the value of the data-path attribute
    var datatablePath = $('#datatablePath').data('path');
    console.log("Datatable path:", datatablePath);
    // Now you can use the datatablePath variable as needed in your JavaScript code
    createDataTable('table.dataTableServersideClass', datatablePath, fields, false);
});
// create datatable passing the selector, url of ajax, the filed, and false because i don't want the rowchild

