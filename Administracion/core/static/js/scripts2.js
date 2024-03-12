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