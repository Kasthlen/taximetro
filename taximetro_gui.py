#importar librerias
import tkinter as tk #interfaces gráficas como botones, ventanas, etc...
from tkinter import messagebox #ALERT!! mensajes para el usuario
import time # cuenta el tiempo, segundos
import csv #lee y escribe archivos .csv
from datetime import datetime #fecha y hora actual

# Constantes de tarifas
TARIFA_PARADO = 0.02   # € por segundo
TARIFA_MOVIMIENTO = 0.05   # € por segundo

# Archivo de registro
ARCHIVO_REGISTROS = "registros_taximetro.csv"

class TaximetroApp:
    def __init__(self, root): #inicia la app
        self.root = root
        self.root.title("🟢 Taxímetro Digital")

        # Estado inicial
        self.estado = None
        self.inicio_estado = None
        self.total = 0.0

        # Crear interfaz
        self.label_estado = tk.Label(root, text="Estado: Inactivo", font=("Arial", 14))
        self.label_estado.pack(pady=10)

        self.label_total = tk.Label(root, text="Total: 0.00 €", font=("Arial", 16))
        self.label_total.pack(pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        self.btn_parado = tk.Button(btn_frame, text="🛑 Parado", width=12, command=self.parar)
        self.btn_parado.grid(row=0, column=0, padx=5)

        self.btn_movimiento = tk.Button(btn_frame, text="🏃 Movimiento", width=12, command=self.mover)
        self.btn_movimiento.grid(row=0, column=1, padx=5)

        self.btn_finalizar = tk.Button(root, text="✅ Finalizar Trayecto", bg="lightgreen", width=25, command=self.finalizar)
        self.btn_finalizar.pack(pady=10)

        self.btn_nuevo = tk.Button(root, text="🔄 Nuevo Trayecto", bg="lightblue", width=25, command=self.nuevo_trayecto)
        self.btn_nuevo.pack(pady=5)

        self.iniciar_trayecto() # llama a la función que prepara todo apara empezar a contar tiempo y costos.

    def iniciar_trayecto(self): # =iniciar trayecto-
        self.total = 0.0 #el total del trayecto vuelve a 0.
        self.estado = None #el estado actual del taxi se pone como "inactivo"
        self.inicio_estado = None
        self.update_labels() #actualiza los textos en la ventana

    def cambiar_estado(self, nuevo_estado):
        ahora = time.time()
        if self.estado is not None and self.inicio_estado is not None:
            duracion = int(ahora - self.inicio_estado)
            tarifa = TARIFA_PARADO if self.estado == "Parado" else TARIFA_MOVIMIENTO
            costo = duracion * tarifa
            self.total += costo

        self.estado = nuevo_estado
        self.inicio_estado = ahora
        self.update_labels()

    """
    1 calcula cuánto tiempo páso desde el utimo cambio de estado.
    2 calcula el costo por ese tiempo
    3 suma el costo total
    4 cambia el estado actal
    5 actualiza los textos de la pantalla

    """
    def parar(self): # <--- Este método estaba mal indentado
        self.cambiar_estado("Parado")

    def mover(self): # <--- Este método también estaba mal indentado
        self.cambiar_estado("Movimiento")

    def finalizar(self):
        ahora = time.time()
        if self.estado is not None and self.inicio_estado is not None:
            duracion = int(ahora - self.inicio_estado)
            tarifa = TARIFA_PARADO if self.estado == "Parado" else TARIFA_MOVIMIENTO
            costo = duracion * tarifa
            self.total += costo

        self.estado = "Finalizado"
        self.inicio_estado = None
        self.update_labels()

        # Guardar registro
        self.guardar_registro()

        messagebox.showinfo("Trayecto Finalizado", f"Total a pagar: {self.total:.2f} €")
    """
    1 calcula el ultimo tramo
    2 muestra el mensaje con el total a pagar
    3 guarda el trayecto en un archivo .csv
    """

    def nuevo_trayecto(self): #reiniciar todo al decir si
        if messagebox.askyesno("Nuevo Trayecto", "¿Deseas iniciar un nuevo trayecto?"):
            self.iniciar_trayecto()

    def update_labels(self): #actualiza los textos que se muestran en pantalla con el estado actual y el total a pagar
        self.label_estado.config(text=f"Estado: {self.estado if self.estado else 'Inactivo'}")
        self.label_total.config(text=f"Total: {self.total:.2f} €")

    def guardar_registro(self): # guardar los registros tal como lo declaramos
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(ARCHIVO_REGISTROS, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([fecha_hora, f"{self.total:.2f}"])


if __name__ == "__main__":
    root = tk.Tk()
    app = TaximetroApp(root)
    root.mainloop()

    """
    crea la ventana principal (root)
    crea al objeto "app" (.TaximetroApp)
    mantiene la ventana abirta esperando acciones
    """