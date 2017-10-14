def parse_input_store(command):
    commands = command.split(' ')
    command_type = commands[0]
    day = commands[1]
    products = commands[2].split('.')
    product_id = products[0]
    category_id = products[1] if len(products) == 2 else None
    country = commands[3].split('.')
    state_id = country[0]
    region_id = country[1] if len(country) == 2 else None

    return command_type, day, product_id, category_id, state_id, region_id

def parse_input_query(command):
    commands = command.split(' ')
    command_type = commands[0]
    days = commands[1].split('.')
    day_start = days[0]
    day_end = days[1] if len(days) == 2 else days[0]
    products = commands[2].split('.')
    product_id = products[0]
    category_id = products[1] if len(products) == 2 else None
    country = commands[3].split('.')
    state_id = country[0]
    region_id = country[1] if len(country) == 2 else None

    return command_type, day_start, day_end, product_id, category_id, state_id, region_id

def read_command(command):
    commands = command.split('\n')
    selling = []
    total_selling = 0

    for command in commands:
        command_type, day, product_id, category_id, state_id, region_id = parse_input_store(command)
        if command_type ==  "S":
            sell = {
                "day": day,
                "product_id": product_id,
                "category_id": category_id,
                "state_id": state_id,
                "region_id": region_id
            }
            selling.append(sell)
        elif command_type == "Q":
            command_type, day_start, day_end, product_id, category_id, state_id, region_id = parse_input_query(command)
            result = [item for item in selling if item['day'] >= day_start and item['day'] <= day_end]
            if int(product_id) > -1:
                result = [item for item in result if item['product_id'] == product_id]

            if int(state_id) > -1:
                result = [item for item in result if item['state_id'] == state_id]

            if category_id:
                result = [item for item in result if item['category_id'] == category_id]

            if region_id:
                result = [item for item in result if item['region_id'] == region_id]

            query_count = len(result)
            total_selling += query_count

    return total_selling

def test_query_found_selling_product_when_given_only_start_date():
    commands = "S 1 3.4 5.6\nS 2 3.4 5.6\nQ 1 3.4 5.6"
    actual_number_selling = read_command(commands)
    expected_number_selling = 1
    assert expected_number_selling == actual_number_selling

def test_query_found_selling_product_when_product_id_is_negative():
    commands = "S 1 3.4 5.6\nS 2 4.4 5.6\nQ 1.2 -1 5.6"
    actual_number_selling = read_command(commands)
    expected_number_selling = 2
    assert expected_number_selling == actual_number_selling

def test_query_found_selling_product_when_state_id_is_negative():
    commands = "S 1 3.4 5.6\nS 2 4.4 5.6\nS 2 4.4 6.6\nQ 1.2 -1 -1"
    actual_number_selling = read_command(commands)
    expected_number_selling = 3
    assert expected_number_selling == actual_number_selling

def test_query_found_selling_product_when_given_only_product_id():
    commands = "S 1 3.4 5.6\nS 2 3.5 5.6\nQ 1.2 3 5.6"
    actual_number_selling = read_command(commands)
    expected_number_selling = 2
    assert expected_number_selling == actual_number_selling

def test_query_found_selling_product_when_given_only_state_id():
    commands = "S 1 3.4 5.6\nS 2 3.4 5.6\nQ 1.2 3.4 5"
    actual_number_selling = read_command(commands)
    expected_number_selling = 2
    assert expected_number_selling == actual_number_selling

def test_query_found_selling_product_in_certain_dates():
    commands = "S 1 3.4 5.6\nQ 1.2 3.4 5.6"
    actual_number_selling = read_command(commands)
    expected_number_selling = 1
    assert expected_number_selling == actual_number_selling

def test_sample_1():
    commands = "S 1 1 2\nS 2 1.1 2\nS 2 2.3 1\nS 1 2.2 1\nQ 1 1 2"
    actual_number_selling = read_command(commands)
    expected_number_selling = 1
    assert expected_number_selling == actual_number_selling

def test_sample_2():
    commands = "S 1 1 2\nS 2 1.1 2\nS 2 2.3 1\nS 1 2.2 1\nQ 1.2 -1 -1"
    actual_number_selling = read_command(commands)
    expected_number_selling = 4
    assert expected_number_selling == actual_number_selling


def test_parse_input_query():
    command = "Q 1.2 3.4 5.6"
    command_type, d_start, d_end, p_id, c_id, s_id, r_id = parse_input_query(command)
    assert "Q" == command_type
    assert "1" == d_start
    assert "2" == d_end
    assert "3" == p_id
    assert "4" == c_id
    assert "5" == s_id
    assert "6" == r_id

def test_parse_input_query_when_given_no_end_day():
    command = "Q 1 3.4 5.6"
    command_type, day_start, day_end, p_id, c_id, s_id, r_id = parse_input_query(command)
    assert "Q" == command_type
    assert "1" == day_start
    assert "1" == day_end
    assert "3" == p_id
    assert "4" == c_id
    assert "5" == s_id
    assert "6" == r_id

def test_parse_input_selling():
    # store_format = "S d p_id[.c_id] s_id[.r_id]
    command = "S 1 3.4 5.6"
    command_type, d, p_id, c_id, s_id, r_id = parse_input_store(command)
    assert "S" == command_type
    assert "1" == d
    assert "3" == p_id
    assert "4" == c_id
    assert "5" == s_id
    assert "6" == r_id
