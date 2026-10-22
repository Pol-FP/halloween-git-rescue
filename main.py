# main.py - Sistema de Monitorització de la Sala de Servidors
import os
import sys

def init_system():
    print("[SISTEMA]: Inicialitzant la línia de defensa de producció...")
    print("[SISTEMA]: Estat inicial: Estable.")

def emergency_lockdown():
    print("[SANCTUARY]: Activant protocol de tancament d'emergència...")
    print("[SANCTUARY]: Totes les sortides de l'edifici han estat segellades.")

def check_temperature_anomalies():
    print("[SENSORS]: Verificant temperatura ambient...")
    # Alerta paranormal de la narrativa
    current_temp = -5.0 
    print(f"[ALERTA]: Temperatura actual de la sala: {current_temp}°C")
    if current_temp < 0:
        print("[CRÍTIC]: Presència freda detectada. Possible bretxa temporal.")

if __name__ == "__main__":
    init_system()
    emergency_lockdown()
    check_temperature_anomalies()
