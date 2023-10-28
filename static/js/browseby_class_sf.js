// function that builds the table
function buildTable(data) {
	// tbody
	let tbody = $('.table-body');
	let after_table = $('#no-data-display');
	if (data.length === 0) {
		tbody.html('');
		after_table.html('<p>No Matching Records Found</p>');
	} else {
		tbody.html(''); // html method is used to reset the content
		after_table.html('');
		let row;
		for (let i = 0; i < data.length; i++) {
			row = `<tr>
        <td>
          <a class="sf-id" href="/superfamily_display/${data[i]._id}" target="_blank">
            ${data[i]._id}
          </a>
          <img src="static/img/popup-link-icon.svg" alt="link to another page">
        </td>
        <td>${data[i].des}</td>
        <td>${data[i].pfam_da}</td>
        <td>${data[i].scop_da}</td>
        <td>${data[i].genomes}</td>
        <td>${data[i].scop_cl}</td>
        <td>${data[i].scop_cf}</td>
        <td>${data[i].sequences}</td>
        <td>${data[i].tp_sequences}</td>
      </tr>`;
			tbody.append(row);
		}
	}
}

// Sorting the rows acc to '_id' first when the page loads
function sortTableFirst(data) {
	data.sort((a, b) => a['_id'] - b['_id']);
	buildTable(data);
}

// Function that searches through the table and allows only those rows to
// exist which contain the string of characters in the search input box
function searchTable(value, data) {
	let filtered_data = [];
	value = value.toLowerCase();
	for (let i = 0; i < data.length; i++) {
		let des = data[i].des.toLowerCase();
		if (des.includes(value)) {
			filtered_data.push(data[i]);
		}
	}
	return filtered_data;
}


var table_data = []; // empty array so that the data from server could be stored for later use
// ajax requests the server for data at 'superfamily_data' route
// gets the data in 'response' object
// calls the buildTable function
$.ajax({
	url: '/class_sf_data', /* Flask route here and not the name of that function */
	type: 'POST', /* type of request that would fetch the data from the server side */
	data: { 'cl_code': cl_code }, /* data that would be sent to the server side */
	dataType: 'json', /* expected type of the data that would be fetched */
	success: function (response) { /* function that executes itself when the retrieval of the data from the server side is a success */
		table_data = response;
		buildTable(table_data);
		sortTableFirst(table_data);
	},
	error: function (error) {
		console.log(error);
	}
});


// When a character is entered in the input box, only the descriptions that contain that particular character would be displayed
let search_input = $('#top-right-input');
search_input.on('keyup', function (event) {
	let value = $(this).val(); // value of the key/character that was entered
	buildTable(searchTable(value, table_data));
});

// thead sorting upon clicking the td in thead
(function () {
	let col_header = $("thead td");
	$(col_header[0]).find('img').css({ display: 'none' }); // the first column header starts in ascending order
	col_header.on('click', function () {
		if ($(this).attr('data-order') === 'none') {
			$(this).attr('data-order', 'asc');
			$(this).find('img').css({ display: 'none' });
			$(this).siblings(':not(this)').find('img').css({ display: 'inline-flex' });
			$(this).siblings(':not(this)').attr('data-order', 'none');
			if ($(this).attr('data-col') === 'des') {
				table_data.sort((a, b) => a[$(this).attr('data-col')].localeCompare(b[$(this).attr('data-col')]));
			} else {
				table_data.sort((a, b) => a[$(this).attr('data-col')] - b[$(this).attr('data-col')]);
			}
			buildTable(table_data);
		} else if ($(this).attr('data-order') === 'asc') {
			$(this).attr('data-order', 'des');
			$(this).find('img').css({ display: 'none' });
			$(this).siblings(':not(this)').find('img').css({ display: 'inline-flex' });
			$(this).siblings(':not(this)').attr('data-order', 'none');
			if ($(this).attr('data-col') === 'des') {
				table_data.sort((a, b) => b[$(this).attr('data-col')].localeCompare(a[$(this).attr('data-col')]));
			} else {
				table_data.sort((a, b) => b[$(this).attr('data-col')] - a[$(this).attr('data-col')]);
			}
			buildTable(table_data);
		} else {
			$(this).attr('data-order', 'asc');
			$(this).find('img').css({ display: 'none' });
			$(this).siblings(':not(this)').find('img').css({ display: 'inline-flex' });
			$(this).siblings(':not(this)').attr('data-order', 'none');
			if ($(this).attr('data-col') === 'des') {
				table_data.sort((a, b) => a[$(this).attr('data-col')].localeCompare(b[$(this).attr('data-col')]));
			} else {
				table_data.sort((a, b) => a[$(this).attr('data-col')] - b[$(this).attr('data-col')]);
			}
			buildTable(table_data);
		}
	});
})();
