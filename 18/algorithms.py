def calculate_minimal_bribe_path(node):
    """Вычисляет минимальную сумму взяток и путь для их сбора"""
    if not node.children:
        return node.bribe, [node.id]
    
    best_cost = float('inf')
    best_path = None
    
    for child in node.children:
        child_cost, child_path = calculate_minimal_bribe_path(child)
        total_cost = child_cost + node.bribe
        
        if total_cost < best_cost:
            best_cost = total_cost
            best_path = child_path + [node.id]
    
    return best_cost, best_path


def format_bribe_path(path):
    """Форматирует путь сбора взяток для вывода на экран"""
    if not path:
        return ""
    
    result = []
    for i, id in enumerate(path):
        if i == len(path) - 1:
            result.append(f"{id} (главный)")
        else:
            result.append(str(id))
    return " -> ".join(result)