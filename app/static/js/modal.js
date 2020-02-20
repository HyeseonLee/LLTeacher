window.onload = function(){
    const openButton = document.getElementById("open");
    const modal = document.querySelector(".modal");
    const overlay = modal.querySelector(".modal_overlay");
    const closeBtn = modal.querySelector(".closeBtn");
    //const submitButton = document.querySelector(".submitButton");
    //const creatModal = document.getElementById(".creatModal");

    const openModal = () => {
            modal.classList.remove("hidden");
            
        }
    const closeModal = () => {   
            modal.classList.add("hidden");
            window.location.reload();
        }
    /*
    const reload = () => {
        window.location.reload(true)
    }
    */
 
    //overlay.addEventListener("click", closeModal);
    closeBtn.addEventListener("click", closeModal);
    openButton.addEventListener("click", openModal);
    //submitButton.addEventListener("click", reload);
    
   
}