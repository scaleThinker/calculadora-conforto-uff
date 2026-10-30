import streamlit as st

# 1. Configuracao da pagina para o ambiente mobile sem elementos visuais extras
st.set_page_config(page_title="Calculadora Conforto 1 UFF", layout="centered")

st.title("Conforto 1 — EAU UFF")
st.subheader("Calculadora de Propriedades Térmicas")
st.write("Insira as camadas de fora para dentro para calcular a Transmitância (U) e a Capacidade Térmica (C).")

# 2. Banco de dados expandido com os 20 materiais da NBR 15220-2 organizados por categorias corretas
materiais_padrao = {
    # Alvenarias e Blocos de Vedacao
    "Bloco cerâmico com furos horizontais (Tijolo baiano)": {"lambda": 0.70, "densidade": 1200, "calor_espe": 0.92, "cat": "Alvenarias e Blocos de Vedação"},
    "Bloco cerâmico com furos verticais (Estrutural)": {"lambda": 1.05, "densidade": 1600, "calor_espe": 0.92, "cat": "Alvenarias e Blocos de Vedação"},
    "Bloco de concreto (Vedação comum)": {"lambda": 1.40, "densidade": 1400, "calor_espe": 1.00, "cat": "Alvenarias e Blocos de Vedação"},
    "Bloco de concreto celular autoclavado": {"lambda": 0.18, "densidade": 500, "calor_espe": 1.00, "cat": "Alvenarias e Blocos de Vedação"},
    "Tijolo cerâmico maciço comum": {"lambda": 0.85, "densidade": 1600, "calor_espe": 0.92, "cat": "Alvenarias e Blocos de Vedação"},
    
    # Concretos
    "Concreto armado": {"lambda": 1.75, "densidade": 2500, "calor_espe": 1.00, "cat": "Concretos"},
    "Concreto simples (sem armadura)": {"lambda": 1.40, "densidade": 2200, "calor_espe": 1.00, "cat": "Concretos"},
    
    # Revestimentos e Argamassas
    "Argamassa de cimento e areia (Reboco tradicional)": {"lambda": 1.15, "densidade": 2000, "calor_espe": 1.00, "cat": "Revestimentos e Argamassas"},
    "Argamassa de cal e areia": {"lambda": 0.85, "densidade": 1700, "calor_espe": 1.00, "cat": "Revestimentos e Argamassas"},
    "Gesso liso para revestimento": {"lambda": 0.35, "densidade": 1000, "calor_espe": 1.00, "cat": "Revestimentos e Argamassas"},
    "Placa de gesso acartonado (Drywall)": {"lambda": 0.21, "densidade": 800, "calor_espe": 1.00, "cat": "Revestimentos e Argamassas"},
    
    # Coberturas e Forros
    "Telha cerâmica": {"lambda": 1.05, "densidade": 1800, "calor_espe": 0.92, "cat": "Coberturas e Forros"},
    "Telha de fibrocimento": {"lambda": 0.65, "densidade": 1900, "calor_espe": 0.84, "cat": "Coberturas e Forros"},
    "Telha metálica simples": {"lambda": 58.00, "densidade": 7800, "calor_espe": 0.46, "cat": "Coberturas e Forros"},
    "Forro ou tábua de madeira (Pinus/Eucalipto)": {"lambda": 0.13, "densidade": 600, "calor_espe": 1.34, "cat": "Coberturas e Forros"},
    
    # Isolantes Termicos
    "Lã de vidro / Lã mineral": {"lambda": 0.04, "densidade": 40, "calor_espe": 0.80, "cat": "Isolantes Térmicos"},
    "Poliuretano expandido (PU)": {"lambda": 0.03, "densidade": 35, "calor_espe": 1.40, "cat": "Isolantes Térmicos"},
    "Poliestireno expandido (EPS / Isopor)": {"lambda": 0.04, "densidade": 20, "calor_espe": 1.45, "cat": "Isolantes Térmicos"},
    
    # Outros Materiais
    "Vidro comum": {"lambda": 1.00, "densidade": 2500, "calor_espe": 0.80, "cat": "Outros Materiais"},
    "Solo compactado (Taipa/Adobe)": {"lambda": 1.00, "densidade": 1800, "calor_espe": 1.00, "cat": "Outros Materiais"},
}

# 3. Gerenciamento do estado da sessao para persistencia das camadas e customizacoes
if 'camadas' not in st.session_state:
    st.session_state.camadas = []
if 'materiais_custom' not in st.session_state:
    st.session_state.materiais_custom = {}

# Combina a lista fixa com os materiais criados pelo aluno na sessao corrente
todos_materiais = {**materiais_padrao, **st.session_state.materiais_custom}

# 4. Definicao das condicoes de contorno com nomenclatura direta por fluxo físico
tipo_fluxo = st.selectbox(
    "Tipo de Elemento / Fluxo de Calor:", 
    ["Fluxo Horizontal (Paredes)", "Fluxo Descendente (Coberturas)"]
)

if "Horizontal" in tipo_fluxo:
    R_superficial = 0.13 + 0.04  # Rsi + Rse = 0.17 m²K/W
else:
    R_superficial = 0.17 + 0.04  # Rsi + Rse = 0.21 m²K/W

st.write("---")

# 5. Secao de Criacao de Material Customizado simplificada com propriedades físicas explícias
with st.expander("Criar Material Customizado para esta Sessão"):
    st.write("Insira o nome e a condutividade térmica do material. Os dados de densidade de massa e calor específico são dicionais.")
    c_nome = st.text_input("Nome do Material Customizado:", placeholder="Ex: Tijolo Ecológico")
    
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
                "lambda": c_lambda, "densidade": densidade_final, "calor_espe": calor_final, "cat": "Customizados"
            }
            st.success(f"Material '{c_nome}' adicionado com sucesso!")
            st.rerun()
        else:
            st.error("Por favor, digite um nome para o material customizado.")

# 6. Secao principal de entrada de dados unificada
st.markdown("### Composição do Elemento")

# Separando os materiais em subcategorias com ordem alfabetica dentro de cada uma
categorias_ordem = [
    "Alvenarias e Blocos de Vedação", 
    "Concretos", 
    "Revestimentos e Argamassas", 
    "Coberturas e Forros", 
    "Isolantes Térmicos", 
    "Outros Materiais",
    "Customizados"
]

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
with col_l2:
    espessura_sel = st.number_input("Espessura (cm):", min_value=0.1, max_value=100.0, value=2.5, step=0.5)

if st.button("Adicionar Camada"):
    if item_valido and material_sel:
        st.session_state.camadas.append({"material": material_sel, "espessura": espessura_sel})
    else:
        st.error("Por favor, selecione um material válido dentro das categorias.")

# 7. Processamento das Camadas e lista simples de exclusao
R_camadas = 0.0
C_total = 0.0

if st.session_state.camadas:
    st.write("---")
    st.write("#### Camadas Atuais (De fora para dentro):")
    
    # Criamos um seletor simples de exclusao para evitar quebra de layout mobile
    lista_exclusao = []
    
    for idx, cam in enumerate(st.session_state.camadas):
        esp_m = cam["espessura"] / 100.0
        
        if cam["material"] == "Câmara de Ar Não Ventilada":
            R_camada = 0.18
            C_camada = 0.0
            st.write(f"Camada {idx+1}: {cam['material']} | {cam['espessura']} cm")
        else:
            props = todos_materiais[cam["material"]]
            R_camada = esp_m / props["lambda"]
            C_camada = esp_m * props["densidade"] * props["calor_espe"]
            st.write(f"Camada {idx+1}: {cam['material']} | {cam['espessura']} cm (λ: {props['lambda']})")
            
        R_camadas += R_camada
        C_total += C_camada
        lista_exclusao.append(f"Camada {idx+1}: {cam['material']} ({cam['espessura']} cm)")

    st.write("")
    
    # Interface direta para remover uma camada sem quebrar colunas no celular
    col_remover, col_limpar = st.columns(2)
    with col_remover:
        camada_para_remover = st.selectbox("Remover uma camada específica:", ["Selecione..."] + lista_exclusao)
        if camada_para_remover != "Selecione...":
            idx_remover = lista_exclusao.index(camada_para_remover)
            st.session_state.camadas.pop(idx_remover)
            st.rerun()
    with col_limpar:
        st.write("") # Espacamento visual
        if st.button("Limpar Todas as Camadas", use_container_width=True):
            st.session_state.camadas = []
            st.rerun()

# 8. Renderizacao dos Resultados Finais
if R_camadas > 0:
    R_total = R_camadas + R_superficial
    U_total = 1.0 / R_total
    
    st.write("---")
    st.markdown("### Resultados Finais")
    
    res1, res2 = st.columns(2)
    with res1:
        st.metric(label="Transmitância Térmica (U)", value=f"{U_total:.3f} W/(m²·K)")
    with res2:
        st.metric(label="Capacidade Térmica (C)", value=f"{C_total:.1f} kJ/(m²·K)")
