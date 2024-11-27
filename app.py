from flask import Flask, request, render_template
import yt_dlp

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>유튜브 동영상 다운로드</h1>
    <form method="POST" action="/download">
        <label>유튜브 URL 입력:</label>
        <input type="text" name="url" style="width: 300px;">
        <button type="submit">다운로드</button>
    </form>
    '''

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',
    'format': 'bestvideo+bestaudio/best',
    'cookiefile': 'C:/Users/MyName/Downloads/youtube.com_cookies.txt',  # 쿠키 파일 경로
}


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return f"<h1>다운로드 완료!</h1><a href='/'>다시 다운로드</a>"

import os  # 환경 변수를 사용하기 위한 모듈

if __name__ == "__main__":
    # Render가 제공하는 포트 번호를 사용
    port = int(os.environ.get("PORT", 5000))
    # Flask 앱 실행
    app.run(host="0.0.0.0", port=port)
