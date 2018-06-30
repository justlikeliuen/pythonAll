# swap
a = 1
b = 2
print(a,b)
a,b = b,a
print(a,b)

# with
# with open(filepath,'r') as f:
    # do_some_thing(f)

"""
%s
"""
print("hello %s" % ('liuen'))
print("hello %(name)s,%(age)d" % {'name':'liuen','age':1})
b
value = {'name':'liuen','age':1}
print("hello %(name)s,%(age)d" % value)

# recommend
print('{great} from {language}'.format(great = 'hello world',language='python'))

# 19 when use 'from ... import ...' ,be cautious. it will contaminate the name space

"""
filter. filter is an inner method.faster than common for
"""
name_list = [1,2,3,4,6]
result_list = filter(lambda x:x > 2,name_list)
print(list(result_list))

import functools
product = functools.reduce(lambda x,y:x * y,[1,2,3,4,5,6])
print(product)

"""
set . use set to print duplicate value in the list
"""
sample_list = [1,2,3,1,2,7,5,4,8,5]
result_list = set([x for x in sample_list if sample_list.count(x)> 1])
print(result_list)
first_list = [1,2,3,9]
print(set(sample_list).difference(set(first_list)))
print(set(sample_list).intersection(set(first_list)))

"""
function
"""
def hi(name="liuen"):
    return "hi " + name
print(hi())
greet = hi()
print(greet)
greet = hi
print(greet())
del hi
#print(hi())
print(greet())

"""
decorator
"""
from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)  # use wraps to keep the function __name__ value
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

def a_function_requiring_decoration():
    print("a I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration()
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()
print(a_function_requiring_decoration.__name__)

@a_new_decorator
def b_function_requiring_decoration():
    print("b   I am the function which needs some decoration to remove my foul smell")

b_function_requiring_decoration()

"""

"""
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fibon(10):
    print(x)

def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)          # receive send()
        if pattern in line:
            print(line)

search = grep('coroutine')
next(search)
#output: Searching for coroutine
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutine instead!")
search.close()
