# TADA
Telemetry and data adquisition

14/01/2021
Creación de la primera version del programa "gui" junto a una interfaz simple con los datos "Velocidad actual", "Velocidad máxima", "Estado" y un recuadro con los datos recibidos, además de un botón que al ser pulsado activa una función (comprobar) que lee los datos del Xbee.
Tambien se ha incluido un archivo llamado "telemetry" que envía datos por uno de los Xbee.

16/01/2021
Se ha añadido una función (end_serial.in_waiting) que evita que el programa se congele al leer datos si el buffer del Xbee no contiene ninguno.

18/01/2021
Ahora el archivo "telemetry" (desde el que se envían los datos) envía un numero modificable de datos aleatorios.
En cuanto al archivo "gui", se ha añadido una variable global "sigue" que ayuda, junto a los botones "recibir" y "parar", a cancelar o reanudar la lectura de los datos procedentes del Xbee. Se ha creado un bucle que se activa al pulsar "recibir" y lee todos los datos del Xbee (eliminando primero el buffer que hubiera) hasta que se pulse el botón "parar", que cambiará la variable global "sigue" del valor True al valor False.
A partir de ahora cuando se pulse el botón "recibir" no llamará a la función comprobar, si no que llamará a una nueva llamada "continuar" que como he mencionado antes cambiará el valor de "sigue" y ahora sí llamará a la función "comprobar".
Por último se ha añadido una llamada recursiva al final de la función "comprobar" que se activará si la variable global "sigue" tiene el valor True y se ha creado un nuevo frame para organizar los botones.