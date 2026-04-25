"""
junta_pdfs.py — O estagiário digital.
Arraste uma pasta com PDFs e ele gera um arquivo único.
Funciona no Linux, MacOS e Windows.
"""

import os
import sys
from PyPDF2 import PdfMerger


def juntar_pdfs(caminho_pasta, arquivo_saida="final_unificado.pdf"):
    """
    Junta todos os PDFs de uma pasta em um único arquivo.
    Ordem alfabética. Sem drama.
    """

    if not os.path.isdir(caminho_pasta):
        print(f"❌ Pasta '{caminho_pasta}' não encontrada.")
        return

    pdfs = [
        arquivo
        for arquivo in os.listdir(caminho_pasta)
        if arquivo.lower().endswith(".pdf")
    ]
    pdfs.sort()

    if not pdfs:
        print("❌ Nenhum PDF encontrado na pasta.")
        return

    merger = PdfMerger()

    print(f"📄 {len(pdfs)} PDFs encontrados. Juntando...\n")

    for pdf in pdfs:
        caminho_completo = os.path.join(caminho_pasta, pdf)
        print(f"  ✅ {pdf}")
        merger.append(caminho_completo)

    merger.write(arquivo_saida)
    merger.close()

    print(f"\n🎉 PRONTO! Arquivo gerado: '{arquivo_saida}'")
    print(f"⏱️  Tempo manual: ~10 minutos. Tempo do script: < 1 segundo.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        pasta = sys.argv[1]
    else:
        pasta = input("📂 Caminho da pasta com os PDFs: ").strip()

    juntar_pdfs(pasta)
