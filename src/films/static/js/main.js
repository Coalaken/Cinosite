$(document).ready(function () {

    const csrf = $("input[name=csrfmiddlewaretoken]").val();

    const button = $(".bookmarks-button");

    const likeButton = $(".like-button")
    
    button.click(function() {
        $.ajax({
            url: "",
            type: "post",
            data: {
                csrfmiddlewaretoken: csrf,
                button_value: $(this).val()
            },
            success: function (response) {
                console.log("Success")
            },
            error: { function(response) {
                    console.log("SomeError")
                }
            }
        });
    });

    likeButton.click(function() {
        $.ajax({
            url: "",
            type: "post",
            data: {
                csrfmiddlewaretoken: csrf,
                liked_film: $(this).val()
            },
            success: function() {
                console.log('success')
                if ($("btn-danger")) {
                    likeButton.removeClass("btn-danger").addClass('btn-success')
                } 
                // if ($('btn-success')) {
                //     likeButton.removeClass("btn-success").addClass('btn-danger')
                // } 
                
            },
            error: function() {
                console.log("OSOme Error")
            }
        })
    })
    
});



// $(document).ready(function () {

//     const csrf = $("input[name=csrfmiddlewaretoken]").val();

//     $(".btn").click(function () {
//         $.ajax({
//             url: "",
//             type: "GET",
//             data: {
//                 button_name: $(this).text()
//             },
//             success: (response) => {
//                 $(".btn").text(response.seconds)
//                 $("#seconds").append("<li>" + response.seconds + '</li>')
//             }
//         });
//     }); 

//     $("#seconds").on('click', 'li', () => {
//         $.ajax({
//             url:'',
//             type: 'post',
//             data: {
//                 text: $(this).text(),
//                 csrfmiddlewaretoken: csrf
//             },
//             success: (response) => {
//                 $("#right").append('<li>' + response.data + '</li>')
//             }
//         })
//     });
// });      
        

