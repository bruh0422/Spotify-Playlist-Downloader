import yt_dlp
import requests
import os

while True:
    spotify_client_id = input('輸入 Spotify Client ID: ')
    spotify_client_secret = input('輸入 Spotify Client secret: ')

    print('驗證及取得 Access Token...')

    response = requests.post(
        url='https://accounts.spotify.com/api/token',
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data={
            'grant_type': 'client_credentials',
            'client_id': spotify_client_id,
            'client_secret': spotify_client_secret
        }
    )

    if response.status_code == 200:
        spotify_access_token = response.json()['access_token']
        print('驗證成功！')
        print('------------------------------')
        break
    else:
        print('驗證失敗，請再試一次。')

while True:
    playlist_url = input('輸入 Spotify 播放清單網址: ')
    playlist_id = playlist_url.split('/')[4].split('?')[0]

    response = requests.get(
        url=f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks',
        headers={
            'Authorization': f'Bearer {spotify_access_token}'
        }
    )

    if response.status_code == 200:
        print(response.json())
        playlist = [f"{i['track']['artists'][0]['name']} - {i['track']['name']}" for i in response.json()['items']]
        print(f'成功取得下列播放清單歌曲 (共 {len(playlist)} 項)：')
        print('\n'.join(playlist))
        print('------------------------------')
        break
    else:
        print('無法取得播放清單。')

print('開始下載...')

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'temp/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav'
    }]
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    index = 1
    for song in playlist:
        print(f'\n正在下載 {song} ({index} / {len(playlist)})')
        ydl.extract_info(f"ytsearch:{song}", download=True)['entries'][0]
        os.rename(f"temp/{os.listdir('temp')[0]}", f'output/{song}.wav')
        index += 1

print('完成')