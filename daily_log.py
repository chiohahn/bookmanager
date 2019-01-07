from logging import handlers
import logging

#log settings
carLogFormatter = logging.Formatter('%(asctime)s,%(message)s')

#handler settings
carLogHandler = handlers.TimedRotatingFileHandler(filename='car.log', when='midnight', interval=1, encoding='utf-8')
carLogHandler.setFormatter(carLogFormatter)
carLogHandler.suffix = "%Y%m%d"

#logger set
carLogger = logging.getLogger()
carLogger.setLevel(logging.INFO)
carLogger.addHandler(carLogHandler)

#use logger
carLogger.info("car is coming")

'''
1) logging 과 logging의 handler를 import
- __init__.py 를 쓰지않으면 이렇게 하위 모듈 (= logging.handler) 를 별도로 가져와야 하는 경우도 있다.


2) logging.Formatter
- 어떤 형식으로 로그가 생성될지를 정한다
→ 여기서는 로그 생성시간(ms 단위까지) + "," + 메시지로 carLogFormatter 설정
- %(asctimes)s 는 로그가 기록되는 시간
- %(message)s 는 입력한 로그가 된다.


3) handler.TimedRotatingFileHandler
- 링크 참조: https://docs.python.org/3/library/logging.handlers.html#timedrotatingfilehandler
- 새로운 파일을 만드는 기준
- 저장할 파일명은 car.log
- when='midnight'의 경우 매일밤 자정에 새로운 파일이 만들어진다.
- 이때 만들어지는 형식은 suffix에 따라 설정된다.
→ 예를 들면 여기서는 carLogHandler.suffix = "%Y%m%d" 이므로 car.log.20180504

4) 실제 사용할 logger를 생성하고 설정
- carLogger 를 만들고
- 출력레벨을 INFO 이상으로 설정하고
- handler를 추가

5) 실제 사용
- carLogger.info("car is coming") 라고 사용하면
- 2018-05-04 08:52:11, 599,car is coming 이라고 car.log 라는 파일에 저장이 된다.
→ 밤 12시가 지나면 car.log.20180504 와 같은 이름으로 다른 파일이 생성됨
'''