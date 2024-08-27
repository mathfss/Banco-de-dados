CREATE DATABASE IF NOT EXISTS Atividade_Aula3;
USE Atividade_Aula3;

CREATE TABLE Usuario(
	idUsuario INT NOT NULL AUTO_INCREMENT,
    Nome VARCHAR(45),
	Email VARCHAR(45),
	Senha VARCHAR(45),
    PRIMARY KEY(idUsuario)
);

SELECT * FROM Usuario;

INSERT INTO Usuario(Nome, Email, Senha) VALUES ('Alexandre', 'alexandre@email.com', '12345');
INSERT INTO Usuario(Nome, Email, Senha) VALUES ('Natanael', 'natanael12@email.com', 'ABCDE');
INSERT INTO Usuario(Nome, Email, Senha) VALUES ('Júlia', 'julia_09@email.com', '98765');
INSERT INTO Usuario(Nome, Email, Senha) VALUES ('Fernanda', 'fernanda@email.com', 'EFGHI');

UPDATE Usuario SET Senha = '54321' WHERE idUsuario = 1;
DELETE FROM Usuario WHERE idUsuario = 4;

SELECT * FROM Usuario;
SELECT * FROM Usuario WHERE Nome like '%N%';
