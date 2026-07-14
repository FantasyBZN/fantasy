import os
import json
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json"
}

def sync():
    print("Iniciando sincronização dos dados do Cartola FC...")
    
    # Garante a pasta data
    os.makedirs("data", exist_ok=True)

    # 1. Busca Status do Mercado
    print("Buscando status do mercado...")
    try:
        r = requests.get("https://api.cartolafc.globo.com/mercado/status", headers=HEADERS, timeout=15)
        r.raise_for_status()
        with open("data/status.json", "w", encoding="utf-8") as f:
            json.dump(r.json(), f, ensure_ascii=False, indent=2)
        print("Status do mercado salvo em data/status.json")
    except Exception as e:
        print(f"Erro ao buscar status do mercado: {e}")

    # 2. Busca Atletas do Mercado
    print("Buscando atletas do mercado...")
    try:
        r = requests.get("https://api.cartolafc.globo.com/atletas/mercado", headers=HEADERS, timeout=20)
        r.raise_for_status()
        with open("data/players.json", "w", encoding="utf-8") as f:
            json.dump(r.json(), f, ensure_ascii=False, indent=2)
        print("Atletas salvos em data/players.json")
    except Exception as e:
        print(f"Erro ao buscar atletas do mercado: {e}")

    # 3. Busca Atletas Pontuados (Scouts)
    print("Buscando pontuações da rodada...")
    try:
        r = requests.get("https://api.cartolafc.globo.com/atletas/pontuados", headers=HEADERS, timeout=20)
        r.raise_for_status()
        with open("data/scores.json", "w", encoding="utf-8") as f:
            json.dump(r.json(), f, ensure_ascii=False, indent=2)
        print("Pontuações salvas em data/scores.json")
    except Exception as e:
        print(f"Erro ao buscar pontuações: {e}")

    print("Sincronização do GitHub finalizada!")

if __name__ == "__main__":
    sync()
