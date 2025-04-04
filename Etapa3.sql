create database intuitive;

use intuitive;
-- Criando a tabela de operadoras (dados vindos da ANS)
CREATE TABLE operadoras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    registro_ans VARCHAR(20) UNIQUE NOT NULL,
    cnpj VARCHAR(20) NOT NULL,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(255),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(3),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(255),
    regiao_comercializacao INT,
    data_registro DATE
);

-- Criando a tabela 'demonstracoes_contabeis' para armazenar os dados financeiros das operadoras
CREATE TABLE demonstracoes_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_registro DATE NOT NULL,
    registro_ans VARCHAR(20) NOT NULL,
    codigo_conta VARCHAR(20) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    saldo_inicial DECIMAL(15,2),
    saldo_final DECIMAL(15,2),
    FOREIGN KEY (registro_ans) REFERENCES operadoras(registro_ans)
);

select * from operadoras;

select * from demonstracoes_contabeis;

SET SQL_SAFE_UPDATES = 0;


LOAD DATA LOCAL INFILE 'C:/Users/aapol/OneDrive/Documentos/GitHub/IntuitiveCode/arquivos/Relatorio_cadop.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, regiao_comercializacao, data_registro);


-- Carregando os dados do arquivo CSV para a tabela 'demonstracoes_contabeis'
LOAD DATA LOCAL INFILE 'C:/Users/aapol/OneDrive/Documentos/GitHub/IntuitiveCode/arquivos/2023/1T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"' -- isso resolve os campos com aspas duplas
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(data_registro, registro_ans, codigo_conta, descricao, saldo_inicial, saldo_final);

-- Carregando os dados contábeis dos arquivos CSV para a tabela 'demonstracoes_contabeis'
LOAD DATA LOCAL INFILE 'C:/Users/aapol/OneDrive/Documentos/GitHub/IntuitiveCode/arquivos/2023/2T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"' -- isso resolve os campos com aspas duplas
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(data_registro, registro_ans, codigo_conta, descricao, saldo_inicial, saldo_final);

LOAD DATA LOCAL INFILE 'C:/Users/aapol/OneDrive/Documentos/GitHub/IntuitiveCode/arquivos/2023/3T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"' -- isso resolve os campos com aspas duplas
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(data_registro, registro_ans, codigo_conta, descricao, saldo_inicial, saldo_final);

LOAD DATA LOCAL INFILE 'C:/Users/aapol/OneDrive/Documentos/GitHub/IntuitiveCode/arquivos/2023/4T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"' -- isso resolve os campos com aspas duplas
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(data_registro, registro_ans, codigo_conta, descricao, saldo_inicial, saldo_final);

LOAD DATA LOCAL INFILE 'C:/Users/aapol/OneDrive/Documentos/GitHub/IntuitiveCode/arquivos/2024/1T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"' -- isso resolve os campos com aspas duplas
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(data_registro, registro_ans, codigo_conta, descricao, saldo_inicial, saldo_final);

LOAD DATA LOCAL INFILE 'C:/Users/aapol/OneDrive/Documentos/GitHub/IntuitiveCode/arquivos/2024/2T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"' -- isso resolve os campos com aspas duplas
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(data_registro, registro_ans, codigo_conta, descricao, saldo_inicial, saldo_final);

LOAD DATA LOCAL INFILE 'C:/Users/aapol/OneDrive/Documentos/GitHub/IntuitiveCode/arquivos/2024/3T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"' -- isso resolve os campos com aspas duplas
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(data_registro, registro_ans, codigo_conta, descricao, saldo_inicial, saldo_final);

LOAD DATA LOCAL INFILE 'C:/Users/aapol/OneDrive/Documentos/GitHub/IntuitiveCode/arquivos/2024/4T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"' -- isso resolve os campos com aspas duplas
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(data_registro, registro_ans, codigo_conta, descricao, saldo_inicial, saldo_final);

-- Consulta para obter as 10 operadoras com maiores despesas no trimestre atual
SELECT o.razao_social, d.registro_ans, SUM(d.saldo_final) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras o ON d.registro_ans = o.registro_ans
WHERE TRIM(REPLACE(d.descricao, '"', '')) = 'Despesas com Eventos / Sinistros'
  AND YEAR(d.data_registro) = YEAR(CURDATE())
  AND QUARTER(d.data_registro) = QUARTER(CURDATE())
GROUP BY o.razao_social, d.registro_ans
ORDER BY total_despesas DESC
LIMIT 10;


-- Consulta para obter as 10 operadoras com maiores despesas no último trimestre?
select registro_ans, sum(saldo_final) as total_despesas from demonstracoes_contabeis where descricao = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR " 
and data_registro between '2024-07-01' and '2023-10-01' group by registro_ans order by total_despesas desc limit 10;
-- Consulta para obter as 10 operadoras com maiores despesas ultimo ano
select registro_ans, sum(saldo_final) as total_despesas from demonstracoes_contabeis where descricao = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR " 
and data_registro between '2024-01-01' and '2024-10-01' group by registro_ans order by total_despesas desc limit 10;

