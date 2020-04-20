$(document).ready( function () {
    $('#myTable').DataTable({
        ajax: {
            url: '/api/music_list/',
            dataType: "json",
            dataSrc: 'results',
            paging: true,
            searching: true,
        },
        columns: [
            { data: 'cover_image',
                  "render": function (data) {
                       return `<img src="${data}" class="img-fluid rounded" width="100" height="100">`;
                  }
            },
            { data: 'artist' },
            { data: 'title' },
            { data: 'label' },
            { data: 'year' },
            { data: 'catalogue_number' },
            {data: 'id',
                "render": function (data) {
                       return `<a href="detail/${data}" class="btn btn-danger">More>></a>`;
                }

            }
        ]
    });


    //Detail
    var url = window.location.href;
    var splitUrl = url.split("/");
    var id = splitUrl[5];
    $.ajax({
          type: 'GET',
          url: `/api/music_list/${id}/`,
          dataType: 'json',
          success : function(data){
                var img = data.cover_image;
                var title = data.title;
                var artist = data.artist;
                var label = data.label;
                var year = data.year;
                var cat_no = data.catalogue_number;
                var record = `
                            <h1 class="text-dark">Artist:${artist}</h1>
                            <p>Song Title: ${title}</p>
                            <p>Record Label: ${label}</p>
                            <p>Released: ${year}</p>
                            <p>Catalog No: ${cat_no}</p>`

                $('#detail_img').append(`<img src='${img}' class="img-fluid" alt="${artist}">`);
                $('#detail_info').append(record);

          },
     });


});
