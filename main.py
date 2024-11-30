import threading
from pynput import keyboard
from playsound import playsound
import os
import sys

def resource_path(relative_path):
    """
    PyInstaller로 패키징된 경우와 개발 중인 경우 모두에서
    리소스 파일의 절대 경로를 반환합니다.
    """
    try:
        # PyInstaller로 패키징된 경우
        base_path = sys._MEIPASS
    except Exception:
        # 개발 중인 경우
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

# 소리 파일의 경로를 설정합니다.
SOUND_FILE = resource_path('meow.wav')

def play_meow():
    """'야옹' 소리를 재생하는 함수입니다."""
    try:
        playsound(SOUND_FILE)
    except Exception as e:
        print(f"소리 재생 중 오류 발생: {e}")

def on_press(key):
    """
    키가 눌릴 때마다 '야옹' 소리를 재생합니다.
    만약 ESC 키가 눌리면 리스너를 종료하고 프로그램을 종료합니다.
    """
    if key == keyboard.Key.esc:
        print("ESC 키가 눌렸습니다. 프로그램을 종료합니다.")
        # 리스너를 중지하여 프로그램을 종료합니다.
        return False
    # 'ESC' 키가 아닐 경우 소리를 재생합니다.
    threading.Thread(target=play_meow, daemon=True).start()

def main():
    """키보드 리스너를 시작하는 메인 함수입니다."""
    print("키보드를 입력하면 '야옹' 소리가 재생됩니다.")
    print("프로그램을 종료하려면 ESC 키를 누르세요.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
