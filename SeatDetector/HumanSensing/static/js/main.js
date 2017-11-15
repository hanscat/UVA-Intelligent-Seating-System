/**
 * Created by Kefan on 10/20/17.
 */

$(document).ready(function() {
    $('#example').DataTable( {
        "ajax": "data/objects.txt",
        "columns": [
            { "data": "name" },
            { "data": "position" },
            { "data": "office" },
            { "data": "extn" },
            { "data": "start_date" },
            { "data": "salary" }
        ]
    } );
} );

window.setTimeout(function () {
    location.href = "localhost:8000";
}, 5000);

$.ajax({
    type: 'POST',
    url: post_url, 
    data: post_data,
    success: function(msg) {
        $(form).fadeOut(800, function () {
            form.html(msg).fadeIn().delay(2000);
    
    });
}});