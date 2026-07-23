# Script rápido para ejecutar el experimento de parsers en Windows
# Uso: .\run_quick.ps1

param(
    [switch]$UseDocker = $false
)

$ErrorActionPreference = "Stop"

Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  Experimento de Parsers - Modo Rápido (Windows)   ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Si se pasa -UseDocker, ejecutar con Docker
if ($UseDocker) {
    Write-Host "🐳 Usando Docker..." -ForegroundColor Yellow
    
    Write-Host "🔨 Construyendo imagen Docker..." -ForegroundColor Yellow
    docker build -t parser-experiment .
    
    Write-Host "⏱️  Ejecutando experimento en Docker..." -ForegroundColor Yellow
    docker run -v ${PWD}/results:/app/results parser-experiment
    
    Write-Host "✅ Experimento completado con Docker" -ForegroundColor Green
    exit 0
}

# Modo local
Write-Host "⚙️  Verificando dependencias..." -ForegroundColor Yellow

# Verificar Python
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Python 3 no está instalado o no está en PATH" -ForegroundColor Red
    Write-Host ""
    Write-Host "Descárgalo desde: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

$pythonVersion = python --version 2>&1
Write-Host "✅ $pythonVersion" -ForegroundColor Green

# Instalar dependencias Python
Write-Host ""
Write-Host "📦 Instalando dependencias Python..." -ForegroundColor Yellow
$requirementsPath = Join-Path $PSScriptRoot "src/antlr_python/requirements.txt"
try {
    python -m pip install -q -r $requirementsPath
    Write-Host "✅ Dependencias instaladas" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Advertencia: No se pudieron instalar todas las dependencias" -ForegroundColor Yellow
}

# Generar archivos de prueba si no existen
$testFileDir = Join-Path $PSScriptRoot "test_files"
$firstTestFile = Join-Path $testFileDir "docker_compose_01.yml"

if (-not (Test-Path $firstTestFile)) {
    Write-Host ""
    Write-Host "🔨 Generando archivos de prueba sintéticos..." -ForegroundColor Yellow
    $generateScript = Join-Path $PSScriptRoot "scripts/generate_test_files.py"
    python $generateScript
}

# Ejecutar experimento
Write-Host ""
Write-Host "⏱️  Ejecutando experimento de carga..." -ForegroundColor Yellow
$runScript = Join-Path $PSScriptRoot "scripts/run_experiment.py"
python $runScript

# Generar gráficas
Write-Host ""
Write-Host "📊 Generando gráficas de resultados..." -ForegroundColor Yellow
$plotScript = Join-Path $PSScriptRoot "scripts/plot_results.py"
python $plotScript

Write-Host ""
Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║  ✅ Experimento completado                         ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""

$resultsPath = Join-Path $PSScriptRoot "results"
Write-Host "📁 Resultados guardados en: $resultsPath" -ForegroundColor Yellow
Write-Host "   - times.csv" -ForegroundColor Gray
Write-Host "   - parse_time_comparison.png" -ForegroundColor Gray
Write-Host "   - total_time_comparison.png" -ForegroundColor Gray
Write-Host ""
Write-Host "💡 Tip: Usa '.\run_quick.ps1 -UseDocker' para ejecutar con Docker" -ForegroundColor Cyan
