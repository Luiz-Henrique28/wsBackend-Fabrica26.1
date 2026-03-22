# 🌍 GeoRank Challenge

Projeto desenvolvido para o desafio wsBackend-Fabrica26.1. Trata-se de um Web App interativo de quiz geográfico, focado no consumo de dados de uma API externa para gerar perguntas dinâmicas sobre bandeiras, capitais e tamanhos de população.

## Tecnologias Utilizadas

- **Backend:** Python 3.11 e Django
- **Banco de Dados:** MySQL 8.0
- **Integração:** REST Countries API
- **Frontend:** HTML, CSS e Django Templates (Jinja)
- **Infraestrutura:** Docker e Docker Compose

## Funcionalidades e Requisitos Atendidos

- **Consumo de API Externa:** Integração com a REST Countries API, com tradução automática dos dados nativos do inglês para Português-BR no momento do armazenamento em cache.
- **CRUD Completo de Usuários:** Cadastro, autenticação, edição de 'bio' no perfil, histórico de pontuação e deleção de conta/registros.
- **Modelagem de Dados:** Relação funcional de `1 Jogador` para `N Partidas`, utilizando Foreign Keys no banco de dados.
- **Competitividade:** Ranking global computando e ordenando a pontuação acumulada e quantidade total de partidas de todos os jogadores registrados.

## Como Executar o Projeto

O projeto está totalmente conteinerizado, garantindo que o banco de dados e o servidor web sejam configurados automaticamente sem instalar dependências manuais na máquina local.

**Pré-requisitos:** Docker Desktop instalado na sua máquina.

1. Clone este repositório.
2. Acesse a pasta raiz do projeto via terminal (onde encontra-se o arquivo `docker-compose.yml`).
3. Execute o comando para construir e subir os containers em segundo plano:

```bash
docker-compose up --build -d
```

4. Após a inicialização, a aplicação estará disponível no navegador através do endereço:
**`http://localhost:8000`**
