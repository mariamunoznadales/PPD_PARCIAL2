import asyncio
from common.tasks import ExtractionTask
from worker.worker import procesar_fuente

FUENTES = {
    "Madrid": [
        "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada",
        "https://www.abc.es/rss/feeds/abcPortada.xml"
    ],
    "Londres": [
        "https://feeds.bbci.co.uk/news/rss.xml"
    ],
    "São Paulo": [
        "https://g1.globo.com/rss/g1/",
        "https://rss.uol.com.br/feed/noticias.xml"
    ]
}

async def master():
    tareas = []
    task_id = 1
    for nodo, urls in FUENTES.items():
        for url in urls:
            tarea = ExtractionTask(id=task_id, fuente_url=url, nodo_origen=nodo)
            tareas.append(procesar_fuente(tarea))
            task_id += 1

    resultados = await asyncio.gather(*tareas, return_exceptions=True)

    for resultado in resultados:
        if isinstance(resultado, dict):
            if resultado.get("fallo"):
                print(f"[MASTER] Fallo en {resultado['fuente']} (nodo: {resultado['nodo']})")
            else:
                print(f"[MASTER] {len(resultado['articulos'])} artículos recibidos de {resultado['nodo']}")
        else:
            print(f"[MASTER] Error inesperado: {resultado}")

if __name__ == "__main__":
    asyncio.run(master())
