# Indicium Tech Code Challenge

## Contexto
Na Indicium, desenvolvemos pipelines de dados completos para nossos clientes, desde a extração de dados de várias fontes até a carga desses dados em seu destino final, que pode variar de um data warehouse para uma ferramenta de Business Intelligence até uma API para integração com sistemas de terceiros.

Como desenvolvedor de software focado em projetos de dados, sua missão é planejar, desenvolver, implantar e manter um pipeline de dados.

## Desafio
Fornecemos duas fontes de dados: um banco de dados PostgreSQL e um arquivo CSV.
- O arquivo CSV representa detalhes de pedidos de um sistema de e-commerce.
- O banco de dados fornecido é uma amostra do banco de dados Northwind da Microsoft, mas sem a tabela de detalhes dos pedidos (`order_details`). Esta tabela está representada pelo arquivo CSV fornecido.

## Objetivo
Construir um pipeline que extraia os dados diariamente de ambas as fontes e escreva os dados primeiro no disco local e, em seguida, em um banco de dados PostgreSQL. Para este desafio, o arquivo CSV e o banco de dados são estáticos, mas em um projeto real, ambas as fontes de dados mudariam constantemente.

### Requisitos
- **Isolamento de Etapas:** Todas as etapas de escrita (escrita de dados das entradas para o sistema de arquivos local e escrita de dados do sistema de arquivos local para o banco de dados PostgreSQL) devem ser isoladas umas das outras.
- **Arquivos Separados:** Para a primeira etapa, onde você escreve dados no disco local, deve escrever um arquivo para cada tabela. Esta pipeline será executada diariamente, então deve haver uma separação nos caminhos dos arquivos criados para cada fonte (CSV ou Postgres), tabela e combinação de dia de execução.
  - Exemplos de caminhos de arquivos:
    - `/data/postgres/{table}/2024-01-01/file.format`
    - `/data/postgres/{table}/2024-01-02/file.format`
    - `/data/csv/2024-01-02/file.format`
- **Carregamento de Dados:** Carregar os dados do sistema de arquivos local, que você criou, para o banco de dados final.
- **Objetivo Final:** Ser capaz de executar uma consulta que mostre os pedidos e seus detalhes. Os pedidos estão em uma tabela chamada `orders` no banco de dados Northwind do PostgreSQL. Os detalhes estão no arquivo CSV fornecido, e cada linha possui um campo `order_id` apontando para a tabela de pedidos.

### Ferramentas
- **Orquestrador:** Airflow
- **Carregador de Dados:** Meltano
- **Banco de Dados:** PostgreSQL

## Estrutura do Projeto

### Diagrama da Solução
![image](docs/diagrama_embulk_meltano.jpg)

## Solução

### Passo 1
Definição e configuração do arquivo docker-compose.yml.

### Passo 2
Inicialização e Configuração do Meltano, arquivo meltano.yml e scripts em python para automatização das tarefas de extração e carregamento dos dados.

### Passo 3
Configuração das DAGs do Airflow, as DAGs foram criadas para auxiliar na automatização do floxo das tarefas.


## Como Rodar o Projeto

### Pré-requisitos
- Docker e Docker Compose instalados.

### Passos para Execução
1. Clone o repositório:
    ```bash
    git clone git@github.com:thaiismeneses/code-challenge-indicium-engdados.git

    cd seu-repositorio
    ```

2. Inicie os serviços com Docker Compose:
    ```bash
    docker-compose up -d
    ```

    Isso irá levantar três contêineres:
    - `db`: Banco de dados PostgreSQL de origem.
    - `db-2`: Banco de dados PostgreSQL de destino.
    - `airflow`: Servidor Airflow para orquestração.

3. Acesse o Airflow:
   - Abra seu navegador e vá para `http://localhost:8080`.
   - Use as credenciais padrão (usuário: airflow, senha: airflow) para acessar o painel do Airflow.

4. Verifique as DAGs do Airflow:
   - No painel do Airflow, você verá três DAGs principais:
     - `pipeline_one_only`: Extrai dados do PostgreSQL e CSV, organiza e salva como CSV.
     - `pipeline_two_only`: Organiza os dados atuais e os carrega no PostgreSQL de destino.
     - `pipeline_one_and_two`: Realiza as duas pipelines.

5. Habilite e execute as DAGs conforme necessário para iniciar os pipelines de ETL.

### Configuração do Meltano
O arquivo `meltano.yml` está configurado para usar os serviços definidos no `docker-compose.yml`. As configurações relevantes são:

#### Extractor
```yaml
- name: tap-postgres
- name: tap-csv
```

#### Loaders
```yaml
- name: target-postgres
- name: target-csv
```

#### Estrutura dos Arquivos

`docker-compose.yml`: Foi configurado para definir os serviços do Docker para PostgreSQL e Airflow.

`meltano`: Diretório onde o meltano foi inicializado e contem o diretório de `scripts` onde estão os documentos de excução em python.

`meltano.yml`:  Foram configurados para terem o extratores e carregadores de dados.

`Airflow/dags`: Diretório onde as DAGs do Airflow são armazenadas.

`data-pipeline`: Diretório contando os arquivos CSV e scripts de inicialização do banco de dados.

#### Considerações Finais

Este projeto de ETL utilizando Meltano e Airflow foi uma oportunidade valiosa para explorar a integração de diferentes fontes de dados e a automação de pipelines de ETL. Ao desenvolver e implementar este projeto, pude aprofundar meu conhecimento em ferramentas modernas de ciência de dados e engenharia de dados. Apesar de nunca ter tido contato com as ferramentas acredito que obtive sucesso.


