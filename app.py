import streamlit as st

st.set_page_config(page_title="Calculadora Conforto 1 UFF", layout="centered")

st.title("Conforto 1 — EAU UFF")
st.subheader("Calculadora de Propriedades Térmicas")
st.write("Metodologia baseada estritamente na ABNT NBR 15220-2.")
st.caption("Importante: Insira as camadas ordenadas obrigatoriamente do EXTERIOR para o INTERIOR.")

# Banco de dados expandido com nomes mobile-first e espessuras normativas padronizadas (NBR 15220-2)
materiais_padrao = {
    # Alvenarias e Blocos de Vedação
    "Bloco Cerâmico 9cm (Tijolo Baiano)": {"lambda": 0.70, "densidade": 1200, "calor_espe": 0.92, "esp_padrao": 9.0, "cat": "Alvenarias e Blocos de Vedação"},
    "Bloco Cerâmico 11.5cm": {"lambda": 0.70, "densidade": 1200, "calor_espe": 0.92, "esp_padrao": 11.5, "cat": "Alvenarias e Blocos de Vedação"},
    "Bloco Cerâmico Estrutural 14cm": {"lambda": 1.05, "densidade": 1600, "calor_espe": 0.92, "esp_padrao": 14.0, "cat": "Alvenarias e Blocos de Vedação"},
    "Bloco de Concreto Comum 14cm": {"lambda": 1.40, "densidade": 1400, "calor_espe": 1.00, "esp_padrao": 14.0, "cat": "Alvenarias e Blocos de Vedação"},
    "Bloco de Concreto Comum 19cm": {"lambda": 1.40, "densidade": 1400, "calor_espe": 1.00, "esp_padrao": 19.0, "cat": "Alvenarias e Blocos de Vedação"},
    "Bloco de Concreto Celular 10cm": {"lambda": 0.18, "densidade": 500, "calor_espe": 1.00, "esp_padrao": 10.0, "cat": "Alvenarias e Blocos de Vedação"},
    "Tijolo Cerâmico Maciço Comum": {"lambda": 0.85, "densidade": 1600, "calor_espe": 0.92, "esp_padrao": 5.7, "cat": "Alvenarias e Blocos de Vedação"},
    "Adobe / Taipa de Pilão": {"lambda": 1.00, "densidade": 1800, "calor_espe": 1.00, "esp_padrao": 30.0, "cat": "Alvenarias e Blocos de Vedação"},
    
    # Concretos e Lajes
    "Concreto Armado": {"lambda": 1.75, "densidade": 2500, "calor_espe": 1.00, "esp_padrao": 10.0, "cat": "Concretos e Lajes"},
    "Concreto Simples (sem armadura)": {"lambda": 1.40, "densidade": 2200, "calor_espe": 1.00, "esp_padrao": 8.0, "cat": "Concretos e Lajes"},
    
    # Revestimentos, Argamassas e Acabamentos
    "Argamassa Cimento/Areia (Reboco)": {"lambda": 1.15, "densidade": 2000, "calor_espe": 1.00, "esp_padrao": 2.5, "cat": "Revestimentos e Argamassas"},
    "Argamassa Cal e Areia": {"lambda": 0.85, "densidade": 1700, "calor_espe": 1.00, "esp_padrao": 2.0, "cat": "Revestimentos e Argamassas"},
    "Gesso Liso para Revestimento": {"lambda": 0.35, "densidade": 1000, "calor_espe": 1.00, "esp_padrao": 1.5, "cat": "Revestimentos e Argamassas"},
    "Placa de Gesso Acartonado (Drywall)": {"lambda": 0.21, "densidade": 800, "calor_espe": 1.00, "esp_padrao": 1.25, "cat": "Revestimentos e Argamassas"},
    "Revestimento em Pedra Natural": {"lambda": 2.60, "densidade": 2600, "calor_espe": 0.90, "esp_padrao": 3.0, "cat": "Revestimentos e Argamassas"},
    "Manta Asfáltica (Impermeabilização)": {"lambda": 0.17, "densidade": 1100, "calor_espe": 1.00, "esp_padrao": 0.4, "cat": "Revestimentos e Argamassas"},
    
    # Coberturas e Forros
    "Telha Cerâmica": {"lambda": 1.05, "densidade": 1800, "calor_espe": 0.92, "esp_padrao": 1.5, "cat": "Coberturas e Forros"},
    "Telha de Fibrocimento": {"lambda": 0.65, "densidade": 1900, "calor_espe": 0.84, "esp_padrao": 0.6, "cat": "Coberturas e Forros"},
    "Telha Metálica Simples": {"lambda": 58.00, "densidade": 7800, "calor_espe": 0.46, "esp_padrao": 0.1, "cat": "Coberturas e Forros"},
    "Forro ou Tábua de Madeira": {"lambda": 0.13, "densidade": 600, "calor_espe": 1.34, "esp_padrao": 1.0, "cat": "Coberturas e Forros"},
    
    # Isolantes Térmicos
    "Lã de Vidro / Mineral": {"lambda": 0.04, "densidade": 40, "calor_espe": 0.80, "esp_padrao": 5.0, "cat": "Isolantes Térmicos"},
    "Poliuretano Expandido (PU)": {"lambda": 0.03, "densidade": 35, "calor_espe": 1.40, "esp_padrao": 3.0, "cat": "Isolantes Térmicos"},
    "Poliestireno Expandido (EPS)": {"lambda": 0.04, "densidade": 20, "calor_espe": 1.45, "esp_padrao": 3.0, "cat": "Isolantes Térmicos"},
    
    # Outros Materiais
    "Vidro Comum": {"lambda": 1.00, "densidade": 2500, "calor_espe": 0.80, "esp_padrao": 0.4, "cat": "Outros Materiais"},
}

if 'camadas' not in st.session_state:
    st.session_state.camadas = []
if 'materiais_custom' not in st.session_state:
    st.session_state.materiais_custom = {}

todos_materiais = {**materiais_padrao, **st.session_state.materiais_custom}

tipo_fluxo = st.selectbox(
    "Tipo de Elemento / Fluxo de Calor:", 
    ["Fluxo Horizontal (Paredes)", "Fluxo Descendente (Coberturas)"]
)

if "Horizontal" in tipo_fluxo:
    R_superficial = 0.13 + 0.04
else:
    R_superficial = 0.17 + 0.04

st.write("---")

with st.expander("Criar Material Customizado para esta Sessão"):
    st.write("Insira o nome e a condutividade térmica do material. Os dados de densidade de massa e calor específico são opcionais.")
    c_nome = st.text_input("Nome do Material Customizado:", placeholder="Ex: Painel OSB")
    
    col_c1, col_c2, col_c3 = st.columns(3)
    with col_c1:
        c_lambda = st.number_input("Condutividade Térmica (λ) [W/m·K]:", min_value=0.01, max_value=400.0, value=1.00, step=0.05)
    with col_c2:
        c_densidade = st.number_input("Densidade de Massa (ρ) [kg/m³] (Opcional):", min_value=0, max_value=10000, value=0, step=50, help="Deixe zero para adotar o padrão de alvenarias")
    with col_c3:
        c_calor = st.number_input("Calor Específico (c) [kJ/kg·K] (Opcional):", min_value=0.0, max_value=5.0, value=0.0, step=0.1, help="Deixe zero para adotar o padrão de alvenarias")
        
    if st.button("Salvar Material na Lista"):
        if c_nome:
            densidade_final = c_densidade if c_densidade > 0 else 1200
            calor_final = c_calor if c_calor > 0.0 else 0.92
            st.session_state.materiais_custom[c_nome] = {
                "lambda": c_lambda, "densidade": densidade_final, "calor_espe": calor_final, "esp_padrao": 2.0, "cat": "Customizados"
            }
            st.success(f"Material '{c_nome}' adicionado!")
            st.rerun()
        else:
            st.error("Por favor, digite um nome para o material customizado.")

st.markdown("### Composição do Elemento")

categorias_ordem = ["Alvenarias e Blocos de Vedação", "Concretos e Lajes", "Revestimentos e Argamassas", "Coberturas e Forros", "Isolantes Térmicos", "Outros Materiais", "Customizados"]
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
            
opcoes_formatadas.append("--- OUTROS ---")
opcoes_formatadas.append("   Câmara de Ar Não Ventilada")
mapa_nomes_reais["   Câmara de Ar Não Ventilada"] = "Câmara de Ar Não Ventilada"

col_l1, col_l2 = st.columns(2)
with col_l1:
    material_sel_formatado = st.selectbox("Selecione o Material:", opcoes_formatadas)
    item_valido = "---" not in material_sel_formatado
    material_sel = mapa_nomes_reais.get(material_sel_formatado, None) if item_valido else None

# Recupera de forma dinâmica a espessura padrão com base no material selecionado no selectbox
if item_valido and material_sel in todos_materiais:
    valor_inicial_espessura = float(todos_materiais[material_sel]["esp_padrao"])
elif material_sel == "Câmara de Ar Não Ventilada":
    valor_inicial_espessura = 2.0
else:
    valor_inicial_espessura = 2.5

with col_l2:
    # O value agora é atualizado dinamicamente pelo estado do selectbox, facilitando o uso mobile
    espessura_sel = st.number_input("Espessura (cm):", min_value=0.01, max_value=100.0, value=valor_inicial_espessura, step=0.5, key=f"esp_{material_sel}")

if st.button("Adicionar Camada"):
    if item_valido and material_sel:
        st.session_state.camadas.append({"material": material_sel, "espessura": espessura_sel})
        st.rerun()
    else:
        st.error("Por favor, selecione um material válido dentro das categorias.")

R_camadas = 0.0
C_total = 0.0

if st.session_state.camadas:
    st.write("---")
    st.write("#### Camadas Inseridas (Ext -> Int):")
    
    for i, camada in enumerate(st.session_state.camadas):
        nome_m = camada["material"]
        e_cm = camada["espessura"]
        e_m = e_cm / 100.0
        
        if nome_m == "Câmara de Ar Não Ventilada":
            # Valores de R para câmara de ar conforme orientação do fluxo (Tabela NBR 15220-2)
            if "Horizontal" in tipo_fluxo:
                R_camada = 0.16 # Espessura média usual entre 2cm e 5cm
            else:
                R_camada = 0.15 # Fluxo descendente
            c_lambda_str = "-"
            p_str = "-"
            c_str = "-"
            C_camada = 0.0
        else:
            dados = todos_materiais[nome_m]
            R_camada = e_m / dados["lambda"]
            C_camada = (dados["densidade"] * (dados["calor_espe"] * 1000) * e_m) / 1000.0
            c_lambda_str = f"{dados['lambda']:.2f}"
            p_str = f"{dados['densidade']}"
            c_str = f"{dados['calor_espe']:.2f}"
            
        R_camadas += R_camada
        C_total += C_camada
        
        st.text(f"{i+1}. {nome_m} ({e_cm} cm)\n   λ: {c_lambda_str} | ρ: {p_str} | c: {c_str} | R: {R_camada:.3f}")

    if st.button("Limpar Composição"):
        st.session_state.camadas = []
        st.rerun()

    R_total = R_superficial + R_camadas
    U_final = 1.0 / R_total

    st.write("---")
    st.markdown("### Resultados Finais")
    st.metric(label="Transmitância Térmica (U) [W/m²·K]", value=f"{U_final:.2f}")
    st.metric(label="Capacidade Térmica (C) [kJ/m²·K]", value=f"{C_total:.1f}")

st.write("---")
st.caption("Desenvolvido para a disciplina de Conforto Ambiental I — EAU UFF.")
