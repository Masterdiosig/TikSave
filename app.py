from flask import Flask, render_template, request
from yt_dlp import YoutubeDL
import os

app = Flask(__name__)
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    fb_url = request.form.get("fb_url", "").strip()
    if not fb_url:
        return {"success": False, "message": "Nhập link video Facebook!"}

    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
        'quiet': True
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(fb_url, download=True)
            filename = ydl.prepare_filename(info)
        return {"success": True, "message": f"✅ Hoàn tất tải video: {os.path.basename(filename)}"}
    except Exception as e:
        return {"success": False, "message": f"❌ Lỗi: {str(e)}"}

if __name__ == "__main__":
    app.run(debug=True, port=5000)



