# Sistema distribuido de extracción de noticias (Master-Worker)

## ¿Qué hace este programa?

Este proyecto implementa un sistema distribuido asincrónico para la extracción y procesamiento de noticias desde diferentes fuentes online, utilizando una 

arquitectura de tipo Master-Worker. El objetivo es simular un sistema de adquisición de datos en nodos geográficos diferentes (Madrid, Londres, São Paulo), con un 

servidor central ubicado en Frankfurt que recibe y gestiona los artículos extraídos.


## ¿Cómo se ejecuta?

1) Abre una terminal y ejecuta:


cd ruta/al/proyecto/central

python server.py


2) Abre otra terminal, navega a la raíz del proyecto y ejecuta:


cd ruta/al/proyecto

python -m master.main


3) Verás en la terminal del servidor central mensajes como:

[CENTRAL] Recibidos 152 artículos de Madrid (https://feeds.elpais.com/...)


4) Y en la terminal del nodo maestro:

[Madrid] 152 artículos extraídos desde https://feeds.elpais.com/...

[Madrid] Artículos enviados al servidor central.

[MASTER] 152 artículos recibidos de Madrid





