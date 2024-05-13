const fields = [
    { data: 'id', orderable: false, searchable: false },
    { data: 'name', orderable: true, searchable: true },
    { data: 'surname', orderable: true, searchable: true },
    { data: 'username', orderable: true, searchable: true },
    { data: 'email', orderable: true, searchable: true },
    { data: 'role', orderable: true, searchable: true }
];

// create datatable passing the selector, url of ajax, the filed, and false because i don't want the rowchild
createDataTable('table.dataTableServersideClass', '/app/user/datatable', fields, false);
