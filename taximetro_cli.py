# importar librerias 
import time
import os

# Tarifas
TARIFA_PARADO = 0.02
TARIFA_MOVIMIENTO = 0.05

#definir funciones 

def bienvenida():
    print("Bienvenido al Taxímetro Digital (versión CLI)")
    print("Este programa calcula el costo de un trayecto de taxi según el tiempo:")
    print("Parado: 2 céntimos por segundo")
    print("Movimiento: 5 céntimos por segundo")
    print("Comandos disponibles durante el trayecto:")
    print("[p] Cambiar a Parado")
    print("[m] Cambiar a Movimiento")
    print("[f] Finalizar trayecto")
    print("[q] Salir del programa")
    print("-" * 50)

def iniciar_trayecto():
    total = 0.0
    estado_actual = None
    inicio = None

    while True:
        cmd = input(">> Ingrese comando (p/m/f/q): ").lower()

        if cmd in ['p', 'm']:
            ahora = time.time()
            if estado_actual and inicio:
                duracion = int(ahora - inicio)
                tarifa = TARIFA_PARADO if estado_actual == "p" else TARIFA_MOVIMIENTO
                costo = duracion * tarifa
                total += costo
                print(f"Estado '{estado_actual}' por {duracion}s → +{costo:.2f}€ (Total: {total:.2f}€)")
            estado_actual = cmd
            inicio = ahora
            print(f"Cambiado a {'Parado' if cmd == 'p' else 'Movimiento'}")

        elif cmd == 'f':
            ahora = time.time()
            if estado_actual and inicio:
                duracion = int(ahora - inicio)
                tarifa = TARIFA_PARADO if estado_actual == "p" else TARIFA_MOVIMIENTO
                costo = duracion * tarifa
                total += costo
                print(f"Último estado '{estado_actual}' por {duracion}s → +{costo:.2f}€")
            print(f"Trayecto finalizado. Total a pagar: {total:.2f}€")
            break

        elif cmd == 'q':
            print("👋 Saliendo del programa...")
            exit()

        else:
            print("Comando no reconocido. Usa: p, m, f, q")

def main():
    bienvenida()
    while True:
        iniciar_trayecto()
        repetir = input("¿Iniciar un nuevo trayecto? (s/n): ").lower()
        if repetir != 's':
            print("Gracias por usar el Taxímetro Digital.")
            break

# Ejecutar el programa
if __name__ == "__main__":
    main()
