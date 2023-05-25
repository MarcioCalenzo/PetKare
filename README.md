# PetKare API

A PetKare API é uma solução desenvolvida para auxiliar a franquia PetKare, um petshop, a ter um controle e organização melhores dos dados dos animais de seus clientes. Essa API tem como objetivo substituir processos manuais e papéis desorganizados, proporcionando uma gestão mais eficiente e simplificada das informações dos bichinhos.

## Objetivo

O principal objetivo da PetKare API é fornecer uma plataforma que permita ao PetKare ter um controle mais preciso dos dados dos animais pertencentes aos seus clientes. Com essa API, o petshop poderá centralizar e estruturar as informações dos animais, facilitando o acesso, a atualização e a busca de dados importantes.

## Rotas

A API oferece as seguintes rotas:

- `api/pets/`

  - `POST` - Cadastrar um pet.
  - `GET` - Listar todos os pets cadastrados.

- `api/pets/<pet_id>/`

  - `GET` - Filtrar um pet específico.
  - `PATCH` - Atualizar os dados de um pet específico.
  - `DELETE` - Excluir um pet específico.

## Modelos

A API utiliza os seguintes modelos:

### Modelo Pet

| Atributo | Propriedades                     |
|----------|---------------------------------|
| name     | String, tamanho máximo de 50     |
| age      | Inteiro                         |
| weight   | Float                           |
| sex      | String, tamanho máximo de 20     |
| group    | Objeto Group                     |
| traits   | Lista de objetos Trait           |

### Modelo Group

| Atributo        | Propriedades                     |
|-----------------|---------------------------------|
| scientific_name | String, tamanho máximo de 50     |
| created_at      | Data e tempo                     |

### Modelo Trait

| Atributo   | Propriedades                     |
|------------|---------------------------------|
| name       | String, tamanho máximo de 20     |

## Exemplos de Uso

### Cadastrar um pet

```json
{
  "name": "Seraphim",
  "age": 1,
  "weight": 20,
  "sex": "Male",
  "group": {"scientific_name": "canis familiaris"},
  "traits": [{"trait_name": "clever"}, {"trait_name": "friendly"}]
}
```
### A resposta terá o seguinte formato:


```json
{
  "id": 1,
  "name": "Seraphim",
  "age": 1,
  "weight": 20.0,
  "sex": "Male",
  "group": {
    "id": 1,
    "scientific_name": "canis familiaris",
    "created_at": "2022-11-27T17:55:22.819371Z"
  },
  "traits": [
    {
      "id": 1,
      "trait_name": "clever",
      "created_at": "2022-11-27T17:55:30.819371Z"
    },
    {
      "id": 2,
      "trait_name": "friendly",
      "created_at": "2022-11-27T17:55:31.819371Z"
    }
  ]
}
```
###Para listar os pets, faça uma requisição GET para api/pets/. A resposta terá o seguinte formato:


```json
{
  "count": 8,
  "next": "http://localhost:8000/api/pets/?page=2",
  "previous": null,
  "results": [
    // Deve haver apenas 2 pets listados por vez
  ]
}
```
# Configuração do Ambiente Local

Siga as instruções abaixo para configurar e executar a PetKare API em seu ambiente local:

1. Clone este repositório em sua máquina local.

2. Ative o ambiente virtual utilizando o seguinte comando:

   - **Windows:**

     ```
     .\venv\Scripts\activate
     ```

   - **Linux:**

     ```
     source venv/bin/activate
     ```

3. Instale as dependências utilizando o seguinte comando:

     ```
     pip install -r requirements.txt
     ```


4. Execute o seguinte comando para iniciar a API:


     ```
     python manage.py run
     ```


Certifique-se de ter o Python e o PIP instalado em seu computador antes de executar os comandos acima. Lembre-se também de estar no diretório correto do projeto ao executar os comandos.



