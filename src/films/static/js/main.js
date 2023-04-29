$(document).ready(function () {

    const csrf = $("input[name=csrfmiddlewaretoken]").val();

    const button = $(".btn");

    // let like_button = document.querySelector(".btn")

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
    

    
    // button.click(function() {
    //     $.ajax({
    //         url: "/SoGood/films/3/", 
    //         type: "post",
    //         data: {
    //             csrfmiddlewaretoken: csrf,
    //             like_field: $(this).val()
    //         },
    //         success: function() {
    //             return
    //         }
    //     })
    // })
    
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
        

