# Sistema de Gestão de ILPIs – Associação Beija Flor

Este é um sistema web desenvolvido com foco no gerenciamento de Instituições de Longa Permanência para Idosos (ILPIs), criado especialmente para atender às necessidades da **Associação Beija Flor**, localizada na **Avenida dos Coqueiros, 134 - Jardim Suisso, Mairiporã - SP**.

## 🧩 Funcionalidades

### 📁 Cadastros
- **Idosos:** registro completo com nome, data de nascimento, CPF, endereço, observações e vínculo com responsáveis e medicamentos.
- **Responsáveis:** cadastro de responsáveis com nome, telefone e email, vinculados aos idosos.
- **Medicamentos:** cadastro de remédios com nome, marca, categoria, custo, imagem e associação aos idosos.
- **Visitas:** agendamento de visitas de responsáveis aos idosos, com data, horário e observações.

### 📊 Análises e Dashboards
- Visitas por responsável
- Volume de estoque por remédio
- Custo total por medicamento
- Número de idosos por medicamento
- Visualização gráfica utilizando `matplotlib`

### 🔍 Tabelas com Recursos Interativos
- Paginação
- Filtros e buscas por nome, data e observações
- Ordenação por colunas

### 🧾 Tratamento de Erros
- Feedback visual em campos obrigatórios
- Mensagens de sucesso e erro após ações (CRUD)
- Validações nos formulários

## ⚙️ Tecnologias Utilizadas

- **Python 3.13**
- **Django 5.2**
- **HTML5, CSS3, Bootstrap 5**
- **JavaScript**
- **SQLite3** (banco de dados local)
- **Matplotlib** para geração dos gráficos

## 🤝 Contribuição Social

Este projeto está sendo desenvolvido de forma **gratuita e solidária** para a **Associação Beija Flor**, com o intuito de **aprimorar o controle dos registros dos idosos**, seus medicamentos, responsáveis e visitas, oferecendo uma solução moderna e segura para facilitar o dia a dia da instituição.

O desenvolvimento conta com o apoio e supervisão da **UNIVESP – Universidade Virtual do Estado de São Paulo**, como parte de uma iniciativa de impacto social.

## 💻 Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   ```
2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o servidor:
   ```bash
   python manage.py runserver
   ```
