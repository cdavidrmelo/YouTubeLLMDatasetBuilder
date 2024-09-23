import yt_dlp

# URL do vídeo
url = 'https://www.youtube.com/watch?v=9bZkp7q19f0'

# Função para imprimir as informações do vídeo
def get_video_info(url):
    with yt_dlp.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False)

        print(f"Título: {info_dict.get('title', 'N/A')}")
        print(f"Duração: {info_dict.get('duration', 'N/A')} segundos")
        print(f"Descrição: {info_dict.get('description', 'N/A')}")
        print(f"Número de visualizações: {info_dict.get('view_count', 'N/A')}")
        print(f"Autor: {info_dict.get('uploader', 'N/A')}")
        print(f"Data de publicação: {info_dict.get('upload_date', 'N/A')}")
        print(f"URL da thumbnail: {info_dict.get('thumbnail', 'N/A')}")

        # Listar os formatos disponíveis
        print("\nFormatos disponíveis:")
        for format in info_dict['formats']:
            print(f"Format ID: {format['format_id']}, Extensão: {format['ext']}, Resolução: {format.get('resolution', 'N/A')}")

# Chamar a função
get_video_info(url)