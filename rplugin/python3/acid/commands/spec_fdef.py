from acid.commands import BaseCommand
from acid.nvim import path_to_ns


class Command(BaseCommand):

    name = 'SpecFdef'
    priority = 0
    nargs = 1
    handlers = ['SpecFdef']
    op = "info"
    shorthand_mapping = 'csfd'
    shorthand="call setreg('s', expand('<cword>'))"

    def prepare_payload(self, data):
        return {"symbol": data, "ns": path_to_ns(self.nvim)}


