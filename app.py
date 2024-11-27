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
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return f"<h1>다운로드 완료!</h1><a href='/'>다시 다운로드</a>"

if __name__ == "__main__":
    app.run(debug=True)
