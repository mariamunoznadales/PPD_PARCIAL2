from aiohttp import web

async def recibir_articulos(request):
    try:
        datos = await request.json()
    except Exception as e:
        return web.Response(status=400, text=f"Error al parsear JSON: {e}")

    nodo = datos.get("nodo", "desconocido")
    fuente = datos.get("fuente", "desconocida")
    articulos = datos.get("articulos", [])

    print(f"[CENTRAL] Recibidos {len(articulos)} artículos de {nodo} ({fuente})")
    return web.Response(status=200, text="Recibido OK")

app = web.Application()
app.router.add_post("/api/articulos", recibir_articulos)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8080)
