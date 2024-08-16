import time
import random
from functools import wraps

def timer(func):

  @wraps(func)
  def decorated(*args, **kwargs):
    st = time.perf_counter()

    ret = func(*args, **kwargs)

    print('time cost: {} seconds'.format(time.perf_counter() - st))
    return ret
  return decorated


def calls_counter(func):
  counter = 0

  @wraps(func)
  def decorated(*args, **kwargs):
    nonlocal counter
    counter += 1
    return func(*args, **kwargs)
  
  def print_counter():
    print(f"counter: {counter}")

  # 函数的属性也可以是函数
  decorated.print_counter = print_counter
  return decorated

@timer
@calls_counter
def random_sleep():
  '''随机睡眠一会儿'''
  time.sleep(random.random())

# 被包装器包装之后，原函数的属性会丢失

random_sleep()
random_sleep()
random_sleep.print_counter()

print(random_sleep.__name__)
print(random_sleep.__doc__)