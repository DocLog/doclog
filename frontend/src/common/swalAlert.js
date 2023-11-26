import Swal from "sweetalert2";

export function showAlert(message, icon){
    Swal.fire({
        title: "Mensagem",
        text: message,
        icon: icon,
        confirmButtonText: 'OK'
    })
}