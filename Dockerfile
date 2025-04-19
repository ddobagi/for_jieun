FROM python:3.10-slim

# 크롬과 드라이버, 필요한 리눅스 패키지 설치
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    wget \
    curl \
    unzip \
    libnss3 \
    libxss1 \
    libappindicator1 \
    libindicator7 \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libx11-xcb1 \
    xdg-utils

# 크롬 위치 알려주기
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER=/usr/bin/chromedriver

# 파이썬 패키지 설치
RUN pip install selenium

# 작업 디렉토리 설정
WORKDIR /app

# 현재 디렉토리 전체 복사
COPY . .

# Express 서버 실행
CMD ["node", "index.js"]
