from acid.handlers import BaseHandler

class Handler(BaseHandler):

    name = "SpecFdef"
    priority = 0

    def on_init(self):
        self.value = []

    def on_handle(self, msg, *_):
        out = "(s/fdef {} :args {} :ret ...)".format(
            msg['name'], msg['arglists-str']
        ))
        self.nvim.funcs.setreg('"', out)
