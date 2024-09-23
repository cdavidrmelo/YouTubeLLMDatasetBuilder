import yt_dlp
import os

# Diretório
download_path = os.path.join(os.getcwd(), 'Download')
os.makedirs(download_path, exist_ok=True)

# Configurações
# Salva o video na pasta
ydl_opts = {
    'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  
}

# vídeo de teste
url = 'https://www.youtube.com/watch?v=9bZkp7q19f0'

# Download
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

# Confirmação
print(f'Vídeo baixado com sucesso em {download_path}')

