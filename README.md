# 🏢 Calculadora de Propriedades Térmicas — Conforto 1 EAU UFF

Esta é uma ferramenta web interativa e de código aberto desenvolvida especificamente como suporte didático para os estudantes de Arquitetura e Urbanismo da **Escola de Arquitetura e Urbanismo da Universidade Federal Fluminense (EAU UFF)**, no escopo da disciplina de **Conforto Ambiental I**.

O aplicativo substitui ferramentas analíticas antigas, permitindo que os alunos simulem, camada por camada, a composição de paredes e coberturas diretamente do navegador ou de seus smartphones. O objetivo pedagógico principal é fornecer uma percepção prática de escala e das características físicas dos materiais construídos, indo além da memorização puramente numérica.

---

📜 Autoria e Créditos

Este aplicativo foi idealizado e desenvolvido como parte das atividades de estágio docência na disciplina de Conforto Ambiental I:
• Desenvolvedor e Autor: Brendo Tavares dos Santos (Estagiário Docente / Mestrando PPGAU UFF)
• Professora Orientadora: Marília Ramalho Fontenelle
• Instituição: Escola de Arquitetura e Urbanismo — Universidade Federal Fluminense (EAU UFF)
Os dados térmicos de referência e parâmetros de cálculo seguem rigorosamente as tabelas oficiais vigentes da Associação Brasileira de Normas Técnicas (ABNT).

---

## 📊 Parâmetros Calculados

A calculadora processa em tempo real os critérios exigidos pelas normas técnicas brasileiras (**ABNT NBR 15220-2** e **ABNT NBR 15575**):

1. **Transmitância Térmica ($U$):** Avaliação do fluxo de calor em regime estacionário, considerando as resistências superficiais internas e externas aplicáveis.
2. **Capacidade Térmica ($C$):** Mensuração da inércia térmica acumulada pelo componente a partir da espessura, densidade de massa e calor específico de cada material.
3. **Diretrizes para Projeto:** Auxílio na verificação dos requisitos da NBR 15575 para Zonas Bioclimáticas, com foco nos parâmetros recomendados para regiões de alta densidade urbana e climas litorâneos (como Niterói), onde se prioriza a correta associação de transmitância e capacidade térmica adequadas.

---

## 🧱 Componentes e Materiais Disponíveis

O banco de dados nativo do aplicativo é fundamentado nas propriedades físicas estritas da **NBR 15220-2**, abrangendo sistemas comuns na construção civil brasileira e na autoconstrução em cenários de interesse social:
* Argamassa tradicional de cimento e areia (Reboco)
* Bloco Cerâmico Furado (Tijolo Baiano)
* Bloco de Concreto (Vedação e Estrutural)
* Concreto Armado (Lajes, pilares e vigas)
* Telhas Cerâmicas e de Fibrocimento
* Forros de Madeira e Gesso Acartonado
* Câmaras de ar não ventiladas (com resistências embutidas conforme fluxo)
* Opção de inserção customizada para Condutividade Térmica ($\lambda$) de novos materiais.

---

## 📱 Como Utilizar em Sala de Aula

O aplicativo foi projetado com foco em dispositivos móveis para facilitar o uso prático durante os exercícios de atelier e análises de casos reais.

### Acesso Direto (Celular ou Computador)
Caso o deploy na nuvem esteja ativo, acesse o link permanente fornecido em aula.

### Execução Local (Desenvolvimento/Professor)
Caso queira rodar o servidor localmente na sua máquina, siga os passos abaixo no terminal:

1. Certifique-se de ter o Python instalado.
2. Clone este repositório:
   ```bash
   git clone https://github.com
   ```
3. Acesse a pasta do projeto:
   ```bash
   cd calculadora-conforto-uff
   ```
4. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
5. Inicie o servidor do Streamlit:
   ```bash
   streamlit run app.py
   ```

---

## 🛠️ Tecnologias Utilizadas

* **Python** (Linguagem de programação principal)
* **Streamlit** (Framework de interface gráfica e ambiente web reativo)
* **Pandas** (Estruturação e manipulação dos dados de materiais)

---

## 📜 Licença e Créditos

Desenvolvido para fins exclusivamente educacionais na Escola de Arquitetura e Urbanismo — UFF. 
Os dados térmicos de referência seguem as tabelas oficiais vigentes da Associação Brasileira de Normas Técnicas (ABNT).
