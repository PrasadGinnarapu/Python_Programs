def outer_method():

    def inner_method2():
        # In nested method, reference nonlocal variable.
        nonlocal value
        value = 100

    # Set local.
    value = 10
    inner_method2()

    # Local variable reflects nonlocal change.
    print(value)

# Call method.
outer_method()
