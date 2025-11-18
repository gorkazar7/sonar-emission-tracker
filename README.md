Emission2025-

Sistema de Auditoría de Código y Consumo Energético

Este sistema ejecuta un análisis de calidad y una medición de huella de carbono cada vez que haces un git push.

⚠️ Prerrequisito Importante para Linux

Si estás en Linux (Ubuntu, Debian, WSL2, etc.), es muy probable que veas el error:
max virtual memory areas vm.max_map_count [65530] is too low

SonarQube usa Elasticsearch, el cual requiere más memoria virtual de la que Linux trae por defecto. Debes aumentar este límite en tu máquina host (tu PC):

Temporal (se pierde al reiniciar PC):

sudo sysctl -w vm.max_map_count=262144


Permanente:
Edita el archivo /etc/sysctl.conf y añade esta línea al final:

vm.max_map_count=262144


Luego recarga la configuración con: sudo sysctl -p

1. Levantar SonarQube (Local)

Ejecuta el siguiente comando para iniciar el servidor de calidad:

docker-compose up -d


Accede a http://localhost:9000 (User: admin, Pass: admin y cámbialo).

2. Configuración del Proyecto

Crea un proyecto en SonarQube llamado "Eco Hello World".

Genera un Token de análisis.

Copia el archivo sonar-project.properties a la raíz de tu código.

3. Conectar GitHub con tu Sonar Local

GitHub Actions corre en la nube, tu Docker corre en tu PC. Tienes dos opciones:

Opción A (Recomendada para pruebas): Usar ngrok para exponer tu puerto 9000 a internet.

ngrok http 9000

Copia la URL generada (ej: https://xyz.ngrok.io).

Opción B (Producción): Usar SonarCloud.io en lugar de Docker local.

4. Configurar Secretos en GitHub

Ve a tu repositorio en GitHub -> Settings -> Secrets and variables -> Actions -> New Repository Secret:

SONAR_TOKEN: El token que generaste en el paso 2.

SONAR_HOST_URL: Tu URL de ngrok o SonarCloud (ej: https://xyz.ngrok.io).

5. Funcionamiento

Haces un cambio en el código (main_measured.py).

Haces git push.

GitHub Actions arranca:

Instala codecarbon.

Ejecuta tu script y genera emissions.csv (Mide CO2 y Energía).

Sube el CSV para que lo puedas descargar.

Envía el código a SonarQube para ver si tienes "Code Smells" o errores.
