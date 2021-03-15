# def highlight(x):
#     print("This shoud be highlighted:",x)
# highlight(4)

import random
def outerfn(fn):
    oper=["@","#","$","%","^"]
    s=random.choice(oper)
    def inner(y):
        print(s*30)
        fn(y)
        print(s*30)
    return inner

# fn=outerfn(highlight)
# print(fn)
# print(fn(5))

@outerfn
def highlight1(x):
    print("This shoud be highlighted:",x)

highlight1(15)