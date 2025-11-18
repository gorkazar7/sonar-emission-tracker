import time
import math
from codecarbon import EmissionsTracker

# Configuración del tracker
# project_name: Nombre para identificarlo en los reportes
# measure_power_secs: Cada cuánto mide el consumo (default 15s)
tracker = EmissionsTracker(project_name="HelloWorld_Eco_Check", output_dir=".", measure_power_secs=1)


def tarea_intensiva():
    """
    Simulamos una carga de trabajo. Un simple print es tan rápido
    que el consumo energético es casi indetectable.
    Haremos calculos matemáticos para estresar la CPU brevemente.
    """
    print("--- Iniciando Proceso Hello World ---")
    size = 10000
    # Operación matemática para generar consumo de CPU
    data = [math.sqrt(i) * math.sin(i) for i in range(size)]
    print(f"Calculados {len(data)} valores.")
    time.sleep(2)  # Simulamos tiempo de espera de I/O
    print("--- Fin del Proceso ---")


if __name__ == "__main__":
    # 1. Iniciar medición
    tracker.start()

    try:
        # 2. Ejecutar tu código
        tarea_intensiva()
    finally:
        # 3. Parar medición y guardar resultados
        emissions = tracker.stop()

        print(f"\n[REPORTE ECO]")
        print(f"Emisiones CO2: {emissions} kg")
        # CodeCarbon guarda automáticamente un archivo emissions.csv