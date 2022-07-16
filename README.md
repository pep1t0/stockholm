# stockholm
Se trata de un proyecto desarrollado durante el BootCamp de ciberseguridad que organizo 42 Barcelona en julio 2022.

Es un programa en Python que encripta mediante AES (CBC MODE) los ficheros contenidos en el directorio HOME/infection (en el caso de existir).

El tipo de fichero a encriptar coincide con los tipos que afecto en su momento WannaCry 

Para probarlo se ha creado una imagen en hub.docker.com  

docker pull danirequena/mysandbox:1.5

La imagen contiene:

[+] El ejecutable stockholm (one_file, no requiere de python)
[+] Un usuario creado jorequen y contraseña password1
[+] Dentro de home/jorequen hay un directorio /infection con diferentes ficheros víctima

Se adjunta el dockerfile por si no se quiere descargar

# uso

Podemos conectarnos al servidor mediante SSH con las credenciales (jorequen/password1) y ejecutar ./stockholm
