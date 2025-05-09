import aiohttp
import json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

async def fetch_data(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            return await response.text()
    except Exception as e:
        print(f"Error al obtener datos de {url}: {e}")
        return None

def parse_data(raw_data):
    try:
        return parse_json(raw_data)
    except:
        try:
            return parse_xml(raw_data)
        except:
            return parse_html(raw_data)

def parse_json(data):
    parsed = json.loads(data)
    return [
        {
            "titulo": a.get("title", "sin título"),
            "fecha": a.get("date", "sin fecha"),
            "contenido": a.get("content", "sin contenido")
        } for a in parsed
    ]

def parse_xml(data):
    root = ET.fromstring(data)
    return [
        {
            "titulo": item.findtext("title", "sin título"),
            "fecha": item.findtext("pubDate", "sin fecha"),
            "contenido": item.findtext("description", "sin contenido")
        } for item in root.findall(".//item")
    ]

def parse_html(data):
    soup = BeautifulSoup(data, "html.parser")
    articles = []
    for article in soup.find_all("article"):
        titulo = article.find("h1") or article.find("h2")
        fecha = article.find("time")
        contenido = article.find("p")
        articles.append({
            "titulo": titulo.text if titulo else "sin título",
            "fecha": fecha["datetime"] if fecha and fecha.has_attr("datetime") else "sin fecha",
            "contenido": contenido.text if contenido else "sin contenido"
        })
    return articles
