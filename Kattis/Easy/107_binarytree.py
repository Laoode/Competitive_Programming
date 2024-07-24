MOD = 1000000007

def process_instruction(instruction, node):
    if instruction == 'L':
        return 2 * node
    elif instruction == 'R':
        return 2 * node + 1
    elif instruction == 'U':
        return node // 2
    return node

def follow_instructions(start_node, instructions):
    nodes = {start_node}
    for instruction in instructions:
        new_nodes=set()
        for node in nodes:
            if instruction == 'L':
                new_nodes.add(2 * node)
            elif instruction == 'R':
                new_nodes.add(2 * node + 1)
            elif instruction == 'U':
                new_nodes.add(node // 2)
        nodes.update(new_nodes)
        
    return nodes

def solve_binary_tree_problem(test_cases):
    results = []
    for idx, (instructions1, instructions2) in enumerate(test_cases):
        current_node = 1
        for instruction in instructions1:
            current_node = process_instruction(instruction, current_node)
        
        possible_nodes = follow_instructions(current_node, instructions2)
        result_count = len(possible_nodes) % MOD
        results.append(f"Case {idx + 1}: {result_count}")
    return results
    
def read_input():
    N = int(input().strip())
    test_cases = []
    
    
    for _ in range(N):
        S = input().strip()
        T = input().strip()
        test_cases.append((S,T))
    return test_cases

test_cases = read_input()


results = solve_binary_tree_problem(test_cases)
for result in results:
    print(result)