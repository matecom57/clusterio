# Usar `ssh-keygen` para no tener que escribir passwords


Cuando te conectas a una PC mediante ssh, te pide un password. Lógico. Pero cuando te conectas a la misma PC a cada rato, escribir passwords se vuelve tedioso. No habrá una manera de que la máquina destino ya te conozca y no te ande preguntando quién eres a cada rato? 

Claro que hay manera! y se llama `ssh-keygen`. Puedes consultar la documentación completa en la [página oficial](https://www.ssh.com/academy/ssh/keygen). Pero por lo pronto, veamos lo más básico.


Para este tutorial, usaremos una computadora `origen` que es donde estamos trabajando, y una `destino` que es a la que queremos conectarnos. La PC `destino` puede estar dentro del cluster, o ser cualquier computadora del mundo a la que tenemos accesso mediante ssh. Si trabajas en la NASA y tienes acceso, bien por tí.

## Generar la llave
Esta llave se guardará en tu home, y será usada para "abrir la puerta" de la computadora destino. En la computadora `origen` usamos:

    ssh-keygen

Te preguntará dónde quieres grabarla, siendo el default to home. Sugiero que no le muevas. Te pedirá también un _passphrase_ opcional. Puedes escribirlo si quieres, pero no vayas a olvidarlo!


## Copiar la llave al destino
Ahora que ya tenemos cómo identificarnos, enviaremos nuestra llave personal a la PC `destino`, y nos pedirá nuestra contraseña por última vez para verificar que somos quienes decimos ser. La próxima vez que queremos entrar a `destino`, esa PC revisará primero las llaves que ya tiene, y si coincide con el usuario y PC `origen`, dejará entrar sin más preguntas. Yeah!  Copiemos nuestra llave con el comando:

    ssh-copy-id usuario@destino

Donde `usuario` es el nombre de usuario que tengamos en la PC `destino`. (más info sobre este comando [aquí](https://www.ssh.com/academy/ssh/copy-id#:~:text=ssh%2Dcopy%2Did%20installs%20an,tool%20is%20part%20of%20OpenSSH.))

Y listo! La próxima vez que hagamos `ssh usuario@destino` entraremos sin más ni más!

:warning: OBVIO: NO COMPARTAS TU LLAVE.


