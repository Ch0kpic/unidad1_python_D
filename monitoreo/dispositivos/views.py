from django.shortcuts import render

# Create your views here.

def panel_dispositivos(request):
    dispositivos = [
        {"nombre": "Sensor Temperatura", "consumo": 100},
        {"nombre": "Medidor Solar", "consumo": 120},
        {"nombre": "Sensor Movimiento", "consumo": 30},
        {"nombre": "Calefactor", "consumo": 200},
    ]

    consumo_maximo = 100

    dispositivos_rojos = [d for d in dispositivos if d["consumo"] > consumo_maximo]
    contador_rojos = len(dispositivos_rojos)

    return render(request, "dispositivos/panel.html" , {
        "dispositivos": dispositivos,
        "consumo_maximo": consumo_maximo,
        "contador_rojos": contador_rojos,
    })