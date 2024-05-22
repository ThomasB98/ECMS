$(document).ready(function () {
    if (typeof jQuery !== "undefined") {
        console.log("jQuery is loaded.");
    } else {
        console.log("jQuery is not loaded.");
    }
    $(".start-button").on("click", function () {
        var card = $(this).closest(".card");
        var timerSpan = card.find(".timer");
        var icon = card.find(".status-icon");

        var startTime = new Date().getTime();
        var updateTimer = setInterval(function () {
            var currentTime = new Date().getTime();
            var elapsedTime = currentTime - startTime;

            timerSpan.text(formatTime(elapsedTime));
        }, 1000);

        $(this).prop("disabled", true);
        card.find(".stop-button").prop("disabled", false);
        icon.removeClass("bg-success").addClass("bg-warning");
        card.data("timerInterval", updateTimer);
    });

    $(".stop-button").on("click", function () {
        var card = $(this).closest(".card");
        var timerSpan = card.find(".timer");
        var icon = card.find(".status-icon");

        clearInterval(card.data("timerInterval"));

        timerSpan.text("00:00");

        $(this).prop("disabled", true);
        card.find(".start-button").prop("disabled", false);
        icon.removeClass("bg-warning").addClass("bg-success");
    });
});

function formatTime(ms) {
    var seconds = Math.floor(ms / 1000);
    var minutes = Math.floor(seconds / 60);
    seconds %= 60;

    return padTime(minutes) + ":" + padTime(seconds);
}

function padTime(val) {
    return val < 10 ? "0" + val : val;
}


document.addEventListener("DOMContentLoaded", function () {
    var timerForms = document.querySelectorAll(".timer-form");

    timerForms.forEach(function (form) {
        var card = form.closest(".card");
        var timerSpan = card.querySelector(".timer");

        form.addEventListener("submit", function (event) {
            event.preventDefault();

            // Add logic to make an AJAX request to your Django backend
            var postID = form.dataset.postId;
            var timerValue = timerSpan.textContent;

            fetch("/stop-timer/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                body: JSON.stringify({
                    post_id: postID,
                    timer_value: timerValue,
                }),
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response data, if needed
                
                // Stop the timer
                stopTimer(card);
            })
            .catch(error => {
                console.error("Error:", error);
            });
        });
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            var cookies = document.cookie.split(";");
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === name + "=") {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});