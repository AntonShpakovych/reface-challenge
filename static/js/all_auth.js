function getElementsForToggling(){
    let loginToggle = document.getElementById("login-toggle")
    let signUpToggle = document.getElementById("signup-toggle")
    let loginForm = document.getElementById("login-form")
    let signUpForm =  document.getElementById("signup-form")

    return [loginToggle, signUpToggle, loginForm, signUpForm]
}

function toggleSignup(){
    let [
        loginToggle,
        signUpToggle,
        loginForm,
        signUpForm
    ] = getElementsForToggling()

    loginToggle.style.backgroundColor="#fff";
    loginToggle.style.color="#222";
    signUpToggle.style.backgroundColor="#57b846";
    signUpToggle.style.color="#fff";
    loginForm.style.display="none";
    signUpForm.style.display="block";
}

function toggleLogin(){
    let [
        loginToggle,
        signUpToggle,
        loginForm,
        signUpForm
    ] = getElementsForToggling()

    loginToggle.style.backgroundColor="#57B846";
    loginToggle.style.color="#fff";
    signUpToggle.style.backgroundColor="#fff";
    signUpToggle.style.color="#222";
    signUpForm.style.display="none";
    loginForm.style.display="block";
}


function formToRender() {
    let formToRender = document.getElementById("form-to-render");

    if (formToRender && formToRender.value === "form_signup") {
        toggleSignup();
    } else {
        toggleLogin();
    }
}

document.addEventListener("DOMContentLoaded", function() {
    formToRender();
});
