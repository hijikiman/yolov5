
# defaults = {
#     foo: 234,
#     wkwk: 2929,
#     bar: 789
# }

def hogehoge(foo=234, wkwk=2929, bar=789):
    # def hogehoge(**kwargs=defaults):
    import pdb; pdb.set_trace()


if __name__ == '__main__':
    import argparse
    args = argparse.Namespace()
    args.foo = "sakana"
    args.bar = "kinoko"
    hogehoge(**vars(args))
    # hogehoge()
