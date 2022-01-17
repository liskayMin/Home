const h1 = document.querySelector("div.hello h1");

const originalClass = h1.className;

function handleTitleClick() {
    const clickedClass = "clicked";
    if(h1.classList.contains(clickedClass)) {
        h1.classList.remove(clickedClass) ;
        console.log(h1.className);
    } else {
        h1.classList.add(clickedClass) ;
        console.log(h1.className);
    }
}
// classList.toggle 로 할 수 있음!

h1.addEventListener("click", handleTitleClick);