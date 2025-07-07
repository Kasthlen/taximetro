# taxímetro
Primer ejercicio usando python en el modulo 1 del bootcamp de inteligencia artificial 

#  Taxímetro Digital

Este proyecto implementa un taxímetro digital básico utilizando Python y la librería Tkinter para la interfaz gráfica de usuario (GUI). Permite simular el cálculo de tarifas de un trayecto en función del tiempo parado y en movimiento, así como registrar los trayectos finalizados en un archivo CSV.

## Características

* Interfaz gráfica intuitiva.
* Cálculo de tarifas en tiempo real (simulado por tiempo transcurrido).
* Estados "Parado" y "Movimiento".
* Registro de trayectos con fecha, hora y costo total.
* Opción para iniciar un nuevo trayecto.

## Instalación y Ejecución

1.  **Clonar el repositorio:**
    ```bash
    git clone (https://github.com/Kasthlen/taximetro.git)
    ```
2.  **Asegúrate de tener Python instalado.** (Versión recomendada: Python 3.x)
3.  **Ejecutar la aplicación:**
    ```bash
    python taximetro_gui.py OR
    pytthon taximetro_cli.py
    ```

## Uso

1.  Al iniciar la aplicación, el estado es "Inactivo" y el total es 0.00 €.
2.  Haz clic en "Movimiento" para iniciar el conteo en movimiento.
3.  Haz clic en "Parado" para cambiar al estado de parado.
4.  El "Total" se actualizará continuamente.
5.  Haz clic en "Finalizar Trayecto" para ver el costo final y guardar el registro.
6.  Haz clic en "Nuevo Trayecto" para reiniciar y comenzar un nuevo viaje.

## Archivo de Registros

Los trayectos finalizados se guardan en el archivo `registros_taximetro.csv` en el mismo directorio de la aplicación.

## Anexos

1. Link trello: https://trello.com/b/EbdpBjcz/taximetro
2. Link Canva: https://www.canva.com/design/DAGsdyVVvjI/6oURlapBhFPLbrd_XG22sg/edit?utm_content=DAGsdyVVvjI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Contribución

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar la aplicación, no dudes en abrir un "issue" o enviar un "pull request".
