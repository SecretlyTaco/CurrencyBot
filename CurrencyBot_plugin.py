# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
import money

@irc3.plugin
class Plugin:

    def __init__(self, bot):
        self.bot = bot

    @command(permission='view')
    def bal(self, mask, target, args):
        """Check balance
        
           %%bal [person]
        """
        if '[person]' in args.keys():
            yield("%s: %s" % (mask.nick, money.get_balance(args['[person]'])))
        else:
            yield("%s: %s" % (mask.nick, money.get_balance(mask.nick)))

    @command(permission='view')
    def pay(self, mask, target, args):
        """Pay money to another person

           %%pay <person> <amount>
        """
        if money.pay(mask.nick, args['<person>'], float(args['<amount>'])):
            yield "Complete"
        else:
            yield "Error happened"
