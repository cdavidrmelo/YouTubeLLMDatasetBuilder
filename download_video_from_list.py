import yt_dlp
import os

# Diretório de download
download_path = os.path.join(os.getcwd(), 'Download')
os.makedirs(download_path, exist_ok=True)

# Arquivo com os links
file_path = 'lista_videos.txt'

# Ler o arquivo 
with open(file_path, 'r') as file:
    urls = file.readlines()

# Configuraões
# Salva o video na pasta 
ydl_opts = {
    'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
}

# Download
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for url in urls:
        url = url.strip() 
        if url:  
            try:
                ydl.download([url])
                print(f"Vídeo '{url}' Downwload realizado com sucesso!\n")
            except Exception as e:
                print(f"Erro ao baixar o vídeo: {url}\nErro: {e}\n")

#Confirmação
print("Todos os vídeos foram processados.")
