from lib import wait

ints = range(9*1000*1000)
del ints
wait('Nine million ints freed')
