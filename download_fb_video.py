from snapsave_downloader import SnapSave

print("SnapSave Facebook Video Downloader (local, 100% offline)")

while True:
    fb_url = input("\nNhập link video Facebook công khai (hoặc gõ exit để thoát):\n> ").strip()
    if fb_url.lower() in ["exit", "quit"]:
        print("Thoát chương trình.")
        break

    if not fb_url:
        print("❌ Bạn chưa nhập link.")
        continue

    print("⏳ Đang xử lý...")
    download_url = SnapSave(fb_url)

    if download_url:
        print(f"✅ Link tải trực tiếp:\n{download_url}")
    else:
        print("❌ Không tìm thấy video hoặc video private / link sai.")
