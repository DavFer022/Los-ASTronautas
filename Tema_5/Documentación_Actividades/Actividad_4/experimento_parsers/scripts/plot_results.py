import os
import pandas as pd
import matplotlib.pyplot as plt

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    results_dir = os.path.join(project_dir, "results")
    csv_path = os.path.join(results_dir, "times.csv")

    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} no encontrado. Ejecuta primero run_experiment.py")
        return

    df = pd.read_csv(csv_path)

    # Estilos visuales
    plt.style.use('ggplot')
    colors = {
        'Python (ANTLR4)': '#3572A5',  # Azul Python
        'C# (ANTLR4)': '#178600',      # Verde C#
        'C (Flex+Bison)': '#555555'    # Gris C Nativo
    }
    markers = {
        'Python (ANTLR4)': 'o',
        'C# (ANTLR4)': 's',
        'C (Flex+Bison)': '^'
    }

    # -------------------------------------------------------------
    # Gráfica 1: Tiempo de Parseo Interno (Parse Time) vs Número de Líneas
    # -------------------------------------------------------------
    fig, ax1 = plt.subplots(figsize=(10, 6), dpi=300)

    for parser_name, group in df.groupby('parser'):
        ax1.plot(
            group['num_lines'],
            group['parse_time_ms'],
            label=parser_name,
            color=colors.get(parser_name, '#000000'),
            marker=markers.get(parser_name, 'x'),
            linewidth=2.2,
            markersize=7
        )

    ax1.set_title('Comparativa de Tiempo Interno de Parseo (Parse Time)', fontsize=14, fontweight='bold', pad=15)
    ax1.set_xlabel('Número de Líneas en Archivo YAML', fontsize=12, labelpad=10)
    ax1.set_ylabel('Tiempo de Parseo Interno (ms)', fontsize=12, labelpad=10)
    ax1.legend(title='Parser', fontsize=10, title_fontsize=11)
    ax1.grid(True, linestyle='--', alpha=0.6)

    parse_chart_path = os.path.join(results_dir, "parse_time_comparison.png")
    plt.tight_layout()
    plt.savefig(parse_chart_path)
    plt.close()
    print(f"Gráfica guardada: {parse_chart_path}")

    # -------------------------------------------------------------
    # Gráfica 2: Tiempo Total de Ejecución (Total Execution Time) vs Número de Líneas
    # -------------------------------------------------------------
    fig, ax2 = plt.subplots(figsize=(10, 6), dpi=300)

    for parser_name, group in df.groupby('parser'):
        ax2.plot(
            group['num_lines'],
            group['total_time_ms'],
            label=parser_name,
            color=colors.get(parser_name, '#000000'),
            marker=markers.get(parser_name, 'x'),
            linewidth=2.2,
            markersize=7
        )

    ax2.set_title('Comparativa de Tiempo Total de Ejecución (Proceso Completo)', fontsize=14, fontweight='bold', pad=15)
    ax2.set_xlabel('Número de Líneas en Archivo YAML', fontsize=12, labelpad=10)
    ax2.set_ylabel('Tiempo Total de Ejecución (ms)', fontsize=12, labelpad=10)
    ax2.legend(title='Parser', fontsize=10, title_fontsize=11)
    ax2.grid(True, linestyle='--', alpha=0.6)

    total_chart_path = os.path.join(results_dir, "total_time_comparison.png")
    plt.tight_layout()
    plt.savefig(total_chart_path)
    plt.close()
    print(f"Gráfica guardada: {total_chart_path}")

if __name__ == "__main__":
    main()
