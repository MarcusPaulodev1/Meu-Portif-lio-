# ============================================
# SISTEMA SIMPLES DE USUÁRIOS COM SQLALCHEMY
# ============================================

# Imports necessários para criar o banco de dados e a tabela
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Endereço do banco de dados SQLite
# O arquivo banco.db será criado automaticamente na pasta do projeto
DATABASE_URL = "sqlite:///banco.db"

# Criação do motor de conexão com o banco
# Sem echo=True, para não mostrar todos os comandos SQL no terminal
engine = create_engine(DATABASE_URL)

# Criação da sessão, usada para conversar com o banco de dados
SessionLocal = sessionmaker(bind=engine)

# Base usada para criar os modelos/tabelas do banco
Base = declarative_base()


# ============================================
# MODELO DA TABELA NO BANCO DE DADOS
# ============================================

class UsuarioModel(Base):
    """
    Essa classe representa a tabela 'usuarios' no banco de dados.
    Cada objeto criado aqui pode virar uma linha da tabela.
    """

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    tipo = Column(String)


# ============================================
# CLASSES DO SISTEMA USANDO POO
# ============================================

class Usuario:
    """
    Classe base do sistema.
    Representa um usuário comum.
    """

    def __init__(self, nome):
        self.nome = nome
        self.tipo = "usuario"

    def salvar(self, db):
        """
        Salva o usuário no banco de dados.
        """
        novo_usuario = UsuarioModel(nome=self.nome, tipo=self.tipo)
        db.add(novo_usuario)
        db.commit()
        print(f"Usuário {self.nome} salvo com sucesso!")


class Gestor(Usuario):
    """
    Classe Gestor.
    Herda de Usuario e adiciona a função de listar usuários.
    """

    def __init__(self, nome):
        super().__init__(nome)
        self.tipo = "gestor"

    def listar_usuarios(self, db):
        """
        Lista todos os usuários cadastrados no banco.
        """
        usuarios = db.query(UsuarioModel).all()

        if not usuarios:
            print("Nenhum usuário cadastrado.")
            return

        for usuario in usuarios:
            print(f"ID: {usuario.id} | Nome: {usuario.nome} | Tipo: {usuario.tipo}")


class Administrador(Gestor):
    """
    Classe Administrador.
    Herda de Gestor e adiciona a função de deletar usuários.
    """

    def __init__(self, nome):
        super().__init__(nome)
        self.tipo = "admin"

    def deletar_usuario(self, db, user_id):
        """
        Deleta um usuário pelo ID.
        """
        usuario = db.query(UsuarioModel).filter(UsuarioModel.id == user_id).first()

        if usuario:
            db.delete(usuario)
            db.commit()
            print(f"Usuário {usuario.nome} deletado com sucesso!")
        else:
            print("Usuário não encontrado.")


# ============================================
# EXECUÇÃO PRINCIPAL DO PROGRAMA
# ============================================

if __name__ == "__main__":
    # Cria a tabela no banco de dados, caso ela ainda não exista
    Base.metadata.create_all(bind=engine)

    # Abre uma sessão com o banco
    db = SessionLocal()

    # Criação de objetos usando POO
    usuario_comum = Usuario("João")
    gestor = Gestor("Maria")
    administrador = Administrador("Carlos")

    # Salvando os usuários no banco
    usuario_comum.salvar(db)
    gestor.salvar(db)
    administrador.salvar(db)

    print("\n--- Lista de usuários cadastrados ---")
    gestor.listar_usuarios(db)

    print("\n--- Administrador deletando o usuário de ID 1 ---")
    administrador.deletar_usuario(db, 1)

    print("\n--- Lista de usuários atualizada ---")
    gestor.listar_usuarios(db)

    # Fecha a sessão com o banco
    db.close()
