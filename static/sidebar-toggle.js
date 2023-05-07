// JavaScript source code
const sidebarToggle = document.getElementById("sidebar-toggle");
const sidebar = document.querySelector(".sidebar");

sidebarToggle.addEventListener("click", () => {
    sidebar.classList.toggle("hide");
    sidebar.classList.toggle("show"); 
    if (sidebar.classList.contains("hide")) {
        sidebarToggle.style.left = "0";
    } else {
        sidebarToggle.style.left = `${sidebar.offsetWidth}px`;
    }
});