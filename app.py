import streamlit as st
import os
import shutil

st.title("🚀 Organizador de Arquivos")

# Escolher pasta
pasta = st.text_input("Digite o caminho da pasta que deseja organizar:")

# Botão para organizar
if st.button("Organizar"):
    if not os.path.exists(pasta):
        st.error("Pasta não encontrada!")
    else:
        tipos = {
            "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
            "Documentos": [".pdf", ".docx", ".txt"],
            "Vídeos": [".mp4", ".mov", ".avi"]
        }
        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho_arquivo):
                _, ext = os.path.splitext(arquivo)
                for pasta_tipo, extensoes in tipos.items():
                    if ext.lower() in extensoes:
                        destino = os.path.join(pasta, pasta_tipo)
                        os.makedirs(destino, exist_ok=True)
                        shutil.move(caminho_arquivo, os.path.join(destino, arquivo))
        st.success("Arquivos organizados!")
