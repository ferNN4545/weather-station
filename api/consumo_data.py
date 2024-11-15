import random
import time
import requests


# Configuración de ThingSpeak con tus claves
THINGSPEAK_API_KEY = "B9QU7G5SDJMCQJYR"  # Tu clave de escritura para ThingSpeak
THINGSPEAK_URL = "https://api.thingspeak.com/update"


# Dispositivos a monitorear
devices = {
    "Fridge": 0,        # Consumo de la nevera (en vatios)
    "Washing Machine": 0,  # Consumo de la lavadora (en vatios)
    "Shower": 0,        # Consumo de la ducha eléctrica (en vatios)
    "Computer": 0,      # Consumo de la computadora (en vatios)
    "TV": 0,            # Consumo del televisor (en vatios)
}


while True:
    # Generar valores aleatorios de consumo eléctrico en vatios (W) para cada dispositivo
    devices["Fridge"] = random.uniform(80, 150)  # Frigorífico consume entre 80 y 150 W
    devices["Washing Machine"] = random.uniform(500, 1500)  # Lavadora consume entre 500 y 1500 W
    devices["Shower"] = random.uniform(1500, 3000)  # Ducha eléctrica consume entre 1500 y 3000 W
    devices["Computer"] = random.uniform(50, 300)  # Computadora consume entre 50 y 300 W
    devices["TV"] = random.uniform(100, 400)  # Televisor consume entre 100 y 400 W


    # Preparar los datos para enviar a ThingSpeak
    payload = {
        "api_key": THINGSPEAK_API_KEY,
        "field1": devices["Fridge"],        # Consumo de la nevera
        "field2": devices["Washing Machine"],  # Consumo de la lavadora
        "field3": devices["Shower"],        # Consumo de la ducha eléctrica
        "field4": devices["Computer"],      # Consumo de la computadora
        "field5": devices["TV"],            # Consumo del televisor
    }


    # Enviar datos a ThingSpeak
    response = requests.post(THINGSPEAK_URL, params=payload)


    # Comprobar si el envío fue exitoso
    if response.status_code == 200:
        print(f"Datos enviados: "
              f"Fridge = {devices['Fridge']:.2f} W, "
              f"Washing Machine = {devices['Washing Machine']:.2f} W, "
              f"Shower = {devices['Shower']:.2f} W, "
              f"Computer = {devices['Computer']:.2f} W, "
              f"TV = {devices['TV']:.2f} W")
    else:
        print("Error al enviar los datos a ThingSpeak:", response.status_code)


    # Esperar 3 segundos antes de la siguiente medición
    time.sleep(3)


