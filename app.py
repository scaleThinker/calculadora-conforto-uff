import streamlit as st

st.set_page_config(page_title="Calculadora Conforto 1 UFF", layout="centered")

st.title("Conforto 1 — EAU UFF")
st.subheader("Calculadora de Propriedades Térmicas")

st.write("Metodologia baseada estritamente na ABNT NBR 15220-2.")
st.caption("⚠️ Importante: Insira as camadas ordenadas obrigatoriamente do EXTERIOR para o INTERIOR.")

# #SESSÃO 3
materiais_padrao = {
    "Bloco cerâmico furado (9 cm)": {"lambda": 0.70, "densidade": 1200, "calor_espe": 0.92, "esp_padrao": 9.0, "bloqueado": True, "cat": "Alvenarias e Blocos de Vedação"},
    "Bloco cerâmico furado (11.5 cm)": {"lambda": 0.70, "densidade": 1200, "calor_espe": 0.92, "esp_padrao": 11.5, "bloqueado": True, "cat": "Alvenarias e Blocos de Vedação"},
    "Bloco cerâmico estrutural (14 cm)": {"lambda": 1.05, "densidade": 1600, "calor_espe": 0.92, "esp_padrao": 14.0, "bloqueado": True, "cat": "Alvenarias e Blocos de Vedação"},
    "Bloco de concreto vedação (9 cm)": {"lambda": 1.40, "densidade": 1400, "calor_espe": 1.00, "esp_padrao": 9.0, "bloqueado": True, "cat": "Alvenarias e Blocos de Vedação"},
    "Bloco de concreto vedação (14 cm)": {"lambda": 1.40, "densidade": 1400, "calor_espe": 1.00, "esp_padrao": 14.0, "bloqueado": True, "cat": "Alvenarias e Blocos de Vedação"},
    "Bloco de concreto celular (10 cm)": {"lambda": 0.18, "densidade": 500, "calor_espe": 1.00, "esp_padrao": 10.0, "bloqueado": True, "cat": "Alvenarias e Blocos de Vedação"},
    "Tijolo cerâmico maciço comum": {"lambda": 0.85, "densidade": 1600, "calor_espe": 0.92, "esp_padrao": 5.7, "bloqueado": False, "cat": "Alvenarias e Blocos de Vedação"},
    "Tijolo ecológico / Solo-cimento": {"lambda": 1.00, "densidade": 1700, "calor_espe": 1.00, "esp_padrao": 12.5, "bloqueado": False, "cat": "Alvenarias e Blocos de Vedação"},
    
    "Concreto armado": {"lambda": 1.75, "densidade": 2500, "calor_espe": 1.00, "esp_padrao": 10.0, "bloqueado": False, "cat": "Concretos"},
    "Concreto simples": {"lambda": 1.40, "densidade": 2200, "calor_espe": 1.00, "esp_padrao": 8.0, "bloqueado": False, "cat": "Concretos"},
    
    "Argamassa cimento/areia (Reboco)": {"lambda": 1.15, "densidade": 2000, "calor_espe": 1.00, "esp_padrao": 2.5, "bloqueado": False, "cat": "Revestimentos e Argamassas"},
    "Argamassa de cal e areia": {"lambda": 0.85, "densidade": 1700, "calor_espe": 1.00, "esp_padrao": 2.0, "bloqueado": False, "cat": "Revestimentos e Argamassas"},
    "Contrapiso (Argamassa de cimento)": {"lambda": 1.15, "densidade": 2000, "calor_espe": 1.00, "esp_padrao": 3.0, "bloqueado": False, "cat": "Revestimentos e Argamassas"},
    "Gesso liso para revestimento": {"lambda": 0.35, "densidade": 1000, "calor_espe": 1.00, "esp_padrao": 1.0, "bloqueado": False, "cat": "Revestimentos e Argamassas"},
    "Pedra natural para revestimento": {"lambda": 2.40, "densidade": 2600, "calor_espe": 1.00, "esp_padrao": 3.0, "bloqueado": False, "cat": "Revestimentos e Argamassas"},
    "Piso cerâmico / Azulejo": {"lambda": 1.05, "densidade": 1800, "calor_espe": 0.92, "esp_padrao": 1.0, "bloqueado": False, "cat": "Revestimentos e Argamassas"},
    "Placa de gesso acartonado (Drywall)": {"lambda": 0.21, "densidade": 800, "calor_espe": 1.00, "esp_padrao": 1.25, "bloqueado": True, "cat": "Revestimentos e Argamassas"},
    
    "Camada de impermeabilização (Asfalto)": {"lambda": 0.22, "densidade": 1100, "calor_espe": 1.00, "esp_padrao": 0.4, "bloqueado": True, "cat": "Coberturas e Forros"},
    "Forro de gesso (Placa plaqueada)": {"lambda": 0.35, "densidade": 1000, "calor_espe": 1.00, "esp_padrao": 1.2, "bloqueado": True, "cat": "Coberturas e Forros"},
    "Forro ou tábua de madeira": {"lambda": 0.13, "densidade": 600, "calor_espe": 1.34, "esp_padrao": 1.0, "bloqueado": False, "cat": "Coberturas e Forros"},
    "Telha cerâmica": {"lambda": 1.05, "densidade": 1800, "calor_espe": 0.92, "esp_padrao": 1.0, "bloqueado": True, "cat": "Coberturas e Forros"},
    "Telha de fibrocimento": {"lambda": 0.65, "densidade": 1900, "calor_espe": 0.84, "esp_padrao": 0.8, "bloqueado": True, "cat": "Coberturas e Forros"},
    "Telha metálica simples": {"lambda": 58.00, "densidade": 7800, "calor_espe": 0.46, "esp_padrao": 0.1, "bloqueado": True, "cat": "Coberturas e Forros"},
    "Telha sanduíche (EPS 30 mm)": {"lambda": 0.038, "densidade": 40, "calor_espe": 1.40, "esp_padrao": 3.1, "bloqueado": True, "cat": "Coberturas e Forros"},
    "Telha sanduíche (PU 30 mm)": {"lambda": 0.028, "densidade": 45, "calor_espe": 1.40, "esp_padrao": 3.1, "bloqueado": True, "cat": "Coberturas e Forros"},
    
    "Câmara de Ar Não Ventilada (5 mm)": {"lambda": None, "densidade": 0, "calor_espe": 0.0, "esp_padrao": 0.5, "bloqueado": True, "cat": "Câmaras de Ar"},
    "Câmara de Ar Não Ventilada (7 mm)": {"lambda": None, "densidade": 0, "calor_espe": 0.0, "esp_padrao": 0.7, "bloqueado": True, "cat": "Câmaras de Ar"},
    "Câmara de Ar Não Ventilada (10 mm)": {"lambda": None, "densidade": 0, "calor_espe": 0.0, "esp_padrao": 1.0, "bloqueado": True, "cat": "Câmaras de Ar"},
    "Câmara de Ar Não Ventilada (15 mm)": {"lambda": None, "densidade": 0, "calor_espe": 0.0, "esp_padrao": 1.5, "bloqueado": True, "cat": "Câmaras de Ar"},
    "Câmara de Ar Não Ventilada (20 mm)": {"lambda": None, "densidade": 0, "calor_espe": 0.0, "esp_padrao": 2.0, "bloqueado": True, "cat": "Câmaras de Ar"},
    "Câmara de Ar Não Ventilada (25 mm)": {"lambda": None, "densidade": 0, "calor_espe": 0.0, "esp_padrao": 2.5, "bloqueado": True, "cat": "Câmaras de Ar"},
    "Câmara de Ar Não Ventilada (50 mm)": {"lambda": None, "densidade": 0, "calor_espe": 0.0, "esp_padrao": 5.0, "bloqueado": True, "cat": "Câmaras de Ar"},
    "Câmara de Ar Não Ventilada (100 mm)": {"lambda": None, "densidade": 0, "calor_espe": 0.0, "esp_padrao": 10.0, "bloqueado": True, "cat": "Câmaras de Ar"},
    "Câmara de Ar Não Ventilada (200 mm)": {"lambda": None, "densidade": 0, "calor_espe": 0.0, "esp_padrao": 20.0, "bloqueado": True, "cat": "Câmaras de Ar"},
    "Câmara de Ar Não Ventilada (300 mm)": {"lambda": None, "densidade": 0, "calor_espe": 0.0, "esp_padrao": 30.0, "bloqueado": True, "cat": "Câmaras de Ar"},
    "Câmara de Ar Não Ventilada (>300 mm)": {"lambda": None, "densidade": 0, "calor_espe": 0.0, "esp_padrao": 35.0, "bloqueado": True, "cat": "Câmaras de Ar"},
    
    "Lã de vidro / Lã mineral": {"lambda": 0.04, "densidade": 40, "calor_espe": 0.80, "esp_padrao": 5.0, "bloqueado": False, "cat": "Isolantes Térmicos"},
    "Poliestireno expandido (EPS)": {"lambda": 0.04, "densidade": 20, "calor_espe": 1.45, "esp_padrao": 3.0, "bloqueado": False, "cat": "Isolantes Térmicos"},
    "Poliuretano expandido (PU)": {"lambda": 0.03, "densidade": 35, "calor_espe": 1.40, "esp_padrao": 3.0, "bloqueado": False, "cat": "Isolantes Térmicos"},
    
    "Solo compactado (Taipa/Adobe)": {"lambda": 1.00, "densidade": 1800, "calor_espe": 1.00, "esp_padrao": 30.0, "bloqueado": False, "cat": "Outros Materiais"},
    "Vidro comum": {"lambda": 1.00, "densidade": 2500, "calor_espe": 0.80, "esp_padrao": 0.6, "bloqueado": True, "cat": "Outros Materiais"}
}


#Sessão 4

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

# #SESSÃO 7
st.markdown("### Composição do Elemento")

categorias_disponiveis = ["Alvenarias e Blocos de Vedação", "Concretos", "Revestimentos e Argamassas", "Coberturas e Forros", "Câmaras de Ar", "Isolantes Térmicos", "Outros Materiais"]
if st.session_state.materiais_custom:
    categorias_disponiveis.append("Customizados")

categoria_sel = st.selectbox("1. Escolha a Categoria:", categorias_disponiveis)

materiais_filtrados = sorted([
    nome for nome, dados in todos_materiais.items() if dados["cat"] == categoria_sel
])

material_sel = st.selectbox("2. Selecione o Material:", materiais_filtrados)

if material_sel:
    espessura_inicial = todos_materiais[material_sel]["esp_padrao"]
    deve_bloquear = todos_materiais[material_sel].get("bloqueado", False)
else:
    espessura_inicial = 2.5
    deve_bloquear = False

# Mecanismo de liberação condicional para dimensões específicas de fabricantes
override_espessura = False
if deve_bloquear:
    override_espessura = st.checkbox("Habilitar espessura customizada", value=False, help="Marque para destravar e editar a espessura sugerida.")

if deve_bloquear and not override_espessura:
    espessura_sel = st.number_input("Espessura (cm):", value=espessura_inicial, disabled=True)
else:
    espessura_sel = st.number_input("Espessura (cm):", min_value=0.1, max_value=100.0, value=espessura_inicial, step=0.5)

if st.button("Adicionar Camada"):
    if material_sel:
        st.session_state.camadas.append({"material": material_sel, "espessura": espessura_sel})
        st.rerun()
    else:
        st.error("Por favor, selecione um material válido.")

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

# #SESSÃO 9: Diagrama Esquemático Espacial Dinâmico (Mobile-First Corrigido)
if st.session_state.camadas:
    st.write("---")
    st.markdown("### Diagrama do Elemento (Ext → Int)")
    
    cores_paleta = ["#4A90E2", "#50E3C2", "#F5A623", "#E2849A", "#B8E986", "#9B51E0", "#4A4A4A"]
    
    espessura_total = sum(camada["espessura"] for camada in st.session_state.camadas if camada["material"] in todos_materiais)
    
    if espessura_total > 0:
        is_parede = "Horizontal" in tipo_fluxo
        
        if is_parede:
            # Layout de Parede (Camadas lado a lado)
            html_diagrama = '<div style="display: flex; flex-direction: row; width: 100%; min-height: 200px; border: 2px solid #333; border-radius: 4px; overflow: hidden; background-color: #f9f9f9;">'
        else:
            # Layout de Cobertura (Camadas empilhadas)
            html_diagrama = '<div style="display: flex; flex-direction: column; width: 100%; border: 2px solid #333; border-radius: 4px; overflow: hidden; background-color: #f9f9f9;">'
        
        for idx, camada in enumerate(st.session_state.camadas):
            nome_m = camada["material"]
            if nome_m in todos_materiais:
                esp_cm = camada["espessura"]
                cor = cores_paleta[idx % len(cores_paleta)]
                
                if is_parede:
                    # Correção absoluta: HTML de parede linearizado em uma única linha sem quebras de texto textuais
                    proporcao = (esp_cm / espessura_total) * 100
                    html_diagrama += f"<div style='background-color: {cor}; width: {proporcao}%; display: flex; flex-direction: column; align-items: center; justify-content: space-between; padding: 15px 5px; color: #fff; font-weight: bold; font-size: 11px; text-align: center; border-right: 1px solid rgba(255,255,255,0.3); box-sizing: border-box;'><span style='writing-mode: vertical-rl; transform: rotate(180deg); margin: auto; text-orientation: mixed;'>Camada {idx+1}: {nome_m}</span><span style='background: rgba(0,0,0,0.2); padding: 2px 4px; border-radius: 3px; font-size: 10px; margin-top: 5px; white-space: nowrap;'>{esp_cm} cm</span></div>"
                else:
                    # HTML de cobertura linearizado
                    proporcao = (esp_cm / espessura_total) * 500
                    altura_px = max(int(proporcao), 25)
                    html_diagrama += f"<div style='background-color: {cor}; height: {altura_px}px; display: flex; align-items: center; justify-content: space-between; padding: 0 15px; color: #fff; font-weight: bold; font-size: 13px; border-bottom: 1px solid rgba(255,255,255,0.3);'><span>Camada {idx+1}: {nome_m}</span><span style='background: rgba(0,0,0,0.2); padding: 2px 6px; border-radius: 3px;'>{esp_cm} cm</span></div>"
        
        html_diagrama += '</div>'
        
        st.markdown(html_diagrama, unsafe_allow_html=True)
        st.caption(f"Espessura total do elemento construtivo: {espessura_total:.1f} cm")

# #SESSÃO 10: Verificação de Conformidade de Desempenho (NBR 15575 Atualizada)
if st.session_state.camadas:
    st.write("---")
    
    with st.expander("Verificação de Desempenho Normativo (NBR 15575 - 2024)"):
        st.write("Valide o componente construtivo frente aos limites de referência da NBR 15575.")
        
        # Filtragem das zonas consolidadas conforme os slides de aula
        zona_sel = st.selectbox(
            "Selecione a Zona Bioclimática:",
            ["ZB 1-2", "ZB 3-4", "ZB 5-6"]
        )
        
        absortancia = st.number_input(
            "Absortância Solar da Superfície (α):", 
            min_value=0.0, max_value=1.0, value=0.3, step=0.05,
            help="Cores claras: α ≤ 0.6 (paredes) ou α ≤ 0.4 (coberturas ZB 5-6). Cores escuras: valores acima destes."
        )
            
        is_parede = "Horizontal" in tipo_fluxo
        mensagem_validacao = ""
        sucesso = True
        
        # ---- FLUXO 1: AVALIAÇÃO DE PAREDES EXTERNAS (PARTE IV) ----
        if is_parede:
            st.markdown("**Componente Analisado: Parede Externa**")
            
            # Limites de Transmitância Térmica (Tabela 13)
            if zona_sel == "ZB 1-2":
                limite_U = 2.7
            else:  # ZB 3-4 e ZB 5-6
                limite_U = 3.7 if absortancia <= 0.6 else 2.5
            
            if U_final > limite_U:
                mensagem_validacao += f"❌ **Transmitância Térmica (U):** O valor calculado de {U_final:.2f} W/(m²·K) ultrapassa o limite máximo permitido de U ≤ {limite_U} W/(m²·K).\n\n"
                sucesso = False
                
            # Limites de Capacidade Térmica (Tabela 14)
            if zona_sel in ["ZB 1-2", "ZB 3-4"]:
                if C_total < 130.0:
                    mensagem_validacao += f"❌ **Capacidade Térmica (C):** O valor de {C_total:.2f} kJ/(m²·K) está abaixo do mínimo obrigatório de C ≥ 130 kJ/(m²·K) para inércia térmica.\n\n"
                    sucesso = False
            else:
                st.caption("ℹ️ Sem requisitos obrigatórios de Capacidade Térmica (C) para paredes nesta zona.")
                
        # ---- FLUXO 2: AVALIAÇÃO DE COBERTURAS (PARTE V) ----
        else:
            st.markdown("**Componente Analisado: Cobertura**")
            st.caption("ℹ️ Não há exigências regulamentares quanto à capacidade térmica (C) para coberturas.")
            
            # Inicialização do Fator de Correção (FT)
            ft = 1.0
            
            # Aplicação das regras específicas para ZB 5-6 com ático ventilado
            if zona_sel == "ZB 5-6":
                is_ventilado = st.checkbox("A cobertura possui ático ventilado / beirais opostos abertos?", value=False)
                if is_ventilado:
                    h_abertura = st.number_input("Altura da abertura do beiral (h) em cm:", min_value=1.0, max_value=200.0, value=50.0, step=5.0)
                    # Fórmula matemática exata extraída do slide da NBR 15575-5
                    if h_abertura > 0:
                        ft = 1.17 - 1.07 * (h_abertura ** -1.04)
                    st.caption(f"Fator de Correção de Transmitância Calculado: FT = {ft:.2f}")
            
            # Definição dos limites de Transmitância da Cobertura baseados em α e FT (Tabela 5)
            if zona_sel == "ZB 1-2":
                limite_U = 2.30
            elif zona_sel == "ZB 3-4":
                limite_U = 2.30 if absortancia <= 0.6 else 1.50
            elif zona_sel == "ZB 5-6":
                # Aplica o FT diretamente multiplicando o valor base regulamentar da tabela
                limite_base = 2.30 if absortancia <= 0.4 else 1.50
                limite_U = limite_base * ft
            
            if U_final > limite_U:
                mensagem_validacao += f"❌ **Transmitância Térmica (U):** O valor de {U_final:.2f} W/(m²·K) ultrapassa o limite máximo corrigido de U ≤ {limite_U:.2f} W/(m²·K).\n\n"
                sucesso = False
                
        # Bloco centralizado de resposta visual para o aluno
        if sucesso:
            st.success("✅ **Componente Aprovado!** Os parâmetros do elemento atendem integralmente aos critérios de desempenho térmico da NBR 15575.")
        else:
            st.error(mensagem_validacao)



# #SESSÃO 11: Memorial de Cálculo e Formulação Normativa (NBR 15220-2)
with st.expander("Para saber mais:"):
    st.markdown("""
    Para conferir os resultados na ponta do lápis seguindo a **ABNT NBR 15220-2**, siga as etapas abaixo:

    ### 1. Transmitância Térmica ($U$)
    A Transmitância Térmica é o inverso da Resistência Térmica Total ($R_T$):
    $$U = \\frac{1}{R_T}$$

    Onde a Resistência Total ($R_T$) é o somatório das resistências superficiais externa ($R_{se}$) e interna ($R_{si}$) com a resistência de cada camada ($R_n$):
    $$R_T = R_{se} + R_{si} + R_1 + R_2 + ... + R_n$$

    **Como calcular a resistência de cada camada ($R_n$):**
    Converta a espessura ($e$) de centímetros para metros e divida pela Condutividade Térmica ($\lambda$) do material:
    $$R = \\frac{e (\\text{em metros})}{\\lambda}$$
    *Nota: Para a Câmara de Ar Não Ventilada, adota-se o valor de $R$ direto da tabela da norma ($0,16$ para paredes ou $0,15$ para coberturas).*

    **Resistências Superficiais Fixas ($R_{se} + R_{si}$):**
    *   **Fluxo Horizontal (Paredes):** $0,04 + 0,13 = 0,17 \\text{ m}^2\\cdot\\text{K/W}$
    *   **Fluxo Descendente (Coberturas):** $0,04 + 0,17 = 0,21 \\text{ m}^2\\cdot\\text{K/W}$

    ---

    ### 2. Capacidade Térmica ($C$)
    A Capacidade Térmica Total do elemento é o somatório da capacidade térmica de cada uma das camadas:
    $$C_{\\text{total}} = C_1 + C_2 + ... + C_n$$

    **Como calcular a capacidade de cada camada ($C_n$):**
    Multiplique a espessura ($e$) em metros, pela Densidade de Massa ($\\rho$) e pelo Calor Específico ($c$):
    $$C = e (\\text{em metros}) \\times \\rho \\times c$$
    *Nota: A Câmara de Ar Não Ventilada não possui capacidade térmica ($C = 0$).*
    """)


st.write("---")
st.caption("Desenvolvido para fins didáticos — Disciplina de Conforto Ambiental I (EAU UFF)")
st.caption("Desenvolvedor: Brendo Tavares dos Santos")
st.caption("brendotavares@id.uff.br")
st.caption("2026")
