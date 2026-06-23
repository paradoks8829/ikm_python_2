from parsers import parse_officials_data, build_hierarchy_from_relations
from algorithms import calculate_minimal_bribe_path, format_bribe_path

def display_main_menu():
    print("\n" + "=" * 60)
    print("ПРОГРАММА ДЛЯ ПОЛУЧЕНИЯ ЛИЦЕНЗИИ")
    print("=" * 60)
    print("1. Ввести данные о чиновниках и найти минимальную взятку")
    print("2. Выйти из программы")
    print("=" * 60)


def collect_officials_and_relations():
    """Собирает данные о чиновниках и отношениях от пользователя"""
    print("\nВведите количество чиновников:")
    try:
        n = int(input("> ").strip())
        if n <= 0:
            print("Ошибка: количество должно быть положительным")
            return None
    except ValueError:
        print("Ошибка: введите целое число")
        return None
    
    print(f"\nВведите данные для {n} чиновников (id и взятка):")
    print("Пример: 1 5")
    lines = [f"{n}"]
    
    for i in range(n):
        line = input(f"Чиновник {i+1}: ").strip()
        if not line:
            print("Ошибка: строка не может быть пустой")
            return None
        lines.append(line)
    
    input_data = '\n'.join(lines)
    officials, error = parse_officials_data(input_data)
    
    if officials is None:
        print(f"Ошибка: {error}")
        return None
    
    print("\nВведите отношения подчинения (начальник подчиненный):")
    print("Пример: 1 2 1 3 2 4")
    relations = input("> ").strip()
    
    root, error = build_hierarchy_from_relations(relations, officials)
    if root is None:
        print(f"Ошибка: {error}")
        return None
    
    return root


def display_bribe_calculation_results(root):
    """Выводит результаты расчета минимальной взятки"""
    print(f"\nГлавный чиновник: {root.id}")
    
    cost, path = calculate_minimal_bribe_path(root)
    
    print(f"\nМинимальная сумма взяток: {cost} у.е.")
    print(f"Порядок получения подписей: {format_bribe_path(path)}")