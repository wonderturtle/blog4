// F.P.

// This file contain the script to make the table row expandable and create a child table.
// create and include a file like this when you want to make the table row expandable.
// Before including this file, include the script "includes/datatables/style_and_script.html",
// that contain the initialization of the primary table.

// To adapt the child table with the correct data, change this parts of the script:

// 1) Change the url of the ajax request
//     url: '{{ url_for("user.role") }}', 

// 2) Put the correct header of ther child table
//     '<tr>' +
//         '<th>Role ID</th>' +
//         '<th>Role</th>' +
//         '<th>Note</th>' +
//         // Add more headers as needed
//     '</tr>' +

// 3) Put the correct data of the child table
//     '<tr>' +
//         '<td>' + item.role_id + '</td>' +
//         '<td>' + item.role + '</td>' +
//         '<td>' + item.note + '</td>' +
//         // Add more columns as needed
//     '</tr>';

table.on('click', 'td.dt-control-plus', function (e) {
        
    let tr = e.target.closest('tr');
    $(tr).attr('data-table-id', tr.id);

    let row = table.row(tr);

    if (row.child.isShown()) {
        // This row is already open - close it
        row.child.hide();
    } else {
        // Open this row
        row.child('Loading...').show();

        let csrfToken = $('#csrf_token').val();
        let idForAjax = $(tr).data('table-id');
        

        // Make AJAX request to fetch user/order data
        $.ajax({
            url: '/user/role',
            type: 'POST',
            data: {
                id: idForAjax, // pass the user Id to route
                csrf_token: csrfToken,
            },
            dataType: 'json',
            success: function (response) {
                try {
                    console.log("Response:", response);
                    // Check if response.data is an array
                    if (Array.isArray(response.data)) {
                        // Create the child table 
                        let childRow = '<div class="child-row card">' +
                            '<div class="card-header bg-primary">' +
                            '<h5 class="card-title">Role</h5>' +
                            '</div>' +
                            '<div class="card-body ">' +
                            '<table class="childTable table width-90 mx-auto">' +
                            '<thead>' +
                            '<tr>' +
                            '<th>Role ID</th>' +
                            '<th>Role</th>' +
                            '<th>Note</th>' +
                            // Add more headers as needed
                            '</tr>' +
                            '</thead>' +
                            '<tbody>';

                        // Populate the child table with data
                        response.data.forEach(function (item) {
                            childRow += '<tr>' +
                                '<td>' + item.role_id + '</td>' +
                                '<td>' + item.role + '</td>' +
                                '<td>' + item.note + '</td>' +
                                // Add more columns as needed
                                '</tr>';
                        });

                        // Close the child table
                        childRow += '</tbody>' +
                            '</table>' +
                            '</div>' +
                            '</div>';

                        console.log("Child row HTML:", childRow);

                        // Append the child table to the current row
                        row.child(childRow).show();

                        // Destroy existing DataTables on child tables
                        $('.childTable').DataTable().destroy();

                        // Initialize all child tables without row selection and without the option to change the number of rows per page
                        $('.childTable').DataTable({
                            lengthChange: false
                        });
                    } else {
                        // Handle the case where response.data is not an array
                        console.error('Invalid or missing data in the response:', response);
                        row.child('Error loading data.').show();
                    }
                } catch (error) {
                    // Handle any unexpected errors
                    console.error('An unexpected error occurred:', error);
                    row.child('Error loading data.').show();
                }
            },
            error: function (xhr, status, error) {
                console.error('AJAX request failed:', error);
                row.child('Error loading data.').show();
            }
        });
    }
});