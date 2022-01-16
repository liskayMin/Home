const h1 = document.querySelector(".hello h1");

function handleH1Click() {
    const currentColor = h1.style.color;
    let newColor;
    if (currentColor ==="blue") {
        newColor ="tomato";
        console.log(newColor);
    } else {
        newColor ="blue";
        console.log(newColor);
    }
    h1.style.color = newColor;
}



h1.addEventListener("click", handleH1Click);


console.dir(h1);