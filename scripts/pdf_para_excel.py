"""
pdf_para_excel.py — O fim da digitação manual.
Extrai tabelas de um PDF e gera uma planilha Excel limpa.
"""

import sys
import os
import pandas as pd
import tabula


def extrair_tabelas(caminho_pdf, caminho_saida="tabelas_extraidas.xlsx"):
    """
    Lê um PDF com tabelas e exporta para Excel.
    Cada tabela vira uma aba separada.
    """

    if not os.path.isfile(caminho_pdf):
        print(f"❌ Arquivo '{caminho_pdf}' não encontrado.")
        return

    print(f"🔍 Lendo: {caminho_pdf}")
    print("⏳ Extraindo tabelas...\n")

    tabelas = tabula.read_pdf(caminho_pdf, pages="all", multiple_tables=True)

    if not tabelas:
        print("❌ Nenhuma tabela encontrada no PDF.")
        return

    with pd.ExcelWriter(caminho_saida, engine="openpyxl") as writer:
        for i, tabela in enumerate(tabelas):
            nome_aba = f"Tabela_{i+1}"
            tabela.to_excel(writer, sheet_name=nome_aba, index=False)
            print(f"  ✅ {nome_aba} — {tabela.shape[0]} linhas x {tabela.shape[1]} colunas")

    print(f"\n🎉 PRONTO! Planilha gerada: '{caminho_saida}'")
    print(f"📊 Total de tabelas extraídas: {len(tabelas)}")
    print(f"⏱️  Tempo manual: ~2 horas. Tempo do script: segundos.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        pdf = sys.argv[1]
    else:
        pdf = input("📄 Caminho do arquivo PDF: ").strip()

    if len(sys.argv) > 2:
        saida = sys.argv[2]
    else:
        saida = input("💾 Nome do arquivo de saída (padrão: tabelas_extraidas.xlsx): ").strip()
        if not saida:
            saida = "tabelas_extraidas.xlsx"

    extrair_tabelas(pdf, saida)
