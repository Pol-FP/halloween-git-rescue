# main.py - Sistema de Monitorització de la Sala de Servidors
import os
import sys

def init_system():
    print("[SISTEMA]: Inicialitzant la línia de defensa de producció...")
    print("[SISTEMA]: Estat inicial: Estable.")

def emergency_lockdown():
    print("[SEGURETAT]: Activant protocol de tancament d'emergència...")
    print("[SEGURETAT]: Totes les sortides de l'edifici han estat segellades.")

if __name__ == "__main__":
    init_system()
    emergency_lockdown()
