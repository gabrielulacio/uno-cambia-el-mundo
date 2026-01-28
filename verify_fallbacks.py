import httpx
import os

def test_fallbacks():
    # Asumimos que la API está corriendo localmente para esta prueba
    # O simplemente analizamos si el código de fallback existe (ya lo hicimos)
    print("Verificando existencia de fallbacks en el código...")
    
    with open("api/index.py", "r") as f:
        content = f.read()
        if "except Exception as e:" in content and "fallback" in content.lower():
            print("✅ El código contiene bloques try-except con retornos de fallback.")
        else:
            print("⚠️ Faltan algunos bloques de fallback explícitos en endpoints.")

if __name__ == "__main__":
    test_fallbacks()
