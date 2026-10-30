import streamlit as st

st.set_page_config(page_title="Calculadora Conforto 1 UFF", layout="centered")

st.title("Conforto 1 — EAU UFF")
st.subheader("Calculadora de Propriedades Térmicas")

st.write("Metodologia baseada estritamente na ABNT NBR 15220-2.")
st.caption("⚠️ Importante: Insira as camadas ordenadas obrigatoriamente do EXTERIOR para o INTERIOR.")

materiais_padrao = {
    # Alvenarias e Blocos de Vedação
    "Bloco cerâmico furado (9 cm)": {"lambda": 0.70, "densidade": 1200, "calor_espe": 0.92, "esp_padrao": 9.0, "cat": "Alvenarias e Blocos de Vedação"},
    "Bloco cerâmico furado (11.5 cm)": {"lambda": 0.70, "densidade": 1200, "calor_espe": 0.92, "esp_padrao": 11.5, "cat": "Alvenarias e Blocos de Vedação"},
    "Bloco cerâmico estrutural (14 cm)": {"lambda": 1.05, "densidade": 1600, "calor_espe": 0.92, "esp_padrao": 14.0, "cat": "Alvenarias e Blocos de Vedação"},
    "Bloco de concreto vedação (9 cm)": {"lambda": 1.40, "densidade": 1400, "calor_espe": 1.00, "esp_padrao": 9.0, "cat": "Alvenarias e Blocos de Vedação"},
    "Bloco de concreto vedação (14 cm)": {"lambda": 1.40, "densidade": 1400, "calor_espe": 1.00, "esp_padrao": 14.0, "cat": "Alvenarias e Blocos de Vedação"},
    "Bloco de concreto celular (10 cm)": {"lambda": 0.18, "densidade": 500, "calor_espe": 1.00, "esp_padrao": 10.0, "cat": "Alvenarias e Blocos de Vedação"},
    "Tijolo cerâmico maciço comum": {"lambda": 0.85, "densidade": 1600, "calor_espe": 0.92, "esp_padrao": 5.7, "cat": "Alvenarias e Blocos de Vedação"},
    "Tijolo ecológico / Solo-cimento": {"lambda": 1.00, "densidade": 1700, "calor_espe": 1.00, "esp_padrao": 12.5, "cat": "Alvenarias e Blocos de Vedação"},
    
    # Concretos
    "Concreto armado": {"lambda": 1.75, "densidade": 2500, "calor_espe": 1.00, "esp_padrao": 10.0, "cat": "Concretos"},
    "Concreto simples": {"lambda": 1.40, "densidade": 2200, "calor_espe": 1.00, "esp_padrao": 8.0, "cat": "Concretos"},
    
    # Revestimentos e Argamassas
    "Argamassa cimento/areia (Reboco)": {"lambda": 1.15, "densidade": 2000, "calor_espe": 1.00, "esp_padrao": 2.5, "cat": "Revestimentos e Argamassas"},
    "Argamassa de cal e areia": {"lambda": 0.85, "densidade": 1700, "calor_espe": 1.00, "esp_padrao": 2.0, "cat": "Revestimentos e Argamassas"},
    "Gesso liso para revestimento": {"lambda": 0.35, "densidade": 1000, "calor_espe": 1.00, "esp_padrao": 1.0, "cat": "Revestimentos e Argamassas"},
    "Pedra natural para revestimento": {"lambda": 2.40, "densidade": 2600, "calor_espe": 1.00, "esp_padrao": 3.0, "cat": "Revestimentos e Argamassas"},
    "Placa de gesso acartonado (Drywall)": {"lambda": 0.21, "densidade": 800, "calor_espe": 1.00, "esp_padrao": 1.25, "cat": "Revestimentos e Argamassas"},
    
    # Coberturas e Forros
    "Camada de impermeabilização (Asfalto)": {"lambda": 0.22, "densidade": 1100, "calor_espe": 1.00, "esp_padrao": 0.4, "cat": "Coberturas e Forros"},
    "Forro ou tábua de madeira": {"lambda": 0.13, "densidade": 600, "calor_espe": 1.34, "esp_padrao": 1.0, "cat": "Coberturas e Forros"},
    "Telha cerâmica": {"lambda": 1.05, "densidade": 1800, "calor_espe": 0.92, "esp_padrao": 1.0, "cat": "Coberturas e Forros"},
    "Telha de fibrocimento": {"lambda": 0.65, "densidade": 1900, "calor_espe": 0.84, "esp_padrao": 0.6, "cat": "Coberturas e Forros"},
    "Telha metálica simples": {"lambda": 58.00, "densidade": 7800, "calor_espe": 0.46, "esp_padrao": 0.1, "cat": "Coberturas e Forros"},
    
    # Isolantes Térmicos
    "Lã de vidro / Lã mineral": {"lambda": 0.04, "densidade": 40, "calor_espe": 0.80, "esp_padrao": 5.0, "cat": "Isolantes Térmicos"},
    "Poliestireno expandido (EPS)": {"lambda": 0.04, "densidade": 20, "calor_espe": 1.45, "esp_padrao": 3.0, "cat": "Isolantes Térmicos"},
    "Poliuretano expandido (PU)": {"lambda": 0.03, "densidade": 35, "calor_espe": 1.40, "esp_padrao": 3.0, "cat": "Isolantes Térmicos"},
    
    # Outros Materiais
    "Câmara de Ar Não Ventilada": {"lambda": 0.0, "densidade": 0, "calor_espe": 0.0, "esp_padrao": 2.0, "cat": "Outros Materiais"},
    "Solo compactado (Taipa/Adobe)": {"lambda": 1.00, "densidade": 1800, "calor_espe": 1.00, "esp_padrao": 30.0, "cat": "Outros Materiais"},
    "Vidro comum": {"lambda": 1.00, "densidade": 2500, "calor_espe": 0.80, "esp_padrao": 0.6, "cat": "Outros Materiais"}
}

if 'camadas' not in st.session_state:
    st.session_state.camadas = []
if 'materiais_custom' not in st.session_state:
    st.session_state.materiais_custom = {}

todos_materiais = {**materiais_padrao, **st.session_state.materiais_custom}

# Sessão 5: Seleção de Fluxo e Condições de Contorno Superficiais
tipo_fluxo = st.selectbox(
    "Tipo de Elemento / Fluxo de Calor:", 
    ["Fluxo Horizontal (Paredes)", "Fluxo Descendente (Coberturas)"]
)

if "Horizontal" in tipo_fluxo:
    R_superficial = 0.13 + 0.04
else:
    R_superficial = 0.17 + 0.04

st.write("---")

# Sessão 6: Interface de Criação de Materiais Customizados Temporários
with st.expander("Criar Material Customizado para esta Sessão"):
    st.write("Insira o nome e a condutividade térmica do material. Os dados de densidade de massa e calor específico são opcionais.")
    c_nome = st.text_input("Nome do Material Customizado:", placeholder="Ex: Painel Termoacústico")
    
    col_c1, col_c2, col_c3 = st.columns(3)
    with col_c1:
        c_lambda = st.number_input("Condutividade Térmica (λ) [W/m·K]:", min_value=0.01, max_value=400.0, value=1.00, step=0.05)
    with col_c2:
        c_densidade = st.number_input("Densidade de Massa (ρ) [kg/m³] (Opcional):", min_value=0, max_value=10000, value=0, step=50, help="Deixe zero para adotar o padrão de alvenarias")
    with col_c3:
        c_calor = st.number_input("Calor Específico (c) [kJ/kg·K] (Opcional):", min_value=0.0, max_value=5.0, value=0.0, step=0.1, help="Deixe zero para adotar o padrão de alvenarias")
    
    c_esp = st.number_input("Espessura Padrão Recomendada (cm):", min_value=0.1, max_value=100.0, value=2.5, step=0.5)
        
    if st.button("Salvar Material na Lista"):
        if c_nome:
            densidade_final = c_densidade if c_densidade > 0 else 1200
            calor_final = c_calor if c_calor > 0.0 else 0.92
            st.session_state.materiais_custom[c_nome] = {
                "lambda": c_lambda, "densidade": densidade_final, "calor_espe": calor_final, "esp_padrao": c_esp, "cat": "Customizados"
            }
            st.success(f"Material '{c_nome}' adicionado com sucesso!")
            st.rerun()
        else:
            st.error("Por favor, digite um nome para o material customizado.")

# Sessão 7: Composição do Elemento Construtivo e Automação de Espessuras
st.markdown("### Composição do Elemento")

categorias_ordem = ["Alvenarias e Blocos de Vedação", "Concretos", "Revestimentos e Argamassas", "Coberturas e Forros", "Isolantes Térmicos", "Outros Materiais", "Customizados"]

opcoes_formatadas = []
mapa_nomes_reais = {}

for cat in categorias_ordem:
    materiais_da_cat = sorted([nome for nome, dados in todos_materiais.items() if dados["cat"] == cat])
    if materiais_da_cat:
        opcoes_formatadas.append(f"--- {cat.upper()} ---")
        for mat in materiais_da_cat:
            nome_exibicao = f"   {mat}"
            opcoes_formatadas.append(nome_exibicao)
            mapa_nomes_reais[nome_exibicao] = mat

if 'index_selecionado' not in st.session_state:
    st.session_state.index_selecionado = 1

material_sel_formatado = st.selectbox("Selecione o Material:", opcoes_formatadas, index=st.session_state.index_selecionado)
item_valido = "---" not in material_sel_formatado

material_sel = mapa_nomes_reais.get(material_sel_formatado, None) if item_valido else None

if item_valido and material_sel:
    espessura_inicial = todos_materiais[material_sel]["esp_padrao"]
else:
    espessura_inicial = 2.5

espessura_sel = st.number_input("Espessura (cm):", min_value=0.1, max_value=100.0, value=espessura_inicial, step=0.5)

if st.button("Adicionar Camada"):
    if item_valido and material_sel:
        st.session_state.camadas.append({"material": material_sel, "espessura": espessura_sel})
        st.rerun()
    else:
        st.error("Por favor, selecione um material válido dentro das categorias.")

# Sessão 8: Lista de Camadas Inseridas, Cálculos da NBR 15220-2 e Créditos
R_camadas = 0.0
C_total = 0.0

if st.session_state.camadas:
    st.write("---")
    st.markdown("### Camadas Inseridas (Ext → Int):")
    
    for idx, camada in enumerate(st.session_state.camadas):
        nome_m = camada["material"]
        if nome_m in todos_materiais:
            dados = todos_materiais[nome_m]
            e = camada["espessura"] / 100.0
            
            if nome_m == "Câmara de Air Não Ventilada":
                r_camada = 0.16 if "Horizontal" in tipo_fluxo else 0.15
                c_camada = 0.0
                especificacao_fisica = f"R = {r_camada:.2f} m²·K/W"
            else:
                r_camada = e / dados["lambda"]
                c_camada = (e * dados["densidade"] * dados["calor_espe"])
                especificacao_fisica = f"λ = {dados['lambda']:.2f} W/m·K | ρ = {dados['densidade']} kg/m³ | c = {dados['calor_espe']:.2f} kJ/kg·K"
            
            R_camadas += r_camada
            C_total += c_camada
            
            col_ver, col_del = st.columns([4, 1])
            with col_ver:
                st.write(f"**Camada {idx+1}: {nome_m}** — {camada['espessura']} cm")
                st.caption(especificacao_fisica)
            with col_del:
                if st.button("Remover", key=f"del_{idx}"):
                    st.session_state.camadas.pop(idx)
                    st.rerun()
            st.write("---")

    R_total = R_superficial + R_camadas
    U_final = 1.0 / R_total

    st.markdown("### Propriedades Térmicas Finais")
    st.metric(label="Transmitância Térmica (U)", value=f"{U_final:.2f} W/(m²·K)")
    st.metric(label="Capacidade Térmica (C)", value=f"{C_total:.2f} kJ/(m²·K)")

if st.session_state.camadas:
    if st.button("Limpar Todas as Camadas"):
        st.session_state.camadas = []
        st.rerun()

st.write("---")
st.caption("Desenvolvido para fins didáticos — Disciplina de Conforto Ambiental I (EAU UFF)")
st.caption("Colaboração: Estágio Docente")
