CREATE TABLE cliente(
    cliente_id serial primary key,
    nome varchar(50) unique not null,
    cpf varchar(11),
    endereco varchar()100
);