function emite_alerta_python() {
    alert("Python Rocks!!");
}
function emite_alerta_django() {
    alert("Django Rocks!!");
}

logo_python = document.getElementsByTagName("img")[0]
logo_python.onclick = emite_alerta_python;

logo_django = document.getElementsByTagName("img")[1]
logo_django.onclick = emite_alerta_django;
