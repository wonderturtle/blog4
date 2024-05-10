// initialize the DataTable with the class name "dataTableClass"
let table = new DataTable('table.dataTableClass', {
    columnDefs: [
        {
            className: 'dtr-control',
            orderable: false,
            targets: 0
        }
    ],
    order: [1, 'asc'],
    // responsive: {
    //     details: {
    //         type: 'column-visibility',
    //         target: 'td.dt-control-plus' // specify the target column
    //     }
    // },

    // options for length menu choice
    lengthMenu: [
        [10, 25, 50, -1],
        [10, 25, 50, 'All']
    ],

    // default row to show in the table
    pageLength: 50,

    dom: 
    // 'f' is search bar 
    // 'B' is buttons exandable
    // 'l' is select of row t o show
    // 'i' is info
    // 'p' is pagination
    
    "<'row'<'col-sm-6'l ><'col-sm-6 d-flex justify-content-end'f B>>" +
    "<'row'>" +
    "<'top-part table-responsive'<'col-sm-12'tr>>" +
    "<'row'<'col-sm-6'i><'col-sm-6'p>>",
    
    buttons: [
        {
            extend: 'collection',
            className: 'custom-html-collection',
            text: '<p><i class="fa fa-download"></i></p>',
            buttons: [
                'pdf',
                'csv',
                'excel',
                'copy',
                'print',
            ]
        }
    ],
    

});