const h1 = document.querySelector("div.hello h1");

const originalClass = h1.className;

function handleTitleClick() {
    h1.classList.toggle("clicked");
}

h1.addEventListener("click", handleTitleClick);