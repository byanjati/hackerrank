def walking_robot(instruction):
    i = 0
    total_potential_crash_right = 0
    is_crashed = False
    total_crash_right = 0
    total_crash_left = 0

    if (len(instruction) > 1):
        while i < len(instruction):
            if (instruction[i] == 'r'):
                total_potential_crash_right += 1
                is_crashed = False

            if (instruction[i] == 'd'):
                total_crash_right += total_potential_crash_right
                total_potential_crash_right = 0
                is_crashed = True

            if (instruction[i] == 'l'):
                if is_crashed:
                    total_crash_left += 1

                if (total_potential_crash_right > 1):
                    total_crash_right += total_potential_crash_right + 1
                    total_potential_crash_right = 0
                    is_crashed = True

                if (total_potential_crash_right > 0):
                    total_crash_right += 2
                    total_potential_crash_right = 0
                    is_crashed = True

            i += 1

        return total_crash_right + total_crash_left
    else:
        return 0

    return total_crash

def assert_walking_robot(instruction, number_of_crash):
    actual = walking_robot(instruction)
    assert actual == number_of_crash

def test_hackerrank():
    instruction = ['r', 'lrrl', 'rrrll', 'rrdlldrr', 'rrrdllrllrrl']
    expected = [0, 3, 5, 4, 11]
    for inst, exp in zip(instruction, expected):
        assert_walking_robot(inst, exp)

def test_combination_of_right_left_and_stayed_robots():
    instruction = ['rdl', 'rrdll', 'rldrl']
    expected = [2, 4]
    for inst, exp in zip(instruction, expected):
        assert_walking_robot(inst, exp)

def test_right_and_left_robot_are_crashed():
    instruction = ['rl', 'rrl', 'rrrl', 'rrrrl', 'rll', 'rlrl', 'rllrll', 'lrlrlr']
    expected = [2, 3, 4, 5, 3, 4, 6, 4]
    for inst, exp in zip(instruction, expected):
        assert_walking_robot(inst, exp)

def test_combination_right_and_left_but_crashed_with_stayed_robot():
    instruction = ['rrdll', 'rrrdlll', 'rrdrdldll']
    expected = [4, 6, 6]
    for inst, exp in zip(instruction, expected):
        assert_walking_robot(inst, exp)

def test_when_robot_going_left_and_crash_the_stayed_robot():
    instruction = ['ld', 'lld', 'dl', 'dll', 'dlll']
    expected = [0, 0, 1, 2, 3]
    for inst, exp in zip(instruction, expected):
        assert_walking_robot(inst, exp)

def test_when_robot_is_crashing_when_there_is_random_robot_stay_on_position():
    instruction = ['rrdrr', 'rrrdrrr', 'rrrrdrrrr', 'drrrr', 'rrdrdrdr']
    expected = [2, 3, 4, 0, 4]
    for inst, exp in zip(instruction, expected):
        assert_walking_robot(inst, exp)

def test_when_robot_is_crashing_with_stopped_robot_but_there_is_a_same_direction_robot_behind():
    instruction = ['rrd', 'rrrd', 'rrrrd']
    expected = [2, 3, 4]
    for inst, exp in zip(instruction, expected):
        assert_walking_robot(inst, exp)

def test_when_robot_is_crashing_with_stopped_robot():
    instruction = 'rd'
    assert_walking_robot(instruction, 1)

def test_when_robot_is_not_crashing():
    instruction = ['ld', 'dr', 'lr', 'll', 'rr']
    for inst in instruction:
        assert_walking_robot(inst, 0)

def test_when_there_is_just_one_robot():
    instruction = 'r'
    assert_walking_robot(instruction, 0)

def test_when_robot_walking_same_direction():
    instruction = 'rr'
    assert_walking_robot(instruction, 0)

def test_when_robot_walking_same_direction_to_left():
    instruction = 'll'
    assert_walking_robot(instruction, 0)

def test_when_robot_walking_is_stay_on_the_position():
    instruction = 'dd'
    assert_walking_robot(instruction, 0)
