# Dockerfile para reproducir el Experimento de Parsers
# Soporta: Python (ANTLR4), C# (ANTLR4), C (Flex+Bison)

FROM python:3.13-slim

# Etiquetas de metadatos
LABEL maintainer="Equipo Compiladores"
LABEL description="Experimento de Carga y Evaluación de Rendimiento de Parsers (YAML/Docker Compose)"

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Java para ANTLR4
    default-jdk-headless \
    # Herramientas C (Flex + Bison + GCC)
    gcc \
    make \
    flex \
    bison \
    # .NET SDK para C#
    dotnet-sdk-8.0 \
    # Utilidades generales
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Establecer directorio de trabajo
WORKDIR /app

# Copiar los archivos del experimento
COPY . .

# Instalar dependencias Python
RUN pip install --no-cache-dir -r src/antlr_python/requirements.txt

# Compilar el parser en C (Flex + Bison)
RUN cd src/bison_c && \
    make clean && \
    make && \
    cd /app

# Compilar el parser en C# (.NET)
RUN cd src/antlr_csharp && \
    dotnet build -c Release && \
    cd /app

# Crear directorio de resultados si no existe
RUN mkdir -p results

# Comando por defecto: ejecutar el experimento
CMD ["python", "scripts/run_experiment.py"]

# Etiqueta de instrucciones para ejecutar
# docker build -t parser-experiment .
# docker run parser-experiment
# docker run -v $(pwd)/results:/app/results parser-experiment  # Para extraer resultados
