import time
import random

def timer(func):

  def decorated(*args, **kwargs):
    st = time.perf_counter()

    ret = func(*args, **kwargs)

    print('time cost: {} seconds'.format(time.perf_counter() - st))
    return ret
  return decorated


@timer
def random_sleep():
  time.sleep(random.random())

# 使用了timer装饰器之后，实际执行的函数为decorated函数
random_sleep()
# 使用装饰器后，函数的名称，文档属性都会变成装饰器内层包装函数decorated的值，
# 会造成原函数的元数据丢失问题，此外，原始函数所拥有的属性也会丢失
print(random_sleep.__name__)
print(random_sleep.__doc__)
