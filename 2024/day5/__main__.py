import requests

def format(puzzle):
    queue, manual = puzzle.strip().split('\n\n')
    queue = queue.split('\n')
    manual = manual.split('\n')
    
    rules = [0] * len(queue)
    updates = [0] * len(manual)

    for i in range(len(queue)):
        a, b = queue[i].split('|')
        rules[i] = (int(a),int(b))

    for i in range(len(manual)):
        update = [int(v) for v in manual[i].split(',')]
        updates[i] = update

    return (rules,updates)

def validate_update(rules,update):
    for i in range(len(update)):
        if update[i] in rules:
            for k in range(0,i):
                if update[k] in rules[update[i]]:
                    return False
    return True




def part1(rules,updates):
    rules_dict = {}
    for rule in rules:
        if rule[0] not in rules_dict:
            rules_dict[rule[0]] = [rule[1]]
        else:
            rules_dict[rule[0]].append(rule[1])

    print(f'rules: {rules_dict}')

    total = 0
    
    for update in updates:
        if validate_update(rules_dict,update): 
            total += update[len(update) // 2]
        print(f'update: {update} valid: {validate_update(rules_dict,update)}')

    return total



if __name__ == '__main__':
    test_file = open('test1.txt','r')
    test_input = test_file.read()
    test_file.close()

    input_file = open('input1.txt','r')
    input_string = input_file.read()
    input_file.close()

    print(input_file) 
    print(f'test input: {test_input}')

    print(f'formated input: {format(test_input)}')

    test_rules, test_updates = format(test_input)

    print(f'part1 test: {part1(test_rules,test_updates)}')

    rules, update = format(input_string)

    print(f'part1 solution: {part1(rules,update)}')
