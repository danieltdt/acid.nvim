from acid.handlers import SingletonHandler
import logging


class Handler(SingletonHandler):

    name = "Log"
    priority = 0
    finalizer = lambda *_: False

    def on_init(self):
        self.logger = logging.getLogger(__name__)
        fh = logging.FileHandler('/tmp/acid-log-handler.log')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(message)s'
        )
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.setLevel(logging.DEBUG)

    def on_handle(self, msg, *_):
        if not 'state' in msg.get('status', []):
            self.logger.info(msg)
