
function make_chart() {
	$('#myTabs a').click(function (e) {
		e.preventDefault();
		$(this).tab('show');

		// Check if the "Chart" tab is active
		if ($(this).attr('href') === '#chart') {
			// Initialize and render the chart here
			var graphs = {{ graphJSON | safe}}; Plotly.newPlot('chart', graphs, {});
		}
	});
};

//function to get description of the superfamily
function get_description(sf_doc) {
  let summary = $('#summary');
  summary.html('');
  let _id = sf_doc['_id'];
  let des = sf_doc['des'];
  let scop_cl = sf_doc['scop_cl'];
  let scop_cf = sf_doc['scop_cf'];
  let sequences = sf_doc['sequences'];
  let tp_sequences = sf_doc['tp_sequences'];
  let scop_da = sf_doc['scop_da'];
  let pfam_da = sf_doc['pfam_da'];
  let genomes = sf_doc['genomes'];
  let sum = `<table>
		  <tr>
			  <th>Superfamily ID</th>
			  <td>${_id}</td>
		  </tr>
		  <tr>
			  <th>Description</th>
			  <td>${des}</td>
		  </tr>
		  <tr>
			  <th>SCOP Class ID</th>
			  <td>${scop_cl}</td>
		  </tr>
		  <tr>
			  <th>SCOP Fold ID</th>
			  <td>${scop_cf}</td>
		  </tr>
		  <tr>
			  <th>Number of Sequences</th>
			  <td>${sequences}</td>
		  </tr>
		  <tr>
			  <th>Number of True Positive Sequences</th>
			  <td>${tp_sequences}</td>
		  </tr>
		  <tr>
			  <th>Number of SCOP Domain Architecture</th>
			  <td>${scop_da}</td>
		  </tr>
		  <tr>
			  <th>Number of PFAM Domain Architecture</th>
			  <td>${pfam_da}</td>
		  </tr>
		  <tr>
			  <th>Number of Genomes</th>
			  <td>${genomes}</td>
		  </tr>
		  <!-- Add more rows as needed -->
	  </table>`;
	  summary.append(sum);
}
$.ajax({
	url : '/superfamily_display/' + sf_code,
	type : 'POST',
	dataType : 'json',
	success: function(response) {
		sf_doc = response;
		get_description(response);
	},
	error: function(error) {
		console.log(error);
	}
});