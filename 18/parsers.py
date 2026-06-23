from models import Official

def parse_officials_data(input_string):
    """Парсит данные о чиновниках (id и взятки)"""
    lines = input_string.strip().split('\n')
    if not lines or not lines[0].strip():
        return None, "пустой ввод"
    
    try:
        n = int(lines[0].strip())
        if n <= 0:
            return None, "количество чиновников должно быть положительным"
    except ValueError:
        return None, "некорректное количество чиновников"
    
    if len(lines) < n + 1:
        return None, f"недостаточно данных: ожидается {n} строк с взятками"
    
    officials = {}
    
    for i in range(1, n + 1):
        parts = lines[i].strip().split()
        if len(parts) != 2:
            return None, f"строка {i}: ожидается 2 числа (id и взятка)"
        
        try:
            id = int(parts[0])
            bribe = int(parts[1])
            if bribe < 0:
                return None, f"взятка не может быть отрицательной"
            officials[id] = Official(id, bribe)
        except ValueError:
            return None, f"строка {i}: некорректные числа"
    
    if len(officials) != n:
        return None, "обнаружены дублирующиеся id"
    
    return officials, None


def build_hierarchy_from_relations(relations_string, officials):
    """Строит иерархию из строки отношений и возвращает корневой узел"""
    if not relations_string or not relations_string.strip():
        return None, "не указаны отношения подчинения"
    
    parts = relations_string.strip().split()
    
    if len(parts) % 2 != 0:
        return None, "каждая пара должна содержать начальника и подчиненного"
    
    edges = []
    has_parent = set()
    parent_count = {}
    
    for i in range(0, len(parts), 2):
        try:
            boss_id = int(parts[i])
            sub_id = int(parts[i + 1])
            
            if boss_id not in officials:
                return None, f"чиновник с id {boss_id} не обнаружена"
            if sub_id not in officials:
                return None, f"чиновник с id {sub_id} не обнаружена"
            
            edges.append((boss_id, sub_id))
            has_parent.add(sub_id)
            
            parent_count[sub_id] = parent_count.get(sub_id, 0) + 1
            if parent_count[sub_id] > 1:
                return None, f"чиновник {sub_id} имеет более одного начальника"
            
        except ValueError:
            return None, "некорректные id в отношениях"

    graph = {id: [] for id in officials}
    for boss_id, sub_id in edges:
        graph[boss_id].append(sub_id)

    visited = set()
    recursion_stack = set()
    
    def has_cycle(node_id):
        if node_id in recursion_stack:
            return True
        if node_id in visited:
            return False
        
        visited.add(node_id)
        recursion_stack.add(node_id)
        
        for child_id in graph[node_id]:
            if has_cycle(child_id):
                return True
        
        recursion_stack.remove(node_id)
        return False
    
    for node_id in officials:
        if node_id not in visited:
            if has_cycle(node_id):
                return None, "обнаружен цикл"

    for boss_id, sub_id in edges:
        officials[boss_id].children.append(officials[sub_id])

    roots = []
    for id, official in officials.items():
        if id not in has_parent:
            roots.append(official)
    
    if len(roots) == 0:
        return None, "нет главного чиновника"

    valid_root = None
    for root in roots:
        visited = set()
        def dfs(node):
            visited.add(node.id)
            for child in node.children:
                dfs(child)
        dfs(root)
        
        if len(visited) == len(officials):
            valid_root = root
            break
    
    if valid_root is not None:
        return valid_root, None
    
    if len(roots) > 1:
        return None, "не все чиновники достижимы из главного"
    
    return None, "не все чиновники достижимы из главного"