from flask import Flask, request  # Flask와 요청(request) 모듈 가져오기
import yt_dlp  # YouTube 동영상 다운로드 라이브러리

# Flask 앱 생성
app = Flask(__name__)

# 홈 페이지 라우트
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>유튜브 동영상 다운로드</title>
    </head>
    <body>
        <h1>유튜브 동영상 다운로드</h1>
        <form method="POST" action="/download">
            <label>유튜브 URL 입력:</label>
            <input type="text" name="url" style="width: 300px;" placeholder="https://www.youtube.com/watch?v=...">
            <button type="submit">다운로드</button>
        </form>
    </body>
    </html>
    '''

# 동영상 다운로드 라우트
@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url', '').strip()  # 입력받은 URL 가져오기
    if not url:  # URL이 비어 있는지 확인
        return "<h1>오류: 유효한 URL을 입력하세요.</h1>", 400

    # yt-dlp 설정
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  # 저장 파일 이름 형식
        'format': 'bestvideo+bestaudio/best',  # 최고 화질 + 오디오 선택
        'cookiefile': 'youtube_cookies.txt',  # 쿠키 파일 경로
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # 동영상 다운로드 실행
        return "<h1>다운로드 완료!</h1><a href='/'>다시 다운로드</a>"
    except Exception as e:
        return f"<h1>오류 발생: {e}</h1>", 500

# Waitress 서버를 사용하여 앱 실행
if __name__ == "__main__":
    from waitress import serve  # Waitress 가져오기
    # Waitress로 Flask 앱 실행
    serve(app, host="0.0.0.0", port=5000)
