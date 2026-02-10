document.addEventListener("DOMContentLoaded", function () {
    // Selección de elementos del formulario de contacto
    const submitButton = document.getElementById("submitButton");
    const form = document.getElementById("contactForm");
    const nameField = document.getElementById("name");
    const emailField = document.getElementById("email");
    const messageField = document.getElementById("message");
    let captchaValidated = false;

    // Verificar si los elementos del formulario existen
    if (form && submitButton && nameField && emailField && messageField) {
        const touchedFields = {
            name: false,
            email: false,
            message: false,
        };

        // Función para validar el formulario
        function validateForm() {
            const name = nameField.value.trim();
            const email = emailField.value.trim();
            const message = messageField.value.trim();

            // Validaciones
            const isNameValid = name.length > 1;
            const isEmailValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
            const isMessageValid = message.length > 5;

            if (touchedFields.name) {
                nameField.classList.toggle("is-invalid", !isNameValid);
            }
            if (touchedFields.email) {
                emailField.classList.toggle("is-invalid", !isEmailValid);
            }
            if (touchedFields.message) {
                messageField.classList.toggle("is-invalid", !isMessageValid);
            }

            // Habilitar el botón solo si todo es válido y el captcha está validado
            if (isNameValid && isEmailValid && isMessageValid && captchaValidated) {
                submitButton.disabled = false;
                submitButton.classList.remove("disabled");
                console.log("Formulario validado, botón habilitado."); // Debug
            } else {
                submitButton.disabled = true;
                console.log("Formulario no validado, botón deshabilitado."); // Debug
            }
        }

        // Callback de Turnstile
        window.turnstileCallback = function (token) {
            captchaValidated = !!token; // Si el token es válido, marcar como validado
            document.getElementById("cf_turnstile_response").value = token; // Actualizar el campo hidden
            console.log("Token Turnstile actualizado:", token); // Debug
            validateForm(); // Revalidar formulario al recibir el token
        };

        // Escuchar el evento "blur" para marcar un campo como "tocado"
        nameField.addEventListener("blur", () => {
            touchedFields.name = true;
            validateForm();
        });

        emailField.addEventListener("blur", () => {
            touchedFields.email = true;
            validateForm();
        });

        messageField.addEventListener("blur", () => {
            touchedFields.message = true;
            validateForm();
        });

        // Validar en tiempo real los campos del formulario
        [nameField, emailField, messageField].forEach((field) => {
            field.addEventListener("input", validateForm);
        });

        form.addEventListener("submit", function (event) {
            const token = document.getElementById("cf_turnstile_response").value;

            if (!captchaValidated || !token) {
                console.error("Error: CAPTCHA no validado.");
                alert("Por favor, completa el CAPTCHA antes de enviar el formulario.");
                event.preventDefault(); // Evitar envío si no hay CAPTCHA
                return;
            }

            console.log("Formulario enviado con éxito.");
        });

        // Inicializar el botón como deshabilitado
        submitButton.disabled = true;
        console.log("Botón deshabilitado por defecto."); // Debug
    }

    // ====== BLOQUE PARA CERRAR EL MODAL ======
    const modalElement = document.getElementById("resumeModal");

    // Verificar si el modal existe
    if (modalElement) {
        const bootstrapModal = new bootstrap.Modal(modalElement);
        const downloadButtons = document.querySelectorAll("#downloadEnglish, #downloadSpanish");

        if (downloadButtons.length > 0) {
            downloadButtons.forEach(button => {
                button.addEventListener("click", () => {
                    bootstrapModal.hide(); // Cierra el modal
                });
            });
        }
    }
});
