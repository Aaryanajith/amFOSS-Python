with open('madibs.txt', 'w') as mdlib :
    mdlib.write('The ADJECTIVE panda walked to the NOUN and then VERB. \nA nearby NOUN was unaffected by these events.')
    mdlib.close()

adj = input("Enter adjective: ")
noun = input("Enter noun: ")
verb = input("Enter verb: ")
adverb=input("Enter adverb: ")

with open('madibs.txt', 'r') as mdlib :
    mdlibs = mdlib.read()
    mdlib.close()
with open('madibs.txt', 'w') as mdlib_f :
    mdlibs = mdlibs.replace('ADJECTIVE' , adj)
    mdlibs = mdlibs.replace('NOUN' , noun)
    mdlibs = mdlibs.replace('VERB' , verb)
    mdlibs=mdlibs.replace('ADVERB',adverb)
    mdlib_f.write(mdlibs)
    mdlib_f.close()
