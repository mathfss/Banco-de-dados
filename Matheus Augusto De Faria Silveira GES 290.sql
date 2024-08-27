create database if not exists missaoagente;
use missaoagente;

create table if not exists Agente (
	idAgente INT NOT NULL,
    nome VARCHAR(45),
    endereco VARCHAR(45),
    nascimento DATE,
    habilidade VARCHAR(45),
    sexo VARCHAR(45),
    email VARCHAR(45),
	PRIMARY KEY (idAgente)
    );
    
    create table if not exists vilao (
	idvilao INT NOT NULL,
    nome VARCHAR(45),
    num_crimes int,
	PRIMARY KEY (idvilao)
    );
    
    create table if not exists missao (
	idmissao INT NOT NULL,
    data DATE,
    nome VARCHAR(45),
    local VARCHAR(45),
    duracao int,
    vilao_idvilao INT,
	PRIMARY KEY (idmissao),
    FOREIGN KEY (vilao_idvilao) REFERENCES vilao(idvilao)
    );
    
    create table if not exists Agente_has_missao (
	Agente_idAgente INT,
    missao_idmissao INT,
    FOREIGN KEY (Agente_idAgente) REFERENCES Agente(idAgente),
    FOREIGN KEY (missao_idmissao) REFERENCES missao(idmissao)
    );
    
    create user user1 identified by 'usuario1';
    grant all on missaoagente.* to user1;
    alter table Agente drop habilidade;
    INSERT INTO Agente(idAgente, nome, endereco, sexo) VALUES ('1', 'Fulano', 'rua arvore', 'masculino');
	INSERT INTO missao(idmissao, nome, duracao, local) VALUES ('2', 'secreta', '100', 'caverna');
    INSERT INTO vilao(idvilao, nome, num_crimes) VALUES ('3', 'Ciclano', '20');
    
    SELECT missao.nome, vilao.nome FROM missao JOIN vilao;
    
    SELECT Agente.nome, missao.nome FROM Agente AS Agente JOIN Agente_has_missao AS Agente_has_missao 
    ON Agente.idAgente = Agente_has_missao.Agente_idAgente JOIN missao AS missao
    ON missao.idmissao = Agente_has_missao.missao_idmissao;
    
    revoke delete on missaoagente.* from user1;

	
    
    