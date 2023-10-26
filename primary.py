from time import sleep

print('Excellent. Find the _first function_.')

COLORS = ['red', 'green', 'blue']

def first_function():
    """The _first function_ returns an instance of the "primary" game,
    Keep hold of this reference:

    Usage:

        game = first_function()
    """
    ## Assert color and sid exist in locals or globals
    ## or last frame.
    return Primary()


class Primary(object):
    """The Primary class maintains a session of the game.
    It consists of _methods_ (functions of a class), attributes (vars)
    and other useful bits.

    Step 1: create an instance of primary:

        from primary import Primary
        game = Primary()
        help(game)
        # this message.

    Step 2: run step one. Attempt to discover this method using python.
            (some great ones exist within the `builtins` module)
    """
    COLORS = COLORS
    step_four_unsatified = True
    _step_four_inner_count = 0
    step_four_answer = 42

    def run_step_1(self, sid=None):
        if sid is None:
            print('Great! Step one achieved. To proceed, '
                  'rerun this function, providing your SID')
            return

        self.cipher = hash(sid)
        return self.cipher

    def check_human(self, human):
        assert 'sid' in human
        assert human['cipher'] == self.cipher
        assert len(human['colors']) == len(COLORS) + 1
        self._human = human
        return True

    def step_two(self, v):
        result = self.cipher + v
        self.step_three_value = result
        return result

    def step_three(self, convert_func):
        expected = '_'.join(str(self.step_three_value))
        value = self.step_three_value
        result = convert_func(value)
        assert expected == result
        self.step_three_result = result
        self._step_four_inner_count = 0
        self.step_four_unsatified = True
        return self.step_three_result

    def step_four(self, value):
        if value != self.step_three_result:
            # hint: the vars and dir functions may help.
            raise Exception('Step Four requires the value from step three.')

        # sleep(.1)
        self._step_four_inner_count += 1
        done = self._step_four_inner_count == len(str(self.cipher))
        self.step_four_unsatified = not done
        if done:
            print('Okay.. Okay - Try this number.')
            self.step_four_answer = int(self.step_three_value / self._step_four_inner_count)
            return self.step_four_answer
        else:
            print("Thinking about it. Try again later.")

    def step_5(self, func):
        items = str(self.step_four_answer)
        res = func(*items)
        assert type(res) == list

        if len(res) != len(items) - 1:
            # raise exception.
            print('Whoops. Forgot to mention, please remove the last item')
            return
        print('Great!')
        self._step_five_results = int(self.step_four_answer / int(''.join(res)))
        return self._step_five_results

    def step_6(self, func):
        items = str(self.step_four_answer)
        res = func(*items)
        print('Great!', res)
        self.step_6_func_name = func.__name__
        self.step_6_results = res

        return sum(res)


    def step_7(self, class_):
        inst = class_()
        items = str(self.step_four_answer)
        res = getattr(inst, self.step_6_func_name)(*items)
        assert res == self.step_6_results
        self.step_7_results = res
        return res

    def step_8(self, value):
        assert value == sum(self.step_7_results)
        self.step_8_results = { 'step_8_result': value}
        return tuple(x + value for x in self.step_7_results)

    def step_9(self, class_):
        h = self._human.copy()
        kw = {}
        for k in ['sid', 'colors', 'cipher']:
            if k in h:
                kw[k] = h[k]
        inst = class_(**kw)
        inst.session = self
        inst.step_10 = self.step_10

        assert hasattr(inst, 'sid')
        assert hasattr(inst, 'cipher')
        assert hasattr(inst, 'colors')

        return inst

    def step_10(self):
        return dict(
                step_three_value=self.step_three_value,
                step_three_result=self.step_three_result,
                step_four_answer=self.step_four_answer,
                step_five_results=self._step_five_results,
                step_6_func_name=self.step_6_func_name,
                step_6_result=self.step_6_results,
                step_7_results=self.step_7_results,
                step_8_result=self.step_8_results,
            )