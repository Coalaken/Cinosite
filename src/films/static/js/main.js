$(document).ready(function () {

    const csrf = $("input[name=csrfmiddlewaretoken]").val();

    const button = $(".btn");

    button.click(function() {
        $.ajax({
            url: "",
            type: "post",
            data: {
                csrfmiddlewaretoken: csrf,
                button_value: $(this).val()
            },
            success: function (response) {
            }
        })
    });
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
        

