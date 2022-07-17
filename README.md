# Stockholm
Proyecto desarrollado durante el BootCamp de ciberseguridad que organizo 42 Barcelona en julio 2022.

Es un programa en Python que encripta mediante AES (CBC MODE) los ficheros contenidos en el directorio HOME/infection (en el caso de existir).

Las extensiones de los ficheros que se encriptan coinciden con las extensiones que tenían los ficheros que en su momento fueron afectados por WannaCry 

Para probarlo se ha creado una imagen Docker que tiene como base Ubuntu y tiene instalados un servidor SSH y un servidor FTP (puertos 4242 y 4141 respectivamente). La imagen se encuentra en hub.docker.com

docker pull danirequena/mysandbox:1.5

La imagen contiene:

[+] El ejecutable stockholm (one_file, no requiere de python)

[+] Un usuario creado jorequen y contraseña password1

[+] Dentro de home/jorequen hay un directorio /infection con diferentes ficheros víctima

Se adjunta el dockerfile por si no se quiere descargar

# Instrucciones de uso

[+] Lanzamos el contenedor usando la imagen descargada

docker run -d -p 4242:4242 -p 4141:4141 danirequena/mysandbox:1.5

[+] Nos conectamos al contenedor mediante SSH con las credenciales (jorequen/password1)

[+] Ejecutamos ./stockholm

Solo se encriptaran y se les añadirá la extension .ft a los ficheros contenidos en el directorio $HOME/infection y que tengan una extension que coincida con alguna de las extensiones que afectaba WannaCry

[+] Para desencriptar los ficheros y dejarlos en su estado original ejecutamos 

./stockhold -r aXde5Ffg6RdE4Jno

[+] Las intrucciones 

./stockholm -h 


