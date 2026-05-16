# 💻 Meu Portfólio de Projetos Python

Repositório com projetos desenvolvidos para praticar programação back-end, Programação Orientada a Objetos (POO), automação, APIs e integração com banco de dados.

---

# 📌 Projetos do Repositório

## 🌦️ Sistema de Consulta Climática com OpenWeather

Projeto desenvolvido em Python utilizando:

- Programação Orientada a Objetos (POO)
- API REST
- JSON
- SQLite
- SQLAlchemy
- Requests
- Pandas

O sistema realiza consultas climáticas em tempo real através da API OpenWeather.

---

# ⚙️ Funcionalidades do Sistema

- Consultar clima de cidades em tempo real
- Consumir dados da API OpenWeather
- Receber respostas em formato JSON
- Converter dados em objetos Python
- Salvar histórico no banco SQLite
- Listar consultas realizadas
- Deletar consultas do banco
- Tratar erros de API e cidades inválidas

---

# 🧠 Conceitos aplicados

## 🔹 Programação Orientada a Objetos

O projeto foi dividido em múltiplas classes para separar responsabilidades:

### ConsultaClima
Classe modelo responsável pelos dados climáticos.

### DatabaseManager
Gerencia conexão e sessões do banco de dados.

### WeatherAPIClient
Responsável pela comunicação com a API OpenWeather.

### ConsultaClimaRepository
Realiza operações no banco de dados.

### ClimaService
Centraliza a lógica principal do sistema.

---

# 🌐 Integração com API

O sistema utiliza requisições HTTP para acessar a API OpenWeather.

Os dados retornam em formato JSON e são tratados automaticamente pelo Python.

Exemplo de fluxo:

Usuário → API → JSON → Objeto Python → Banco SQLite

---

# 🛠️ Tecnologias utilizadas

- Python
- SQLAlchemy
- SQLite
- Requests
- Pandas
- OpenWeather API
- Programação Orientada a Objetos (POO)

---

# 🚀 Conhecimentos demonstrados

Este projeto demonstra conhecimentos em:

- Consumo de APIs REST
- Manipulação de JSON
- Estruturação de sistemas em Python
- Programação Orientada a Objetos
- ORM com SQLAlchemy
- Banco de dados SQLite
- CRUD completo
- Tratamento de erros
- Organização de código em camadas
- Integração entre banco de dados e APIs
- Desenvolvimento back-end

---

# ▶️ Como executar

## Instalar dependências

```bash
pip install sqlalchemy requests pandas
```

---

## Configurar API KEY

Crie uma conta no OpenWeather:

https://openweathermap.org/api

Depois substitua:

```python
API_KEY = "SUA_CHAVE_AQUI"
```

---

## Executar o sistema

```bash
python sistema_clima_openweather.py
```

---

# 🎯 Objetivo do projeto

O objetivo deste projeto foi praticar conceitos fundamentais de desenvolvimento back-end utilizando Python, APIs, banco de dados e Programação Orientada a Objetos, criando uma aplicação organizada, funcional e próxima de cenários reais de mercado.

---

# 👨‍💻 Autor

Marcus Paulo

- Estudante de Engenharia de Software
- Desenvolvedor Python
- Interesse em Back-end, APIs, IA e automação

## 🔗 LinkedIn

https://www.linkedin.com/in/marcus-paulo-00a2833a6

## 🔗 GitHub

https://github.com/MarcusPaulodev1
