document.addEventListener("DOMContentLoaded", function () {
    console.log("Script.js loaded!"); // Debugging

    const navLinks = document.querySelectorAll(".nav-link");
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navbarCollapse = document.getElementById("collapsibleNavId");

    navLinks.forEach(link => {
        link.addEventListener("click", () => {
            console.log("Nav link clicked!"); // Debugging
            if (navbarCollapse.classList.contains("show")) {
                navbarToggler.click();
            }
        });
    });
});




// Validation form 

function validate(){
    const username = document.getElementById("full-name").value;
    const nameError = document.getElementById("nameError");
    const alphaExp = /^[a-zA-Z ]+$/ ;
    const mail = document.getElementById("email").value;
    const mailError = document.getElementById("mailError");
    const mailExp = /^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$/; 
    const mobile = document.getElementById("phone").value;
    const mobileError = document.getElementById("mobileError");
    const numExp = /^[0-9]+$/ ;
    const startDate = document.getElementById("start-date").value;
    const endDate = document.getElementById("end-date").value;
    const numTravelers = document.getElementById("num-travelers").value;
    
    const startDateError = document.getElementById("startDateError");
    const endDateError = document.getElementById("endDateError");
    const travelerError = document.getElementById("travelerError");
    
    const today = new Date(); // Current date
    today.setHours(0, 0, 0, 0); // Set the current date to midnight
    const start = new Date(startDate); // Start date entered by user
    const end = new Date(endDate); // End date entered by user
    
    let nameStatus = false;
    let mobileStatus = false;
    let mailStatus = false;
    let startDateStatus = false;
    let endDateStatus = false;
    let travelerStatus = false;

    // Name Validation

    if (username === "")
    {
        nameError.textContent = ("Please enter name");
    }
    else{
        if(username.match(alphaExp)){
            nameError.textContent = "";
            nameStatus = true;
        }
        else{
            nameError.textContent = ("Name should be only characters");
        }
    }

    // Mail Validation
    if (mail === "")
        {
            mailError.textContent = ("Please enter mail");
        }
        else{
            if(mail.match(mailExp)){
                mailError.textContent = "";
                mailStatus = true;
            }
            else{
                mailError.textContent = ("Please enter valid mail");
            }
        }
    
    // Mobile Validation
    if (mobile === "")
        {
            mobileError.textContent = ("Please enter phone number");
        }
        else{
            if(mobile.match(numExp)){
                if (mobile.length === 10){
                    mobileError.textContent = "";
                    mobileStatus = true;
                }
                else{
                    mobileError.textContent = ("Phone number should be 10 digits");
                }
                
            }
            else{
                mobileError.textContent = ("Phone number should be only numbers");
            }
        }
    // Start Date Validation
    if (startDate === "") {
        startDateError.textContent = "Please select a start date";
    } else if (start < today) {
        startDateError.textContent = "Start date cannot be in the past";
    } else {
        startDateError.textContent = "";
        startDateStatus = true;
    }
    
    // End Date Validation
    if (endDate === "") {
        endDateError.textContent = "Please select an end date";
    } else if (end <= start) {
        endDateError.textContent = "End date must be after the start date";
    } else {
        endDateError.textContent = "";
        endDateStatus = true;
    }

    // Travelers Validation
    if (numTravelers < 1 || numTravelers > 20) {
        travelerError.textContent = "Number of travelers must be between 1 and 20";
    } else {
        travelerError.textContent = "";
        travelerStatus = true;
    }

    // Return Validation
    if (nameStatus  && mobileStatus && mailStatus && startDateStatus && endDateStatus && travelerError){
        return true;
    }
    else{
        return false;
    }
}
