from acid.commands import BaseCommand
from acid.nvim import path_to_ns
from acid.nvim.log import warning


class Command(BaseCommand):

    name = 'Require'
    priority = 0
    nargs='?'
    handlers = {'Ignore': '', 'DoAutocmd': 'AcidRequired'}
    op = "eval"
    mapping = 'car'
    shorthand_mapping = 'caR'
    shorthand = 'normal! \\"syi]'

    def prepare_payload(self, *args):
        if len(args) == 0:
            ns = path_to_ns(self.nvim)
            if ns is None:
                warning(
                    self.nvim,
                    "Unable to require: couldn't find namespace from path."
                )
                return None
        else:
            ns = " ".join(args)

        return {"code": "(require '[{}] :reload)".format(ns)}

