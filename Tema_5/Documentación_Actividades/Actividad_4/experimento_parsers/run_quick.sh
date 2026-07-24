#!/bin/bash
# Script rápido para ejecutar el experimento de parsers
# Funciona en Linux, macOS y WSL

set -e  # Salir en caso de error

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$SCRIPT_DIR"

echo "╔════════════════════════════════════════════════════╗"
echo "║  Experimento de Parsers - Modo Rápido             ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

# Verificar dependencias básicas
echo "⚙️  Verificando dependencias..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado"
    exit 1
fi
echo "✅ Python 3 disponible"

# Instalar dependencias Python si es necesario
echo ""
echo "📦 Instalando dependencias Python..."
pip3 install -q -r "$PROJECT_DIR/src/antlr_python/requirements.txt" || {
    echo "⚠️  Advertencia: No se pudieron instalar todas las dependencias"
}

# Generar archivos de prueba si no existen
if [ ! -f "$PROJECT_DIR/test_files/docker_compose_01.yml" ]; then
    echo ""
    echo "🔨 Generando archivos de prueba sintéticos..."
    python3 "$PROJECT_DIR/scripts/generate_test_files.py"
fi

# Ejecutar experimento
echo ""
echo "⏱️  Ejecutando experimento de carga..."
python3 "$PROJECT_DIR/scripts/run_experiment.py"

# Generar gráficas
echo ""
echo "📊 Generando gráficas de resultados..."
python3 "$PROJECT_DIR/scripts/plot_results.py"

echo ""
echo "╔════════════════════════════════════════════════════╗"
echo "║  ✅ Experimento completado                         ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""
echo "📁 Resultados guardados en: $PROJECT_DIR/results/"
echo "   - times.csv"
echo "   - parse_time_comparison.png"
echo "   - total_time_comparison.png"
echo ""
