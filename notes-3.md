import the primary module

    it's call primary

Create a range of vars

    color, your favourite color
    sid, your ID

Step 1: call the correct function from the primary module

    hint remember the dir function can help inspect a module
    hint remember help() can print the doc string of a function


        primary.run_step_1()
        # Assert Error (this requires an extra parameter...)

    # user uses help()

        help(primary.run_step_1)
        primary.run_step_1(sid)

    # returns ciper int of the sid
    # Use the result to call the next step

Write a dictionary containing the sid, ciper, colors

    {
        'sid': ...
        'ciper': ...
        'color': ...
    }

_append_ your color to the primary colors, and assign to your dict.

    colors = [color] + primary.colors
    # ['blue', 'red', 'green', 'blue']

    {
        'sid': ...
        'ciper': ...
        'colors': colors
    }

    # It doesn't matter if your name is already a primary color.

Call the step two function 100x, add 1 each time

    ## not good
    for i in range(100):
        primary.step_two(cipher + i)

    ## better
    for i in range(100):
        primary.step_two(cipher += 1)

    # res == cipher + 100
    ## res is stored in primary.step_3


Write a function to accept your number, and convert it to a string

    expected = '#_#_#_#_#_#' for every char.

    def my_func(value):
        return expected

    # Hint: var class can 'inspect' a live object.


now run this function many times, until satified, with the content from primary.step_3.

    # in the background the step_3_unsatified monitors every call of step_3
    # until a secret number...
    while primary.step_3_unsatified:
        my_func(primary.step_3)

write a function of accepts many args which returns a _list_. Items in the list are in `step_4_items`

    ## Because it comes in as tuples, the user will need to convert it.
    def my_cleaner_func(*args):
        return list(args)

Now provide this function to `step_4`, it will use it...

    primary.step_4(my_cleaner_func)
    ## Correct! You can provide a function without executing it first.

    ## When used, it will yield a pretend error the user must solve.
    ## raises Error (Oops. Jay forgot to expand the question.)
    ## You need to _slice_ the last argument from the function.

Edit the function as expected can try again in step 5.

    def my_cleaner_func(*args):
        return list(args[0:-1])

    primary.step_5(my_cleaner_func)
    ## Excellent!


Update the function to perform this check:

    call `primary.step_6()` with each argument given to the func and the index of the argument.
    if the given arg is less than 10, don't call the func
    if greater than 50, multiply by the value in `step_4_result`

        # not good
        def cleaner(*args):
            c = 0
            for arg in args:
                c += 1
                if arg < 10:

                elif arg > 40:
                    arg = arg * primary.step_4_result
                    primary.step_6(arg, i)
                else:
                    primary.step_6(arg, i)

        # good
        def cleaner(*args):
            for i, arg in enumerate(args):
                if arg < 10:
                    continue
                if arg > 40
                    arg = arg * primary.step_4_result
                primary.step_6(arg, i)


Now create a class with a function performing the same. Provide to `step_7`

    class MyClass(object):
        def cleaner(self, *args):
            ...

    primary.step_7(MyClass)
    # the method calls upon the class for testing.


update the init method to accept these dictionary params:

    # using vars from the parent dict.
    sid, color, ciper

    primary.step_7(MyClass)


Ensure those params are stored in the class as the same name.

    # best
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    primary.step_8(MyClass)

Add another method called 'foo' for the following:

    all args are above 100: return true
    arg == 6 or 12: return false
    else return None

        # user will likely update their other cell.
        class MyClass(object):
            ...

            def foo(self, *args):
                ...

        primary.step_9(MyClass)


write a method to _flip_ a boolean.

    # best
    def flip_bool(self, value):
        return not bool(value)

    primary.step_10(MyClass)

 Assign an instance of this class to your step 1.5 dictionary
    ## Merge that dict with this one, and provide the result to the step_9

        # provide a new dict the user must merge into their dict

        result = {
            ...
        }

    primary.step_9(result)
    ## Correct. To Proceed, unpack this result rather than supplying one dict

    res = primary.step_9(**result)
    ## returns prepared step9

_try_ to Run step 10

    ## raises ValueError, KeyError
    ## stores step 10

    primary.step_10()
    ## error
    primary.step_10(content)
    ## error
    primary.step_10(content, other=30)


write a method that accepts a function, of which raises an assertion when the value is X

    ## This test will push a user to use the f'' string to format their assertion.

    # expected
    def myfunc(self, value):
        assert value is not X, 'Value is not X'

    primary.step_10(my_func)
    ## Great. The function asserts! However the message should
    ## 'Value is not Xv',

    def myfunc(self, value):
        assert value is not X, f'Value is not {X}'
    ## Correct

Write the text value to a file.

    ## This may not be able to occur because jupyter remote.

    with path.open('w') as stream:
        stream.write(content)

    ## better
    pathlib.Path().write_text(content)

submit this to the flask endpoint.

    res = requests.post({...})
    ...
    data == content


write a method to assert the result of the post. It should match value from `step_10_result`

    requests.post().json() == primary.step_10_result

    ## Asserting a complex type
    {
        sid: 11
        color: [red]
        ciper: 100
    }

    ### The local colors is a tuple, the remote was a list.

---

To finalise this. The end dict should be a uniquely generated object, including a unique (and correct) ciper, inside the jupyter file.
The content should be clear and tidy. Points are awarded for:

+ Accuracy: It must work
+ Tidyness: Readability is key
+ Methodology: Using the best bits of python in a pythonic manner


