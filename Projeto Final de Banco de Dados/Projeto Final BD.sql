DROP DATABASE IF EXISTS biblioteca; #checando se o bd biblioteca existe e apagando ele se for necessário
CREATE DATABASE IF NOT EXISTS biblioteca; #criando o bd biblioteca
USE biblioteca;

#Crinado tabelas	
#Tabela Autor 	
CREATE TABLE Autor (
    autor_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);

#Tabela Livro
CREATE TABLE Livro (
    livro_id INT PRIMARY KEY AUTO_INCREMENT,
    codigo_livro VARCHAR(20) NOT NULL, 
    titulo VARCHAR(255) NOT NULL,
    ano_publicacao float,
    autor_id INT,
    genero VARCHAR(45),
    FOREIGN KEY (autor_id) REFERENCES Autor(autor_id)
);

#Tabela Usuario
CREATE TABLE Usuario (
    usuario_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE DetalhesUsuario (
    usuario_id INT PRIMARY KEY,
    data_nascimento DATE,
    endereco VARCHAR(255),
	FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id)
);

#Tabela Emprestimo
CREATE TABLE Emprestimo (
    emprestimo_id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT,
    livro_id INT,
    data_emprestimo DATE NOT NULL,
    data_devolucao DATE,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id),
    FOREIGN KEY (livro_id) REFERENCES Livro(livro_id)
);

#Tabela Usuario_empréstimo (para representar o relacionamento N para M)
CREATE TABLE Usuario_empréstimo (
    usuario_id INT,
    emprestimo_id INT,
    PRIMARY KEY (usuario_id, emprestimo_id),
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id),
    FOREIGN KEY (emprestimo_id) REFERENCES Emprestimo(emprestimo_id)
);

# Alterando o tipo da variavel ano_publicacao da tabela livro
ALTER TABLE Livro MODIFY COLUMN ano_publicacao int;

#Inserindo um novo autor na tabela Autor
INSERT INTO Autor (nome) VALUES ('Shakspare');
INSERT INTO Autor (nome) VALUES ('Newton');
INSERT INTO Autor (nome) VALUES ('Chico');
INSERT INTO Autor (nome) VALUES ('Friedrich Nietzsche');
INSERT INTO Autor (nome) VALUES ('Nicholas Sparks');
INSERT INTO Autor (nome) VALUES ('Augusto Cury');

#Inserindo mais livros associados a diferentes autores na tabela Livro
INSERT INTO Livro (codigo_livro, titulo, ano_publicacao, autor_id, genero) VALUES ('XYZ456', 'Matemática para iniciantes', 2019, 2, 'Academico');
INSERT INTO Livro (codigo_livro, titulo, ano_publicacao, autor_id, genero) VALUES ('LMN789', 'a 5 passos de vc', 2021, 1, 'Drama');
INSERT INTO Livro (codigo_livro, titulo, ano_publicacao, autor_id, genero) VALUES ('ABC123', 'dracula', 2022, 1, 'Terror');
INSERT INTO Livro (codigo_livro, titulo, ano_publicacao, autor_id, genero) VALUES ('ABC353', 'a ultima hora', 2022, 1, 'Suspense');
INSERT INTO Livro (codigo_livro, titulo, ano_publicacao, autor_id, genero) VALUES ('JHG764', 'Assim Falou Zaratustra', 1883, 4, 'Academico');
INSERT INTO Livro (codigo_livro, titulo, ano_publicacao, autor_id, genero) VALUES ('SHD345', 'Investindo na Mente', 2015, 6, 'Investimento');
INSERT INTO Livro (codigo_livro, titulo, ano_publicacao, autor_id, genero) VALUES ('JVG735', 'No seu olhar', 2000, 5, 'Romance');

#Inserindo um novo usuário na tabela Usuario
INSERT INTO Usuario (nome, email) VALUES ('Felipe', 'felipe@example.com');
INSERT INTO Usuario (nome, email) VALUES ('Matheus', 'matheus@example.com');
INSERT INTO Usuario (nome, email) VALUES ('Livia', 'livia@example.com');
INSERT INTO Usuario (nome, email) VALUES ('Maria', 'maria@example.com');
INSERT INTO Usuario (nome, email) VALUES ('anakin', 'anakin@example.com');
INSERT INTO Usuario (nome, email) VALUES ('Luke', 'luke@example.com');

#Inserir dados na tabela DetalhesUsuario para usuários específicos
INSERT INTO DetalhesUsuario (usuario_id, data_nascimento, endereco) 
VALUES (1, '1990-01-01', 'Rua Principal, 456');
INSERT INTO DetalhesUsuario (usuario_id, data_nascimento, endereco)
VALUES (2, '1985-05-15', 'Avenida Cruzada, 789');
INSERT INTO DetalhesUsuario (usuario_id, data_nascimento, endereco)
VALUES (3, '1992-11-20', 'Rua Secundária, 321');
INSERT INTO DetalhesUsuario (usuario_id, data_nascimento, endereco)
VALUES (4, '1978-07-03', 'Travessa Principal, 567');
INSERT INTO DetalhesUsuario (usuario_id, data_nascimento, endereco)
VALUES (5, '1998-03-25', 'Avenida Secundária, 876');
INSERT INTO DetalhesUsuario (usuario_id, data_nascimento, endereco)
VALUES (6, '1989-09-10', 'Rua Terciária, 432');

#Realizando um novo empréstimo na tabela Emprestimo
INSERT INTO Emprestimo (usuario_id, livro_id, data_emprestimo, data_devolucao) VALUES (1, 1, '2023-01-01', '2023-01-15');
INSERT INTO Emprestimo (usuario_id, livro_id, data_emprestimo, data_devolucao) VALUES (2, 2, '2023-02-01', '2023-02-15');
INSERT INTO Emprestimo (usuario_id, livro_id, data_emprestimo, data_devolucao) VALUES (1, 3, '2023-03-01', '2023-03-15');
INSERT INTO Emprestimo (usuario_id, livro_id, data_emprestimo, data_devolucao) VALUES (5, 6, '2023-03-01', '2023-03-15');
INSERT INTO Emprestimo (usuario_id, livro_id, data_emprestimo, data_devolucao) VALUES (5, 5, '2023-03-01', '2023-03-15');
INSERT INTO Emprestimo (usuario_id, livro_id, data_emprestimo, data_devolucao) VALUES (6, 4, '2023-03-01', '2023-03-15');

#Atualizando o ano de publicação de um livro na tabela Livro
UPDATE Livro
SET ano_publicacao = 2022
WHERE livro_id = 1;

#Deletando o usuario com id = 3
DELETE FROM DetalhesUsuario WHERE usuario_id = '3';
DELETE FROM Usuario WHERE usuario_id = '3';


#Atualizando o e-mail de Felipe na tabela Usuario
UPDATE Usuario
SET email = 'felipesouza@example.com'
WHERE usuario_id = 1;

#consulta e retornando uma lista de títulos de livros juntamente com os nomes dos autores correspondentes
SELECT Livro.titulo, Autor.nome AS autor
FROM Livro
JOIN Autor ON Livro.autor_id = Autor.autor_id;

#Listando os empréstimos do usuário Felipe
SELECT Usuario.nome, Livro.titulo, Emprestimo.data_emprestimo, Emprestimo.data_devolucao
FROM Usuario
JOIN Emprestimo ON Usuario.usuario_id = Emprestimo.usuario_id
JOIN Livro ON Livro.livro_id = Emprestimo.livro_id
WHERE Usuario.usuario_id = 1;

#Listando os empréstimos do usuário Matheus
SELECT Usuario.nome, Livro.titulo, Emprestimo.data_emprestimo, Emprestimo.data_devolucao
FROM Usuario
JOIN Emprestimo ON Usuario.usuario_id = Emprestimo.usuario_id
JOIN Livro ON Livro.livro_id = Emprestimo.livro_id
WHERE Usuario.usuario_id = 2;

#Listando os empréstimos do usuário Livia
SELECT Usuario.nome, Livro.titulo, Emprestimo.data_emprestimo, Emprestimo.data_devolucao
FROM Usuario
JOIN Emprestimo ON Usuario.usuario_id = Emprestimo.usuario_id
JOIN Livro ON Livro.livro_id = Emprestimo.livro_id
WHERE Usuario.usuario_id = 3;

#Listando os empréstimos do usuário Maria
SELECT Usuario.nome, Livro.titulo, Emprestimo.data_emprestimo, Emprestimo.data_devolucao
FROM Usuario
JOIN Emprestimo ON Usuario.usuario_id = Emprestimo.usuario_id
JOIN Livro ON Livro.livro_id = Emprestimo.livro_id
WHERE Usuario.usuario_id = 4;

#Listando os empréstimos do usuário anakin
SELECT Usuario.nome, Livro.titulo, Emprestimo.data_emprestimo, Emprestimo.data_devolucao
FROM Usuario
JOIN Emprestimo ON Usuario.usuario_id = Emprestimo.usuario_id
JOIN Livro ON Livro.livro_id = Emprestimo.livro_id
WHERE Usuario.usuario_id = 5;

#Listando os empréstimos do usuário luke
SELECT Usuario.nome, Livro.titulo, Emprestimo.data_emprestimo, Emprestimo.data_devolucao
FROM Usuario	
JOIN Emprestimo ON Usuario.usuario_id = Emprestimo.usuario_id
JOIN Livro ON Livro.livro_id = Emprestimo.livro_id
WHERE Usuario.usuario_id = 6;

#Concedendo a permissão SELECT no banco de dados 'biblioteca' para o usuário 'pedro'
#Poderá realizar operações de consulta em todas as tabelas do bd biblioteca
CREATE USER 'Murilo' IDENTIFIED BY '123456';
GRANT SELECT ON biblioteca.* TO 'Murilo';

#Revogando a permissão SELECT no banco de dados 'biblioteca' do usuário 'amora'
REVOKE SELECT ON biblioteca.* FROM 'Murilo';