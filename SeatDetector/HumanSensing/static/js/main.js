/**
 * Created by Kefan on 10/20/17.
 */
// $( function() {
//   var $winHeight = $( window ).height();
//   $( '.container' ).height( $winHeight );
// });


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