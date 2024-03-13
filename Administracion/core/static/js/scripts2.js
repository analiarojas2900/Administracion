function mostrarCargaArchivo() {
    var tieneCopia = document.querySelector('input[name="copiaCarnet"]:checked').value;
    var campoArchivo = document.getElementById('labelArchivo');

    if (tieneCopia === 'Si') {
        campoArchivo.style.display = 'inline-block';
        document.getElementById('archivoCarnet').style.display = 'inline-block';
    } else {
        campoArchivo.style.display = 'none';
        document.getElementById('archivoCarnet').style.display = 'none';
    }
}


$(document).ready(function() {
    $(".datepicker").datepicker({
        dateFormat: 'dd/mm/yy'
    });
});


function separarRut(rutCompleto) {
    var rut = rutCompleto.substring(0, rutCompleto.length - 2);
    var dv = rutCompleto.substring(rutCompleto.length - 2);
    rut = rut.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    document.getElementById("rut").value = rut;
    document.getElementById("dv").value = dv;
}


document.getElementById("sueldoBase").addEventListener("input", function(event) {
    var sueldo = event.target.value;
    if (sueldo && !sueldo.includes("$")) {
        var sueldoNumerico = parseInt(sueldo.replace(/\D/g,'')); // Elimina caracteres no numéricos
        sueldo = "$" + sueldoNumerico.toLocaleString('es-CL'); // Añade el símbolo de peso y formatea el número como CLP
        event.target.value = sueldo.replace(/,/g, 'G'); // Reemplaza las comas por 'G'
    }
});
