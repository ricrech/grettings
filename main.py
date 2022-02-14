from greets import greetings
from translate import Translator

tranlator = Translator(to_lang='pt')


for g in greetings:
    print(tranlator.translate(g).title())

