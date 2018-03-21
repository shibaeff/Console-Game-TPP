import generation as gen


def stringer(items):
    for item in items:
        print(item.name + " " + type(item).pos_name)

stringer(gen.Pool.gen_pool(4, 5))