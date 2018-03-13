import charpool as cp
test_pool = cp.Pool()
print(*[str(item) for item in test_pool.get_pool_list()], sep="\n")
