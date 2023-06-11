console.log("I'm linked!");

function checkPasswordsMatch(form) {
    let p1 = form.password
    let p2 = form.password_confirmation
    return p1 === p2;
}

(function () {
    'use strict'

    const form = document.getElementById('registerForm')
    console.log('Got form', form)
    form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
            console.log('Something is wrong')
            event.preventDefault()
            event.stopPropagation()
        }
        else if (!checkPasswordsMatch(form)) {
            console.log('Passwords match check failed')
            form.
            event.preventDefault()
            event.stopPropagation()
        }
        else {
            console.log('Sending request...')
        }
        form.classList.add('was-validated')
    }, false)
})()