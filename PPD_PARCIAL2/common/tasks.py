from dataclasses import dataclass

@dataclass
class ExtractionTask:
    id: int
    fuente_url: str
    nodo_origen: str
