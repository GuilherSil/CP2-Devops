CREATE DATABASE app_almoxarifado;
USE app_almoxarifado;

CREATE TABLE materiais (
  id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(50) NOT NULL,
  quantidade INT NOT NULL,
  unidade VARCHAR(20) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO materiais(
    nome,
    quantidade,
    unidade
    ) VALUES (
    'Fio de cobre',
    100,
    'm'
    );