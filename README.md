# 🟩 Sistema de Auditoría de Código y Consumo Energético

Este sistema utiliza un script de auditoría desacoplado
(`emissions_runner.py`) para medir el consumo energético de cualquier
proyecto Python **sin modificar tu código fuente**.

## 📂 Estructura del Proyecto

    MI-PROYECTO-ECO/
    │
    ├── .github/workflows/
    │   └── eco-pipeline.yml     <-- Automatización
    │
    ├── emissions_runner.py      <-- 🛠️ HERRAMIENTA DE AUDITORÍA (Reutilizable)
    ├── main.py                  <-- 📦 TU PROYECTO (Limpio, sin código de test)
    │
    ├── docker-compose.yml       <-- Infraestructura SonarQube
    ├── sonar-project.properties <-- Configuración Sonar
    └── README.md

## 🚀 Cómo funciona el desacople

### Tu código (`main.py`)

Código puro, sin librerías de medición ni lógica extra.

### El Runner (`emissions_runner.py`)

Script genérico que ejecuta tu programa dentro de un monitor energético.

**Uso:**

    python emissions_runner.py <archivo_a_auditar>

### El Pipeline (GitHub Actions)

Ejecuta el runner en lugar de tu app, sin tocar tu código.

## ⚠️ Prerrequisito en Linux (para SonarQube / Elasticsearch)

### Configuración temporal:

    sudo sysctl -w vm.max_map_count=262144

### Configuración permanente:

1.  Edita:

        sudo nano /etc/sysctl.conf

2.  Añade:

        vm.max_map_count=262144

3.  Aplica cambios:

        sudo sysctl -p

## 1️⃣ Levantar SonarQube (Local)

    docker-compose up -d

Accede a: http://localhost:9000\
Usuario: admin\
Contraseña: admin

## 2️⃣ Configuración del Proyecto en SonarQube

1.  Create Project → Manually\
2.  Rellena:
    -   Display Name: Eco Hello World
    -   Project Key: eco-helloworld
    -   Main Branch: main
3.  Genera token "GithubToken"
4.  Selecciona "Other" + "Linux"

📌 El Project Key debe coincidir con `sonar.projectKey` del archivo
`sonar-project.properties`.

## 3️⃣ Configuración de Ngrok

### Instalar

-   macOS:

        brew install ngrok/ngrok/ngrok

-   Windows:

        choco install ngrok

### Autenticar:

    ngrok config add-authtoken TU_TOKEN_AQUI

### Exponer SonarQube:

    ngrok http 9000

Copia la URL HTTPS generada.

## 4️⃣ Secretos en GitHub

  Nombre           Valor
  ---------------- -----------------------------
  SONAR_TOKEN      Token generado en SonarQube
  SONAR_HOST_URL   URL HTTPS de ngrok

## 5️⃣ Funcionamiento del Sistema

1.  Haces un push\
2.  GitHub Actions instala dependencias\
3.  Ejecuta tu script mediante el runner\
4.  Genera `emissions.csv`\
5.  Sube artefacto\
6.  Envía calidad de código a SonarQube mediante ngrok

------------------------------------------------------------------------