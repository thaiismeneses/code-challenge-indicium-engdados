import os
import json
from datetime import datetime

def generate_files_definition(data_dir):
    """
    Gera um arquivo "files_definition.json" com base nos arquivos CSV presentes no diretório especificado.

    Args:
        data_dir (str): Diretório onde os arquivos CSV estão localizados.
    """
    # Verifica o diretório
    if not os.path.isdir(data_dir):
        raise ValueError(f"Invalid data directory: {data_dir}")

    # Lista todos os arquivos no diretório de dados
    files = os.listdir(data_dir)

    files_definition = []

    # Itera sobre os arquivos encontrados no diretório
    for filename in files:
        if filename.endswith(".csv"):
            entity_name = os.path.splitext(filename)[0]
            file_path = os.path.join(data_dir, filename)
            files_definition.append({
                "entity": entity_name,
                "path": file_path,
                "keys": []
            })

    # Cria o diretório temporário se não existir
    temp_dir = os.path.join(data_dir, ".temp")
    os.makedirs(temp_dir, exist_ok=True)

    # Caminho completo para o arquivo de definição
    output_file_path = os.path.join(temp_dir, "files_definition.json")

    # Escreve o arquivo de definição JSON
    with open(output_file_path, "w") as f:
        json.dump(files_definition, f, indent=4)

    print(f"Generated files_definition.json in: {output_file_path}")

if __name__ == "__main__":
    base_directory = "/code-challenge-indicium-engdados/data-pipeline/current_data"
    generate_files_definition(base_directory)
