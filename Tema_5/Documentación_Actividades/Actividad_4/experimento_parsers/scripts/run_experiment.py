import os
import glob
import subprocess
import time
import re
import csv

def count_lines(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return len(f.readlines())

def run_parser(cmd_list):
    t_start = time.perf_counter()
    res = subprocess.run(cmd_list, capture_output=True, text=True)
    t_end = time.perf_counter()
    
    total_time_ms = (t_end - t_start) * 1000.0
    parse_time_ms = total_time_ms  # fallback
    
    match = re.search(r"PARSE_TIME:\s*([\d\.]+)", res.stdout)
    if match:
        parse_time_ms = float(match.group(1))
    
    return total_time_ms, parse_time_ms, res.returncode

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    test_files_dir = os.path.join(project_dir, "test_files")
    results_dir = os.path.join(project_dir, "results")
    os.makedirs(results_dir, exist_ok=True)
    
    csv_path = os.path.join(results_dir, "times.csv")
    
    # Rutas a los parsers
    python_main = os.path.join(project_dir, "src", "antlr_python", "main.py")
    
    csharp_exe = os.path.join(project_dir, "src", "antlr_csharp", "bin", "Release", "net8.0", "Parser.exe")
    if not os.path.exists(csharp_exe):
        # Fallback para Unix / Linux si no hay .exe
        csharp_exe = os.path.join(project_dir, "src", "antlr_csharp", "bin", "Release", "net8.0", "Parser")
        
    c_exe = os.path.join(project_dir, "src", "bison_c", "parser_c.exe")
    if not os.path.exists(c_exe):
        c_exe = os.path.join(project_dir, "src", "bison_c", "parser_c")

    files = sorted(glob.glob(os.path.join(test_files_dir, "*.yml")))
    print(f"Encontrados {len(files)} archivos YAML para el experimento.")
    
    rows = []
    
    for fpath in files:
        fname = os.path.basename(fpath)
        lines_cnt = count_lines(fpath)
        
        # Extraer número de redes del nombre (ej. docker_compose_01.yml -> index 1 -> 2 networks)
        idx_match = re.search(r"(\d+)", fname)
        idx = int(idx_match.group(1)) if idx_match else 1
        num_networks = idx * 2
        
        print(f"Probando {fname} ({lines_cnt} líneas, {num_networks} redes)...")
        
        # 1. Parser Python
        tot_py, parse_py, code_py = run_parser(["python", python_main, fpath])
        rows.append({
            "file": fname,
            "num_lines": lines_cnt,
            "num_networks": num_networks,
            "parser": "Python (ANTLR4)",
            "total_time_ms": round(tot_py, 4),
            "parse_time_ms": round(parse_py, 4)
        })
        
        # 2. Parser C#
        if os.path.exists(csharp_exe):
            cmd_cs = [csharp_exe, fpath]
        else:
            cmd_cs = ["dotnet", "run", "-c", "Release", "--no-build", "--project", os.path.join(project_dir, "src", "antlr_csharp", "Parser.csproj"), fpath]
            
        tot_cs, parse_cs, code_cs = run_parser(cmd_cs)
        rows.append({
            "file": fname,
            "num_lines": lines_cnt,
            "num_networks": num_networks,
            "parser": "C# (ANTLR4)",
            "total_time_ms": round(tot_cs, 4),
            "parse_time_ms": round(parse_cs, 4)
        })
        
        # 3. Parser C
        tot_c, parse_c, code_c = run_parser([c_exe, fpath])
        rows.append({
            "file": fname,
            "num_lines": lines_cnt,
            "num_networks": num_networks,
            "parser": "C (Flex+Bison)",
            "total_time_ms": round(tot_c, 4),
            "parse_time_ms": round(parse_c, 4)
        })

    # Guardar en CSV
    fieldnames = ["file", "num_lines", "num_networks", "parser", "total_time_ms", "parse_time_ms"]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nExperimento completado exitosamente! Datos guardados en {csv_path}")

if __name__ == "__main__":
    main()
