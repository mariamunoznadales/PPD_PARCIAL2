import aiohttp
from common.utils import fetch_data, parse_data

CENTRAL_SERVER_URL = "http://localhost:8080/api/articulos"

async def procesar_fuente(task):
    async with aiohttp.ClientSession() as session:
        raw = await fetch_data(session, task.fuente_url)
        if raw:
            articulos = parse_data(raw)
            print(f"[{task.nodo_origen}] {len(articulos)} artículos extraídos desde {task.fuente_url}")

            # Enviar al servidor central
            payload = {
                "nodo": task.nodo_origen,
                "fuente": task.fuente_url,
                "articulos": articulos
            }
            try:
                async with session.post(CENTRAL_SERVER_URL, json=payload) as response:
                    if response.status == 200:
                        print(f"[{task.nodo_origen}] Artículos enviados al servidor central.")
                    else:
                        print(f"[{task.nodo_origen}] Error al enviar artículos: {response.status}")
            except Exception as e:
                print(f"[{task.nodo_origen}] Excepción al enviar artículos: {e}")

            return {"nodo": task.nodo_origen, "articulos": articulos, "fuente": task.fuente_url}
        else:
            print(f"[{task.nodo_origen}] Fallo al obtener datos de {task.fuente_url}")
            return {"nodo": task.nodo_origen, "articulos": [], "fuente": task.fuente_url, "fallo": True}
