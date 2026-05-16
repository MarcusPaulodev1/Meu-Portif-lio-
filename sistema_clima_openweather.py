# =========================================
# SISTEMA DE CONSULTA CLIMÁTICA COM OPENWEATHER
# Projeto em Python usando POO, API, JSON, SQLite e SQLAlchemy
# =========================================

# Para usar no Google Colab, execute antes:
# !pip install sqlalchemy requests pandas

from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import requests
import pandas as pd


# =========================================
# MODELO
# =========================================

Base = declarative_base()


class ConsultaClima(Base):
    """
    Classe que representa uma consulta climática.

    Cada objeto dessa classe será salvo como um registro
    na tabela consultas_clima do banco de dados SQLite.
    """

    __tablename__ = "consultas_clima"

    id = Column(Integer, primary_key=True)
    cidade = Column(String(120), nullable=False)
    descricao = Column(String(120), nullable=False)
    temperatura = Column(Float, nullable=False)
    sensacao_termica = Column(Float)
    umidade = Column(Integer)
    pressao = Column(Integer)
    velocidade_vento = Column(Float)
    data_consulta = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.cidade} - {self.temperatura}°C - {self.descricao}"

    def to_dict(self):
        """Converte o objeto em dicionário para facilitar a exibição com Pandas."""
        return {
            "id": self.id,
            "cidade": self.cidade,
            "descricao": self.descricao,
            "temperatura": self.temperatura,
            "sensacao_termica": self.sensacao_termica,
            "umidade": self.umidade,
            "pressao": self.pressao,
            "velocidade_vento": self.velocidade_vento,
            "data_consulta": self.data_consulta.isoformat()
        }


# =========================================
# BANCO DE DADOS
# =========================================

class DatabaseManager:
    """
    Classe responsável por criar a conexão com o banco SQLite
    e gerar as sessões usadas pelo SQLAlchemy.
    """

    def __init__(self):
        self.engine = create_engine("sqlite:///clima.db")
        self.Session = sessionmaker(bind=self.engine)

    def criar_tabelas(self):
        Base.metadata.create_all(self.engine)

    def criar_sessao(self):
        return self.Session()


# =========================================
# CLIENTE DA API
# =========================================

class WeatherAPIClient:
    """
    Classe responsável por se comunicar com a API OpenWeather.
    Ela envia a cidade, recebe os dados em JSON e trata erros básicos.
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.openweathermap.org/data/2.5/weather"

    def consultar_clima(self, cidade):
        params = {
            "q": cidade,
            "appid": self.api_key,
            "units": "metric",
            "lang": "pt_br"
        }

        resposta = requests.get(self.url, params=params)

        if resposta.status_code == 404:
            raise ValueError("Cidade não encontrada.")

        if resposta.status_code == 401:
            raise ValueError("Chave inválida ou não ativada.")

        if resposta.status_code != 200:
            raise Exception("Erro na API.")

        return resposta.json()


# =========================================
# REPOSITÓRIO
# =========================================

class ConsultaClimaRepository:
    """
    Classe responsável pelas operações no banco de dados.
    Aqui ficam as ações de salvar, listar e deletar consultas.
    """

    def __init__(self, session):
        self.session = session

    def salvar(self, consulta):
        self.session.add(consulta)
        self.session.commit()
        self.session.refresh(consulta)
        return consulta

    def listar(self):
        return self.session.query(ConsultaClima).order_by(
            ConsultaClima.data_consulta.desc()
        ).all()

    def deletar(self, consulta_id):
        consulta = self.session.query(ConsultaClima).filter(
            ConsultaClima.id == consulta_id
        ).first()

        if not consulta:
            return False

        self.session.delete(consulta)
        self.session.commit()
        return True


# =========================================
# SERVICE
# =========================================

class ClimaService:
    """
    Classe que concentra a lógica principal do sistema.
    Ela conecta a API ao repositório e transforma o JSON em objeto.
    """

    def __init__(self, api, repo):
        self.api = api
        self.repo = repo

    def consultar(self, cidade):
        dados = self.api.consultar_clima(cidade)

        consulta = ConsultaClima(
            cidade=dados["name"],
            descricao=dados["weather"][0]["description"],
            temperatura=dados["main"]["temp"],
            sensacao_termica=dados["main"]["feels_like"],
            umidade=dados["main"]["humidity"],
            pressao=dados["main"]["pressure"],
            velocidade_vento=dados["wind"].get("speed")
        )

        return self.repo.salvar(consulta)

    def listar(self):
        return self.repo.listar()

    def deletar(self, consulta_id):
        return self.repo.deletar(consulta_id)


# =========================================
# CONFIGURAÇÃO DO SISTEMA
# =========================================

API_KEY = "SUA_CHAVE_AQUI"


def iniciar_sistema():
    """Configura banco, API, repositório e serviço principal."""
    db = DatabaseManager()
    db.criar_tabelas()
    session = db.criar_sessao()

    api = WeatherAPIClient(API_KEY)
    repo = ConsultaClimaRepository(session)
    service = ClimaService(api, repo)

    return service


# =========================================
# MENU PRINCIPAL
# =========================================

def menu():
    service = iniciar_sistema()

    while True:
        print("\n=== MENU ===")
        print("1 - Consultar clima")
        print("2 - Ver histórico")
        print("3 - Deletar")
        print("4 - Sair")

        op = input("Escolha: ")

        if op == "1":
            cidade = input("Digite a cidade, exemplo: Belo Horizonte,MG,BR: ")

            try:
                consulta = service.consultar(cidade)
                print("Consulta salva com sucesso!")
                print("Resultado:", consulta)
            except Exception as e:
                print("Erro:", e)

        elif op == "2":
            historico = service.listar()

            if not historico:
                print("Nenhuma consulta encontrada.")
            else:
                for c in historico:
                    print(c.id, "-", c)

                df = pd.DataFrame([c.to_dict() for c in historico])
                print("\nTabela de histórico:")
                print(df)

        elif op == "3":
            try:
                cid = int(input("Digite o ID para deletar: "))

                if service.deletar(cid):
                    print("Consulta deletada com sucesso!")
                else:
                    print("ID não encontrado.")
            except ValueError:
                print("Digite apenas números no ID.")

        elif op == "4":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
