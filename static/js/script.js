const categoryBtn = document.getElementById("category_btn");
const categoryList = document.getElementById("category");

categoryBtn.addEventListener("click", ()=> {
    categoryList.classList.toggle("visible");
})