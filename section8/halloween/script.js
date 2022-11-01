document.addEventListener("DOMContentLoaded", function(){
    let button = document.querySelector("button");
    button.addEventListener("click", function(){
        text = document.querySelector("p");
        if (text.style.color == "orange")
        {
            blackify();
        }
        else
        {
            orangify();
        }
    });
});

function orangify(){
    text = document.querySelector("p");
    text.style.color = "orange";
    text.classList.add("cool")
}

function blackify(){
    text = document.querySelector("p");
    text.style.color = "#f056c7";
    text.classList.add("cool")
}

