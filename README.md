# 下載 Spotify 播放清單
下載公開的 Spotify 播放清單內的所有歌曲，不需要 Spotify Premium。

## 運作原理
串接 Spotify API 獲取播放清單內的所有歌曲，再以 `<artist> - <track_name>` 的關鍵字形式使用 `yt-dlp` 從 Youtube 取得搜尋結果並下載搜尋結果內的第一個影片。

## 前置作業
### 複製儲存庫
```bash
git clone https://github.com/bruh0422/Spotify-Playlist-Downloader.git
cd Spotify-Playlist-Downloader
```

### 安裝必要檔案
```bash
pip install -r requirements.txt
```
還需要安裝 [FFmpeg](https://ffmpeg.org/)，具體操作步驟請自行 [Google](https://www.google.com/search?q=ffmpeg+install)。

### 取得 Spotify API Key
1. 前往 [Spotify for Developers](https://developer.spotify.com/)，點擊右上方的 "Log in" 登入帳號。
2. 登入後，點擊右上方的下拉式選單，選擇 "[Dashboard](https://developer.spotify.com/dashboard)"。
3. 點擊 "[Create app](https://developer.spotify.com/dashboard/create)"，依序填入 "App name"、"App description"、"Redirect URIs" 並勾選 "I understand and agree with Spotify's Developer Terms of Service and Design Guidelines" 後按下 "Create"。
    > [!TIP]
    > "Redirect URIs" 如果你不知道要填什麼，可以直接填入 "https://google.com/"，這格填了什麼無所謂。
4. 之後網頁會重導向到你的應用頁面，點擊右上方的 "Settings" 進入設定頁面。
5. 在 "Basic Information" 頁面中你會看到你的 "Client ID"，點擊下面的 "View client secret" 顯示你的 Client secret。
    > [!CAUTION]
    > 不要將這兩組資料與他人分享及共用。
6. 將 .env 中的 `spotify_client_id` 與 `spotify_client_secret` 替換為你的 Client ID 與 Client secret。

## 開始使用
```bash
python run.py
```
接下來按照程式指定的步驟操作即可。\
下載下來的曲目會先儲存到 `temp` 資料夾內，程式會將檔案依 `<artist> - <track_name>` 的格式重新命名再移動到 `output` 資料夾中。