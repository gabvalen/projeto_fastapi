import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==============================
# 🎨 CONFIG GERAL DA PÁGINA
# ==============================
st.markdown(
    "<h3 style='text-align: center; color: #FFFFFF;'>📊 Análise Gráfica de Evasão Escolar</h3>",
    unsafe_allow_html=True
)

# Caminho do CSV
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
csv_path = os.path.join(base_dir, "backend", "dados", "dados_evasao_limpo.csv")

# ==============================
# 📥 LEITURA DOS DADOS
# ==============================
try:
    df = pd.read_csv(csv_path)
except Exception as e:
    st.error(f"❌ Erro ao carregar o arquivo CSV: {e}")
    st.stop()

# ==============================
# 🔤 MAPEAMENTOS TEXTO ↔ NÚMERO
# ==============================
educacao_opcoes = {
    0: "Nenhuma",
    1: "Primário",
    2: "Fundamental",
    3: "Médio",
    4: "Superior"
}

tempo_estudo_opcoes = {
    0: "Muito baixo",
    1: "Baixo",
    2: "Médio",
    3: "Alto",
    4: "Muito alto"
}

# ==============================
# 🧼 CRIAR CÓPIA LIMPA E MAPEAR TEXTO
# ==============================
df_plot = df.copy()

# Converter Dropped_Out para booleano
if df_plot["Dropped_Out"].dtype == object:
    df_plot["Dropped_Out"] = df_plot["Dropped_Out"].astype(str).str.lower().map({"true": True, "false": False})
else:
    df_plot["Dropped_Out"] = df_plot["Dropped_Out"].astype(bool)

# Criar coluna de texto para exibição
df_plot["Dropped_Out_Text"] = df_plot["Dropped_Out"].map({False: "Não Evadido", True: "Evadido"})

# Aplicar mapeamentos adicionais
if "Mother_Education" in df_plot.columns:
    df_plot["Mother_Education"] = df_plot["Mother_Education"].map(educacao_opcoes)

if "Study_Time" in df_plot.columns:
    df_plot["Study_Time"] = df_plot["Study_Time"].map(tempo_estudo_opcoes)

# ==============================
# 🎨 ESTILO GLOBAL DOS GRÁFICOS
# ==============================
plt.style.use("seaborn-v0_8-darkgrid")
sns.set_palette(["#74C69D", "#2D6A4F"])

def format_axes(ax, titulo, xlabel, ylabel):
    ax.set_title(titulo, color="black", fontsize=16, weight="bold")
    ax.set_xlabel(xlabel, color="black", fontsize=12)
    ax.set_ylabel(ylabel, color="black", fontsize=12)
    ax.tick_params(colors="black", labelsize=11)
    for spine in ax.spines.values():
        spine.set_edgecolor("black")

def legend_black(ax, title, labels=None, loc="best"):
    handles, _ = ax.get_legend_handles_labels()
    if labels is None:
        labels = ["Não Evadido", "Evadido"]
    leg = ax.legend(
        handles,
        labels,
        title=title,
        facecolor="white",
        edgecolor="black",
        framealpha=1,
        labelcolor="black",
        title_fontsize=11,
        fontsize=10,
        loc=loc
    )
    plt.setp(leg.get_texts(), color="black")
    plt.setp(leg.get_title(), color="black")

# ==============================
# 📋 OPÇÕES DE GRÁFICOS (1–5)
# ==============================
opcoes = [
    "1️⃣ Distribuição de Evasão",
    "2️⃣ Taxa de Evasão por Tipo de Área (Rural vs Urbana)",
    "3️⃣ Evasão por Idade e Gênero (Linha)",
    "4️⃣ Escolaridade dos Pais x Evasão (Porcentagem)",
    "5️⃣ Tempo de Estudo x Evasão (Área)"
]

tipo = st.selectbox("📈 Escolha o tipo de gráfico:", opcoes)

# ==============================
# 1️⃣ Distribuição geral de evasão (pizza)
# ==============================
if tipo == "1️⃣ Distribuição de Evasão":
    evasao_counts = df_plot["Dropped_Out_Text"].value_counts()

    fig, ax = plt.subplots(figsize=(7, 7))
    cores = ["#74C69D", "#2D6A4F"]

    wedges, texts, autotexts = ax.pie(
        evasao_counts,
        labels=evasao_counts.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=cores,
        textprops={"color": "black", "fontsize": 13, "weight": "bold"},
        wedgeprops={"edgecolor": "white", "linewidth": 2}
    )

    ax.set_title(
        "Distribuição Geral de Evasão Escolar",
        fontsize=18,
        fontweight="bold",
        color="black",
        pad=20
    )
    ax.axis("equal")
    st.pyplot(fig)

# ==============================
# 2️⃣ Gráfico de Pizza — Taxa de Evasão por Tipo de Área (Rural vs Urbana)
# ==============================
elif tipo == "2️⃣ Taxa de Evasão por Tipo de Área (Rural vs Urbana)":
    if not {"Address", "Dropped_Out"}.issubset(df_plot.columns):
        st.error("❌ Colunas necessárias não encontradas no dataset (Address, Dropped_Out).")
    else:
        df_area = df_plot.copy()
        df_area["Dropped_Out"] = (
            df_area["Dropped_Out"]
            .astype(str)
            .str.lower()
            .map({"true": True, "false": False})
        )
        df_area["Tipo_Area"] = df_area["Address"].map({"R": "Rural", "U": "Urbana"})

        taxa_evasao_area = (
            df_area.groupby("Tipo_Area")["Dropped_Out"]
            .mean()
            .reset_index()
            .rename(columns={"Dropped_Out": "Taxa_Evasao"})
        )
        taxa_evasao_area["Taxa_Evasao"] *= 100

        fig, ax = plt.subplots(figsize=(7, 7))
        cores = ["#74C69D", "#2D6A4F"]
        wedges, texts, autotexts = ax.pie(
            taxa_evasao_area["Taxa_Evasao"],
            labels=taxa_evasao_area["Tipo_Area"],
            autopct="%1.1f%%",
            startangle=90,
            colors=cores,
            textprops={"color": "black", "fontsize": 13, "weight": "bold"},
            wedgeprops={"edgecolor": "white", "linewidth": 2}
        )
        ax.set_title(
            "Taxa de Evasão por Tipo de Área (Rural vs Urbana)",
            fontsize=18,
            fontweight="bold",
            color="black",
            pad=20
        )
        ax.axis("equal")
        st.pyplot(fig)

# ==============================
# 3️⃣ Evasão por Idade e Gênero (Gráfico de Linhas Duplas)
# ==============================
elif tipo == "3️⃣ Evasão por Idade e Gênero (Linha)":
    if not {"Age", "Gender", "Dropped_Out"}.issubset(df_plot.columns):
        st.error("❌ Colunas necessárias não encontradas no dataset (Age, Gender, Dropped_Out).")
    else:
        df_aux = df_plot.copy()
        df_aux["Age"] = df_aux["Age"].astype(int)
        df_aux["Gender"] = df_aux["Gender"].map({"M": "Masculino", "F": "Feminino"})
        df_aux["Dropped_Out"] = df_aux["Dropped_Out"].astype(str).str.lower().map({"true": True, "false": False})
        df_aux = df_aux[df_aux["Age"] <= 21]

        total_grp = df_aux.groupby(["Age", "Gender"]).size().reset_index(name="Total")
        evadidos_grp = df_aux[df_aux["Dropped_Out"] == True].groupby(["Age", "Gender"]).size().reset_index(name="Evadidos")

        taxa = pd.merge(total_grp, evadidos_grp, on=["Age", "Gender"], how="left").fillna(0)
        taxa["Taxa_Evasao"] = (taxa["Evadidos"] / taxa["Total"]) * 100
        taxa = taxa.sort_values(["Age", "Gender"])

        fig, ax = plt.subplots(figsize=(10, 6))
        cores_genero = {"Masculino": "#2D6A4F", "Feminino": "#74C69D"}

        for genero, dados in taxa.groupby("Gender"):
            ax.plot(
                dados["Age"],
                dados["Taxa_Evasao"],
                marker="o",
                linewidth=2,
                color=cores_genero.get(genero, "gray"),
                label=genero
            )
            for x, y in zip(dados["Age"], dados["Taxa_Evasao"]):
                offset = 0.7 if genero == "Masculino" else -0.7
                ax.text(x, y + offset, f"{y:.1f}%", color="black", fontsize=9, ha="center")

        ax.set_title("Taxa de Evasão por Idade e Gênero", fontsize=16, fontweight="bold", color="black")
        ax.set_xlabel("Idade", fontsize=12, color="black")
        ax.set_ylabel("Taxa de Evasão (%)", fontsize=12, color="black")
        ax.set_xticks(sorted(taxa["Age"].unique()))
        ax.tick_params(colors="black")
        ax.grid(axis="y", linestyle="--", alpha=0.3)
        legend_black(ax, "Gênero", ["Masculino", "Feminino"], loc="upper left")
        st.pyplot(fig)

# ==============================
# 4️⃣ Escolaridade dos Pais x Evasão (Porcentagem)
# ==============================
elif tipo == "4️⃣ Escolaridade dos Pais x Evasão (Porcentagem)":
    df_tmp = df_plot.copy()
    if df_tmp["Mother_Education"].dtype in ["int64", "float64"]:
        df_tmp["Mother_Education"] = df_tmp["Mother_Education"].map(educacao_opcoes)
    if df_tmp["Father_Education"].dtype in ["int64", "float64"]:
        df_tmp["Father_Education"] = df_tmp["Father_Education"].map(educacao_opcoes)

    ordem_escolaridade = ["Nenhuma", "Primário", "Fundamental", "Médio", "Superior"]
    evasao_mae = df_tmp.groupby("Mother_Education")["Dropped_Out"].mean().mul(100).rename("Taxa_Mae")
    evasao_pai = df_tmp.groupby("Father_Education")["Dropped_Out"].mean().mul(100).rename("Taxa_Pai")

    taxas = pd.concat([evasao_mae, evasao_pai], axis=1).reindex(ordem_escolaridade).fillna(0)
    import numpy as np
    x = np.arange(len(ordem_escolaridade))
    largura = 0.35
    valores_mae = taxas["Taxa_Mae"].to_numpy()
    valores_pai = taxas["Taxa_Pai"].to_numpy()

    fig, ax = plt.subplots(figsize=(10, 6))
    barras_mae = ax.bar(x - largura/2, valores_mae, width=largura, color="#74C69D", edgecolor="black", label="Mãe")
    barras_pai = ax.bar(x + largura/2, valores_pai, width=largura, color="#1B4332", edgecolor="black", label="Pai")

    ax.set_xticks(x)
    ax.set_xticklabels(ordem_escolaridade, rotation=15, ha="right", color="black", fontsize=11)
    ax.set_title("Taxa de Evasão por Escolaridade dos Pais", color="black", fontsize=16, fontweight="bold")
    ax.set_xlabel("Escolaridade", color="black", fontsize=12)
    ax.set_ylabel("Evasão (%)", color="black", fontsize=12)
    ax.tick_params(colors="black", labelsize=11)
    for spine in ax.spines.values():
        spine.set_edgecolor("black")
    ax.grid(True, linestyle="--", alpha=0.4, axis="y")

    legenda = ax.legend(title="Responsável", facecolor="white", edgecolor="black", framealpha=1,
                        labelcolor="black", title_fontsize=11, fontsize=10, loc="upper right")
    plt.setp(legenda.get_texts(), color="black")
    plt.setp(legenda.get_title(), color="black")

    for b in barras_mae:
        altura = b.get_height()
        ax.text(b.get_x() + b.get_width()/2, altura + 0.5, f"{altura:.1f}%", ha="center", va="bottom", color="black", fontsize=10, fontweight="bold")
    for b in barras_pai:
        altura = b.get_height()
        ax.text(b.get_x() + b.get_width()/2, altura + 0.5, f"{altura:.1f}%", ha="center", va="bottom", color="black", fontsize=10, fontweight="bold")

    st.pyplot(fig)

# ==============================
# 5️⃣ Gráfico de Área — Tempo de Estudo × Evasão Escolar
# ==============================
elif tipo == "5️⃣ Tempo de Estudo x Evasão (Área)":
    if not {"Study_Time", "Dropped_Out"}.issubset(df_plot.columns):
        st.error("❌ Colunas necessárias não encontradas no dataset (Study_Time, Dropped_Out).")
    else:
        df_area = df_plot.copy()
        mapa_estudo = {"Muito baixo": 0, "Baixo": 1, "Médio": 2, "Alto": 3, "Muito alto": 4}
        df_area["Study_Time_Num"] = df_area["Study_Time"].map(mapa_estudo)
        df_area = df_area[df_area["Study_Time_Num"] >= 1]
        df_area["Dropped_Out"] = df_area["Dropped_Out"].astype(str).str.lower().map({"true": True, "false": False})
        taxa_area = df_area.groupby("Study_Time_Num")["Dropped_Out"].mean().reset_index().rename(columns={"Dropped_Out": "Taxa_Evasao"})
        taxa_area["Taxa_Evasao"] *= 100

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.fill_between(taxa_area["Study_Time_Num"], taxa_area["Taxa_Evasao"], color="#74C69D", alpha=0.5, label="Taxa de Evasão")
        ax.plot(taxa_area["Study_Time_Num"], taxa_area["Taxa_Evasao"], color="#2D6A4F", linewidth=2.5)

        ax.set_xticks(range(1, 5))
        ax.set_xticklabels(["Baixo", "Médio", "Alto", "Muito alto"], rotation=15)
        ax.set_title("Taxa de Evasão por Tempo de Estudo", fontsize=16, fontweight="bold", color="black")
        ax.set_xlabel("Tempo de Estudo", fontsize=12, color="black")
        ax.set_ylabel("Taxa de Evasão (%)", fontsize=12, color="black")
        ax.tick_params(colors="black")
        ax.grid(axis="y", linestyle="--", alpha=0.3)
        for x, y in zip(taxa_area["Study_Time_Num"], taxa_area["Taxa_Evasao"]):
            ax.text(x, y + 0.5, f"{y:.1f}%", ha="center", color="black", fontsize=10, fontweight="bold")
        legend_black(ax, "Indicador", ["Taxa de Evasão"], loc="upper right")
        st.pyplot(fig)








