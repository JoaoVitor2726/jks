# Controle de Medicamentos CLI

Aplicação simples em Python com interface de linha de comando (CLI), desenvolvida para auxiliar no gerenciamento de medicamentos e seus horários de uso. O sistema permite cadastrar, visualizar, marcar como tomado e remover medicamentos, ajudando usuários a manterem uma rotina organizada e segura.

## Problema real
Muitas pessoas, especialmente idosos, pacientes com tratamentos contínuos e cuidadores, enfrentam dificuldades para lembrar os horários corretos de administração de medicamentos. Esse problema pode causar esquecimentos, uso incorreto e impactos negativos na saúde.

## Proposta da solução
A proposta será oferecer uma forma simples e acessível de registrar e acompanhar medicamentos, permitindo controle básico e eficiente da rotina de medicação.

## Público-alvo
- Idosos
- Pacientes em tratamento contínuo
- Cuidadores
- Pessoas com dificuldade de organização de rotina

## Funcionalidades principais
- Adicionar medicamento
- Listar medicamentos cadastrados
- Marcar tarefa como concluída
- Remover tarefa
- Salvar tarefas em arquivo JSON

## Tecnologias utilizadas
- Python 3
- Pytest
- Flake8
- GitHub Actions
- JSON

## Estrutura do projeto
```bash
controle_medicamentos/
├── src/
│   ├── main.py
│   ├── task_manager.py
│   ├── api_service.py
│   └── __init__.py
├── data/
│   └── tasks.json
├── tests/
│   ├── test_task_manager.py
│   └── test_api.py
├── requirements.txt
├── README.md
├── VERSION
└── .github/workflows/ci.yml
```

## Integração com API pública
O sistema utiliza a World Time API para registrar automaticamente o horário real em que um medicamento é marcado como tomado. Ao marcar um medicamento como tomado, o aplicativo chama a API e salva o campo `datetime` retornado por `http://worldtimeapi.org/api/timezone/America/Sao_Paulo`.

## World Time API
A World Time API é um serviço público que fornece a data e hora atuais para fusos horários específicos. Neste projeto, ela é usada para garantir que o registro de tomada seja gravado com o horário real de São Paulo.

## Registro automático de horário
Quando o usuário marca um medicamento como tomado, o sistema:
- consulta a API de horário;
- obtém o campo `datetime` retornado;
- salva o valor em JSON no campo `taken_at`;
- exibe o horário real do registro no terminal.

## Publicação / Deploy
Este projeto pode ser executado localmente como uma aplicação CLI. Para publicar ou implantar, basta manter o repositório atualizado e usar o GitHub Actions para validar cada push e pull request. O workflow já configura Python 3.10, instala dependências, executa lint com `flake8` e roda os testes com `pytest`.

## Instalação
```bash
!Execute no Power Shell ou no CMD do Linux!

git clone https://github.com/JoaoVitor2726/jks.git
cd Controle de Medicamentos
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Execução
```bash
python src/main.py
```

### Exemplo de saída no terminal
```text
PS C:\Users\Arthur\studyflow> python src/main.py
===== CONTROLE DE MEDICAMENTOS =====
1. Adicionar
2. Listar
3. Marcar como tomado
4. Remover
5. Sair
Escolha: 1
Digite a tarefa: Revisar banco de dados
Tarefa adicionada com sucesso!


```
![image](https://github.com/ArthurNeiva017/studyflow/blob/main/docs/Evid%C3%AAncia%20Funcionamento.png)<br>
<strong>A evidência do funcionamento do programa está na pasta `Docs`</strong>

## Como usar
Ao executar o programa, o usuário verá um menu com as opções:

```text
1 - Adicionar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Remover tarefa
5 - Sair
```

## Executar os testes
```bash
pytest
```

## Executar o lint
```bash
ruff check .
```
## Versão do Projeto

O projeto utiliza versionamento semântico no formato MAJOR.MINOR.PATCH.

Versão atual: Study Flow **v1.0.0**

A versão está declarada no arquivo `pyproject.toml` e também no arquivo `VERSION`.

## Autor
João Vitor Belchior Estanislau


