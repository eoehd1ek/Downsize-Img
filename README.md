# Downsize-Img
이미지 용량 줄이는 프로그램
앨범 커버에 넣을만한 이미지가 용량이 커서 줄이려고 만든 프로그램


# 사용법
Downsize-Img.exe에 이미지 끌어 넣기.
원본은 삭제되지 않으며, 결과 파일이 원본 파일 위치의 "원본이름_pressed.jpg"으로 저장됨.


# 목표 해상도 수정법
1. 이곳만 수정 이라는 주석 부분 수정
2. 가상환경 실행
```shell
call .venv/Scripts/activate
```
3. 필요 라이브러리 설치
```shell
pip install -r requirements.txt
```
4. pyinstaller로 exe 빌드
```shell
pyinstaller -F -n output.exe main.py
```