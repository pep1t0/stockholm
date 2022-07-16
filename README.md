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

[+] Lanzamos el contenedor usando la imagen descargada
docker run -d -p 4242:4242 -p 4141:4141 danirequena/mysandbox:1.5 
[+] Nos conectamos al contenedor mediante SSH con las credenciales (jorequen/password1)
[+] Ejecutamos ./stockholm
Los ficheros contenidos en el directorio /home/jorequen/infection con extensiones coincidentes a las extensiones de WannaCry se encriptan y se les añade la extension .ft
[+] Para desencriptar los ficheros y dejarlos en su estado original ejecutamos ./stockhold -r aXde5Ffg6RdE4Jno
[+] Las intrucciones ./stockholm -h 


