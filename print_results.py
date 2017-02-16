from pickle import load
saved = open('out', 'rb')
hosts = load(saved)
print hosts['http://mantaops.com/']

