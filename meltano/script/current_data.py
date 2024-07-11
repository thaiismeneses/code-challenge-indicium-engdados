import os
import shutil
from datetime import datetime

def move_current_data(base_directory, date=None):
    """
    Organiza os arquivos baseados no dia, que seram inseridos no banco de dados.

    Args:
        data_dir (str): Diretório onde os arquivos CSV estão localizados.
        date (str): Data dos arquivos que serão organizados.
    """
    # Se a data não for definida
    if date is None:
        today = datetime.today()
        date = today.strftime('%Y%m%d')
    else:
        # Verifica o formato da data
        try:
            datetime.strptime(date, '%Y%m%d')
        except ValueError:
            raise ValueError("A data fornecida não está no formato correto YYYYMMDD.")

    # Diretorio de origem onde estão as pastas com datas
    source_dir = os.path.join(base_directory, date)

    # Diretorio de destino, onde os arquivos serão copiados
    dest_dir = os.path.join(base_directory, 'current_data')

    # Se não existir, cria o diretorio
    os.makedirs(dest_dir, exist_ok=True)

    # Limpar o diretorio de destino (se existir)
    print(f"Limpando diretório de destino: {dest_dir}")
    #Itera sobre cada arquivo do diretorio
    for filename in os.listdir(dest_dir):
        file_path = os.path.join(dest_dir, filename)
        try:
            # Verifica se é um arquivo válido
            if os.path.isfile(file_path) or os.path.islink(file_path):
                # Remove o arquivo
                os.unlink(file_path)
            # Se for um diretorio
            elif os.path.isdir(file_path):
                #Remove o diretorio
                shutil.rmtree(file_path)
            print(f"Arquivo ou diretório removido: {file_path}")
        except Exception as e:
            print(f"Falha ao deletar {file_path}. Erro: {e}")

    # Copiar os arquivos da pasta correspondente à data para o diretório de destino
    print(f"Copiando arquivos de {source_dir} para {dest_dir}")
    if os.path.exists(source_dir) and os.path.isdir(source_dir):
        for root, dirs, files in os.walk(source_dir):
            for filename in files:
                file_path = os.path.join(root, filename)
                if os.path.isfile(file_path):
                    # Verificar se o arquivo não está na pasta metrics
                    if "metrics" not in root:
                        shutil.copy(file_path, dest_dir)
                        print(f"Arquivo copiado: {file_path} -> {os.path.join(dest_dir, filename)}")
    else:
        print(f"A pasta para a data {date} não existe ou não é um diretório válido em {base_directory}.")

    print(f"Processamento concluído para a data {date}.")


if __name__ == "__main__":
    # Diretório base
    base_directory = "/code-challenge-indicium-engdados/data-pipeline"

    # Chama a função sem data para usar a data atual
    move_current_data(base_directory)

    # Ou pode também chamar a função com uma data específica
    # move_current_data(base_directory, "20240613")
