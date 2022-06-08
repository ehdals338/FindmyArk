# Discord bot을 이용한 아이템 레벨 확인

## 시스템 환경
Python 3.9.6   

## 사전 설치
#### cmd 환경에서 아래 명령어 입력
```   
pip install discord
pip install asyncio
pip install websockets
pip install aiohttp
pip install discord asyncio websockets aiohttp
pip install requests beautifulsoup4
```   

## 사용법
#### cmd 환경에서 아래 명령어 입력
```   
.\discord_bot.py
```   

그 후 생성된 18자리 봇 클라이언트 아이디를 복사하여 아래와 같이 web-discord를 실행한다.   
https://discordapp.com/oauth2/authorize?client_id={봇클라이언트아이디}&scope=bot   
ex) https://discordapp.com/oauth2/authorize?client_id=123456789123456789&scope=bot   
   
서버를 선택한 후 봇이 추가된 것을 확인할 수 있다.   
   
명령어는 다음과 같다.   
!아이디   
ex) !으아아아악   
   
봇의 답변은 아래와 같이 출력되면 정상이다.   
@사용자아이디: "으아아아악" Lv.9999.99