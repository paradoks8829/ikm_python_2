from ui import display_main_menu, collect_officials_and_relations, display_bribe_calculation_results

def main():
    while True:
        display_main_menu()
        choice = input("Выберите пункт меню (1-2): ").strip()
        
        if choice == "1":
            root = collect_officials_and_relations()
            if root is not None:
                display_bribe_calculation_results(root)
            input("\nНажмите Enter для продолжения...")
            
        elif choice == "2":
            print("\nДо свидания!")
            break
            
        else:
            print("\nОшибка: неверный выбор!")
            input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()