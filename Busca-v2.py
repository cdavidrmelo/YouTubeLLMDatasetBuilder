from googleapiclient.discovery import build
import yt_dlp
con
# Configurações da API
API_KEY = 'SUA_API_KEY'  # Substitua pela sua chave de API do YouTube DATA v3
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(query, max_results=5, video_type='video', video_license='any', video_duration='any'):
    """
    Função para buscar vídeos no YouTube com base nos parâmetros especificados e extrair metadados.
    
    Parâmetros:
    - query (str): Termo de busca.
    - max_results (int): Número máximo de resultados a serem retornados.
    - video_type (str): Tipo de resultado ('video', 'channel', 'playlist').
    - video_license (str): Tipo de licença do vídeo ('any', 'creativeCommon').
    - video_duration (str): Duração do vídeo ('any', 'long', 'medium', 'short').
    
    Retorna:
    - videos (list): Lista de dicionários contendo todos os metadados disponíveis dos vídeos.
    """
    # Cria um objeto de serviço da API do YouTube
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

    # Executa a busca na API do YouTube com os parâmetros fornecidos
    search_response = youtube.search().list(
        q=query,
        part='snippet',
        maxResults=max_results,
        type=video_type,
        videoLicense=video_license,
        videoDuration=video_duration
    ).execute()

    # Lista para armazenar as informações dos vídeos
    videos = []

    # Itera sobre os itens retornados na resposta da busca
    for search_result in search_response.get('items', []):
        # Verifica se o item é um vídeo
        if search_result['id']['kind'] == 'youtube#video':
            video_url = f"https://www.youtube.com/watch?v={search_result['id']['videoId']}"
            
            # Extrai a descrição completa usando yt-dlp
            video_info = get_full_description(video_url)
            
            # Adiciona as informações do vídeo à lista
            videos.append({
                'title': search_result['snippet'].get('title', 'N/A'),                               # Título do vídeo
                'description': video_info.get('description', 'N/A'),                                # Descrição completa do vídeo
                'url': video_url,                                                                   # URL do vídeo
                'publishedAt': search_result['snippet'].get('publishedAt', 'N/A'),                   # Data de publicação
                'channelTitle': search_result['snippet'].get('channelTitle', 'N/A'),                 # Nome do canal
                'tags': search_result['snippet'].get('tags', 'N/A'),                                 # Tags
                'thumbnails': search_result['snippet']['thumbnails']['default']['url'],              # URL da miniatura --> imagens representativas do vídeo
                'license': video_license,                                                            # Licença do vídeo
                'liveBroadcastContent': search_result['snippet'].get('liveBroadcastContent', 'N/A')  # Transmissão ao vivo
            })

    # Retorna a lista de vídeos encontrados
    return videos

def get_full_description(video_url):
    """
    Função para extrair a descrição completa do vídeo usando yt-dlp.

    Parâmetros:
    - video_url (str): URL do vídeo no YouTube.

    Retorna:
    - video_info (dict): Dicionário contendo a descrição completa e outras informações do vídeo.
    """
    with yt_dlp.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        return {
            'description': info_dict.get('description', 'N/A')  # Pega a descrição completa do vídeo
        }

# Parâmetros de busca
query = "machine learning"            # Termo de busca
max_results = 3                      # Número máximo de resultados
video_type = 'video'                  # Tipo de resultado ('video', 'channel', 'playlist')
video_license = 'creativeCommon'      # Licença do vídeo ('any', 'creativeCommon')
video_duration = 'long'               # Duração do vídeo ('any', 'long', 'medium', 'short')

# Executar a busca e obter os resultados
results = youtube_search(query, max_results, video_type, video_license, video_duration)

# Informar a quantidade de vídeos encontrados
print(f"Quantidade de vídeos encontrados: {len(results)}")

# Salvar os links e metadados em um arquivo .txt
with open('video_metadata.txt', 'w', encoding='utf-8') as file:
    # Escreve a quantidade de vídeos no arquivo
    file.write(f"Quantidade de vídeos encontrados: {len(results)}\n")
    file.write("=" * 50 + "\n\n")

    # Itera sobre cada vídeo nos resultados
    for video in results:
        # Escreve os metadados no arquivo
        file.write(f"Título: {video['title']}\n")
        file.write(f"Descrição: {video['description']}\n")  # Descrição completa do vídeo
        file.write(f"URL: {video['url']}\n")
        file.write(f"Publicado em: {video['publishedAt']}\n")
        file.write(f"Canal: {video['channelTitle']}\n")
        file.write(f"Tags: {', '.join(video['tags']) if isinstance(video['tags'], list) else 'N/A'}\n")
        file.write(f"URL da miniatura: {video['thumbnails']}\n")
        file.write(f"Licença: {video['license']}\n")
        file.write(f"Transmissão ao vivo: {video['liveBroadcastContent']}\n")
        file.write("-" * 50 + "\n\n")

# Exibir os resultados no terminal
# for video in results:
#     print(f"Título: {video['title']}")
#     print(f"Descrição: {video['description']}")
#     print(f"URL: {video['url']}")
#     print(f"Publicado em: {video['publishedAt']}")
#     print(f"Canal: {video['channelTitle']}")
#     print(f"Tags: {', '.join(video['tags']) if isinstance(video['tags'], list) else 'N/A'}")
#     print(f"URL da miniatura: {video['thumbnails']}")
#     print(f"Licença: {video['license']}")
#     print(f"Transmissão ao vivo: {video['liveBroadcastContent']}")
#     print("-" * 50)
