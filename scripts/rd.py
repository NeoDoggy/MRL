import random
import time

while True:
  f=open("ball.txt","w")
  f2=open("box.txt","w")
  f.write(f'{"{:.2f}".format(random.uniform(-1, 1))} {"{:.2f}".format(random.uniform(-1, 1))} {"0.1"}')
  f2.write(f'{"{:.2f}".format(random.uniform(-1, 1))} {"{:.2f}".format(random.uniform(-1, 1))} {"0.1"}')
  f.close()
  f2.close()
  time.sleep(0.1)
  