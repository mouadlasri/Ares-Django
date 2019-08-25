

window.onload = typeWriter;

window.onscroll = function () {
    scrollFunction();  
};

function scrollFunction() {
    // When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
        document.getElementById("navbar").style.padding = "10px 10px";
        document.getElementById("navbar").style.backgroundColor = "#2c2d3e";
        document.getElementById("brand").style.color = "white";
        document.getElementById("brand").fontSize = "15px";
        var titles = document.getElementsByClassName("navigation-title");
        // console.log(titles);
        for (var i = 0; i < titles.length; i++) {
            titles[i].style.fontSize = "15px";
            titles[i].style.color = "white";
        }
    } else {
        document.getElementById("navbar").style.padding = "20px 10px";
        document.getElementById("navbar").style.backgroundColor = "#f1f1f1";
        document.getElementById("brand").style.color = "black";
        document.getElementById("brand").fontSize = "22px";
        var titles = document.getElementsByClassName("navigation-title");
        for (var i = 0; i < titles.length; i++) {
            titles[i].style.fontSize = "22px";
            titles[i].style.color = "black";
        }
    }
}

var i = 0;
var txt = "Mouad Lasri"
var speed = 75;

function typeWriter() {
    if (i < txt.length) {
        document.getElementById("name").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    }
}


