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
