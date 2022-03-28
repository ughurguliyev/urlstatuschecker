$(document).ready(function () {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === name + "=") {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie("csrftoken");


    $(".urls").each(function () {
        let url = $(this).text();
        
        checkURLResponseCode(url, $(this));
    });


    function addResultToRow(isSuccess, element) {
        if (isSuccess) {
            element.css('background-color', '#4BB543');
        } else {
            element.css('background-color', '#B00020');
        };
    };


    function checkURLResponseCode(url, element) {
        $.ajax({
            url: window.location.pathname,
            type: "POST",
            data: {
                csrfmiddlewaretoken: csrftoken,
                action: "check_url",
                url: url,
            },
            success: function (data) {
                addResultToRow(data.success, element);
            }
        });
    };
});