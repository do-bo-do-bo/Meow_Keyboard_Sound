# Meow_Keyboard_Sound
meow meow meow meow

키보드를 입력할 때마다 고양이 "야옹" 소리가 재생되는 프로그램입니다.

## 기능

- 키보드 입력 시 "야옹" 소리 재생
- ESC 키를 눌러 프로그램 종료

## 사용 방법

1. [Releases](https://github.com/do-bo-do-bo/Meow_Keyboard_Sound/releases) 페이지에서 최신 버전의 `Meow.exe` 파일을 다운로드합니다.
2. 다운로드한 `.exe` 파일을 더블 클릭하여 실행합니다.
3. 키보드를 입력할 때마다 "야옹" 소리가 재생됩니다.
4. 프로그램을 종료하려면 `ESC` 키를 누르세요.


## 요구 사항

- Windows 운영체제
- Python 3.9 이상 (소스 코드를 직접 실행하는 경우)


## ⚠️ 주의 사항
**__백신에서 이 프로그램을 바이러스 (Trojan:Win32/Wacatac.B!ml)로 인식하는 문제가 있습니다**__

이는 키보드 입력을 감지하는 기능 자체가 바이러스로 인식되어 생기는 문제로, exe 파일을 실행하기 위해서는 백신에서 예외처리(다운로드 허용)이 필요합니다.
   - **Chrome에서 다운로드 차단 시**:
     - 다운로드가 차단되었다는 경고 메시지가 나타나면, 다운로드 창에서 **"다운로드"** 버튼을 클릭하고, **"위험을 무시하고 파일 열기(Open anyway)"**를 선택하세요.
   - **바이러스 백신 경고 시**:
     - 바이러스 백신 소프트웨어에서 경고가 발생하면, 해당 프로그램을 **예외 목록(Whitelist)**에 추가하세요.
     - 구체적인 방법은 사용하는 바이러스 백신 소프트웨어의 도움말을 참고하세요.
     
python을 다뤄본 적 있다면, 공개된 소스코드를 활용하여 직접 실행해보시는 것을 권장합니다.


## 🛠️ Python 패키지 설치

이 프로젝트의 모든 의존성을 설치하려면 `requirements.txt` 파일을 사용하세요. 아래 단계를 따라 환경을 설정하고 의존성을 설치할 수 있습니다.

```bash
pip install -r requirements.txt
```
참고: requirements.txt 파일은 다음과 같이 구성되어 있습니다.

```plaintext
pynput==1.7.6
playsound==1.2.2
```


## 라이선스

[MIT License](LICENSE)
