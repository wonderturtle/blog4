/**
 * Creates a DataTable with server-side processing for the specified selector and AJAX URL.
 *
 * @param {string} selector - The selector for the DataTable container.
 * @param {string} ajaxUrl - The URL for server-side processing.
 * @param {Array} fields - An array of objects representing the DataTable columns.
 * @param {boolean} [controlColumn=false] - Whether to include a control column.
 * @return {DataTable} The created DataTable instance named "table".
 */

// function createDataTable(selector, ajaxUrl, fields, controlColumn = false) {
//     // Initialize the columns array based on the control column flag
//     const columns = controlColumn ? [{
//         className: 'dt-control-plus',
//         orderable: false,
//         data: null,
//         defaultContent: '<i class="fa fa-plus text-primary"></i>'
//     }] : [];

//     // Add the fields to the columns array
//     columns.push(...fields.map(field => ({
//         data: field.data,
//         orderable: field.orderable !== undefined ? field.orderable : true,
//         searchable: field.searchable !== undefined ? field.searchable : true
//     })));

//     // Create the DataTable with the specified options
//     return table = new DataTable(selector, {
//         serverSide: true, // Enable server-side processing
//         ajax: {
//             url: ajaxUrl, // Set the AJAX URL
//             type: 'POST', // Set the AJAX request type
//             data: {
//                 csrf_token: $('#csrf_token').val() // Add the CSRF token to the AJAX data
//             },
//             dataType: 'json', // Set the expected AJAX response type
//         },
//         columns: columns, // Set the columns for the DataTable
//         columnDefs: [ // Define the column classes
//             {
//                 className: 'dtr-control',
//                 orderable: false,
//                 targets: 0
//             }
//         ],
//         order: [1, 'asc'], // Set the initial ordering
//         lengthMenu: [ // Set the length menu options
//             [10, 25, 50, 999999999999],
//             [10, 25, 50, 'All']
//         ],
//         pageLength: 50, // Set the default page length
//         dom: // Set the DOM structure
//             "<'row'<'col-sm-6'l ><'col-sm-6 d-flex justify-content-end'f B>>" +
//             "<'row'>" +
//             "<'top-part table-responsive'<'col-sm-12'tr>>" +
//             "<'row'<'col-sm-6'i><'col-sm-6'p>>",
//         buttons: [ // Set the buttons configuration
//             {
//                 extend: 'collection',
//                 className: 'custom-html-collection',
//                 text: '<p><i class="fa fa-download"></i></p>',
//                 buttons: [
//                     'pdf',
//                     'csv',
//                     'excel',
//                     'copy',
//                     'print',
//                 ]
//             }
//         ]
//     });
// }


function createDataTable(selector, ajaxUrl, fields, controlColumn = false, advancedSearchFields = false) {
    // Initialize the columns array based on the control column flag
    const columns = controlColumn ? [{
        className: 'dt-control-plus',
        orderable: false,
        data: null,
        defaultContent: '<i class="fa fa-plus text-primary"></i>'
    }] : [];

    // Add the fields to the columns array
    columns.push(...fields.map(field => ({
        data: field.data,
        orderable: field.orderable !== undefined ? field.orderable : true,
        searchable: field.searchable !== undefined ? field.searchable : true
    })));

    // Constructing the data object for AJAX request
    var data_to_send = {
        csrf_token: $('#csrf_token').val(), // Add the CSRF token to the AJAX data
    };

    // Add the advanced search fields to the data object if passed
    if (advancedSearchFields) {
        data_to_send['advanced_search_fields'] = advancedSearchFields;
    }


    // Create the DataTable with the specified options
    return table = new DataTable(selector, {
        serverSide: true, // Enable server-side processing
        ajax: {
            url: ajaxUrl, // Set the AJAX URL
            type: 'POST', // Set the AJAX request type
            data: data_to_send,
            dataType: 'json', // Set the expected AJAX response type
        },
        columns: columns, // Set the columns for the DataTable
        columnDefs: [ // Define the column classes
            {
                className: 'dtr-control',
                orderable: false,
                targets: 0
            }
        ],
        order: [1, 'asc'], // Set the initial ordering
        lengthMenu: [ // Set the length menu options
            [10, 25, 50, 999999999999],
            [10, 25, 50, 'All']
        ],
        pageLength: 50, // Set the default page length
        dom: // Set the DOM structure
            "<'row'<'col-sm-6'l ><'col-sm-6 d-flex justify-content-end'f B>>" +
            "<'row'>" +
            "<'top-part table-responsive'<'col-sm-12'tr>>" +
            "<'row'<'col-sm-6'i><'col-sm-6'p>>",
        buttons: [ // Set the buttons configuration
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
        ]
    });
}
