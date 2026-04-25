"""
renomeia_em_lote.py — Adeus, "Documento_Final_V3_Revisado2.pdf".
Renomeia centenas de arquivos com um padrão definido por você.
"""

import os
import sys
from pathlib import Path


def renomear_arquivos(caminho_pasta, prefixo="arquivo", extensao=None, numerar=True):
    """
    Renomeia todos os arquivos de uma pasta com prefixo + número.
    Exemplo: foto_001.jpg, foto_002.jpg, foto_003.jpg
    """

    if not os.path.isdir(caminho_pasta):
        print(f"❌ Pasta '{caminho_pasta}' não encontrada.")
        return

    arquivos = [
        f for f in os.listdir(caminho_pasta)
        if os.path.isfile(os.path.join(caminho_pasta, f))
    ]

    if extensao:
        arquivos = [f for f in arquivos if f.lower().endswith(extensao.lower())]

    arquivos.sort()

    if not arquivos:
        print("❌ Nenhum arquivo encontrado.")
        return

    print(f"📁 {len(arquivos)} arquivos encontrados. Renomeando...\n")

    for i, arquivo in enumerate(arquivos, start=1):
        extensao_original = Path(arquivo).suffix
        nome_antigo = os.path.join(caminho_pasta, arquivo)

        if numerar:
            nome_novo = f"{prefixo}_{i:03d}{extensao_original}"
        else:
            nome_novo = f"{prefixo}{extensao_original}"

        caminho_novo = os.path.join(caminho_pasta, nome_novo)

        os.rename(nome_antigo, caminho_novo)
        print(f"  ✅ '{arquivo}' → '{nome_novo}'")

    print(f"\n🎉 PRONTO! {len(arquivos)} arquivos renomeados.")
    print(f"⏱️  Tempo manual: ~30 minutos. Tempo do script: < 1 segundo.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        pasta = sys.argv[1]
    else:
        pasta = input("📂 Caminho da pasta com os arquivos: ").strip()

    prefixo = input("🏷️  Prefixo para os novos nomes (ex: nota_fiscal): ").strip()
    if not prefixo:
        prefixo = "arquivo"

    extensao = input("🔤 Filtrar por extensão? (ex: .pdf, .jpg) ou ENTER para todos: ").strip()
    if not extensao:
        extensao = None

    renomear_arquivos(pasta, prefixo, extensao)
