$(document).ready(function () {
    // let likeBut = document.getElementsByClassName("like-button")
    
    const csrf = $("input[name=csrfmiddlewaretoken]").val();

    const button = $(".bookmarks-button");

    const likeButton = $(".like-button")

    const btn = document.getElementById("filmliked")
    const index = 0

    function buttonColor () {
        if (btn.style.backgroundColor === 'grey') {
            btn.style.backgroundColor = 'red'
        } else {
            btn.style.backgroundColor = 'grey'
        }
    }

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
                console.log("syu")

                btn.onclick =  buttonColor
               
            },
            error: function() {
                console.log("OSOme Error")
            }
        });
    });

    

    
});


        

