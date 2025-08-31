from yt_dlp import YoutubeDL

print("Facebook Video Downloader bằng yt-dlp (100% local)")

while True:
    fb_url = input("\nNhập link video Facebook công khai (hoặc gõ exit để thoát):\n> ").strip()
    if fb_url.lower() in ["exit", "quit"]:
        print("Thoát chương trình.")
        break

    if not fb_url:
        print("❌ Bạn chưa nhập link.")
        continue

    ydl_opts = {
        'format': 'best',              # Tải video chất lượng cao nhất
        'outtmpl': '%(title)s.%(ext)s', # Lưu file với tên video
        'quiet': False
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([fb_url])
        print("✅ Hoàn tất tải video!")
    except Exception as e:
        print(f"❌ Lỗi: {e}")
