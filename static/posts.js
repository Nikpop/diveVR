$("#btn_get_post").click(function () {

$.ajax({
    type: "POST",
    url: "/posts_new/",
    data: {
        'button': $("#button_name_input").val(),
    },
    dataType: "text",
    cache: false,
    success: function (data) {
            console.log("ok");
            alert('DONE');
        }
    }
});