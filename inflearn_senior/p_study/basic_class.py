def args_add(*args):
    for _ in len(args):
        args += args
    return args

print(args_add(10, 20, 30))
