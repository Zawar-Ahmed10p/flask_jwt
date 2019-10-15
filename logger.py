import logging

from datetime import datetime


logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s',level=50)

log=logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

#logging.warning("dsadasd")

#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
#logging.warning('This will get logged to a file')


class Print_log:


    def write(self, *args, **kwargs):
        now=datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        argu=dt_string+" "+str(*args)
        self.out1.write(argu, **kwargs)
        self.out2.write(*args, **kwargs)

    def __init__(self, out1, out2):

        self.out1 = out1
        self.out2 = out2

    def flush(self):

        pass

