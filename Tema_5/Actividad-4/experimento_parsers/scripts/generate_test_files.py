import os

def generate_yaml(num_networks, output_path):
    lines = []
    lines.append("version: '3.8'")
    lines.append("services:")
    lines.append("  web:")
    lines.append("    image: nginx:latest")
    lines.append("    networks:")
    for i in range(1, num_networks + 1):
        lines.append(f"      - net_{i}")
    
    lines.append("networks:")
    for i in range(1, num_networks + 1):
        lines.append(f"  net_{i}:")
        lines.append("    driver: bridge")
        lines.append("    ipam:")
        lines.append("      config:")
        lines.append(f"        subnet: 172.20.{i}.0/24")

    content = "\n".join(lines) + "\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    return len(lines)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    test_files_dir = os.path.join(project_dir, "test_files")
    os.makedirs(test_files_dir, exist_ok=True)

    print(f"Generando 16 archivos YAML sintéticos en {test_files_dir}...")
    
    # 16 archivos con número creciente de redes: 2, 4, 6, ..., 32
    for idx in range(1, 17):
        num_nets = idx * 2
        file_name = f"docker_compose_{idx:02d}.yml"
        file_path = os.path.join(test_files_dir, file_name)
        num_lines = generate_yaml(num_nets, file_path)
        print(f"Creado {file_name}: {num_nets} redes, {num_lines} líneas")

if __name__ == "__main__":
    main()
