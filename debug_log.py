import logging

# 콘솔 디버깅
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# 파일 디버깅
logging.basicConfig(filename='myDebuglogging.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


logging.debug('Start of programe')