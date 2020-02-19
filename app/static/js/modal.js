window.onload = function(){
    const openButton = document.getElementById("open");
    const modal = document.querySelector(".modal");
    const overlay = modal.querySelector(".modal_overlay");
    const closeBtn = modal.querySelector(".closeBtn");
    //const submit = modal.querySelector(".submit");
    const openModal = () => {
            modal.classList.remove("hidden");
        }
    const closeModal = () => {
            modal.classList.add("hidden");
        }
    /*const submitModal = () {
        
    }
    submit.addEventListener("click", submitModal);
    
    */
    overlay.addEventListener("click", closeModal);
    closeBtn.addEventListener("click", closeModal);
    openButton.addEventListener("click", openModal);  
}