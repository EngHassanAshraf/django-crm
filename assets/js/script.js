// const navListLinks = document.querySelectorAll(".nav-list-link");

// navListLinks.forEach(link => {
//     link.addEventListener("click", ()=>{
//         if (!link.classList.contains("active")){
//             link.classList.add("active");
//         }
//     });
// });


const closeButton = document.querySelector(".close-button");
let alertArea = document.querySelector(".alert")
if (closeButton && alertArea) {
    closeButton.addEventListener("click", () => {
        alertArea.style.display = "none";
    });
}