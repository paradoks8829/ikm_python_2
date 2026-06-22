class QueueUI:
    def __init__(self, queue):
        self.queue = queue
    
    def display_main_menu(self):
        print("\n" + "=" * 60)
        print("     УПРАВЛЕНИЕ ОЧЕРЕДЬЮ")
        print("=" * 60)
        print("1. Ввести данные вручную")
        print("2. Выход")
        print("=" * 60)
    
    def show_help(self):
        print("\n" + "=" * 60)
        print("     ДОСТУПНЫЕ КОМАНДЫ")
        print("=" * 60)
        print("push <число>  - Добавить элемент в конец очереди")
        print()
        print("pop           - Извлечь элемент из начала очереди")
        print()
        print("front         - Показать первый элемент без удаления")
        print()
        print("size          - Показать размер очереди")
        print()
        print("clear         - Очистить очередь")
        print()
        print("exit          - Выйти из режима ручного ввода")
        print("="*60)
    
    def process_command(self, command_parts):
        """Обработка введенной команды"""
        if not command_parts:
            return True
        
        command = command_parts[0].lower()
        
        if command == "push":
            if len(command_parts) != 2:
                print("Ошибка: команда push требует число")
                print("Пример: push 5")
                return True
            try:
                n = int(command_parts[1])
                result = self.queue.push(n)
                print(f"Результат: {result}")
            except ValueError:
                print("Ошибка: необходимо ввести целое число!")
            return True
        
        elif command == "pop":
            result = self.queue.pop()
            if result == "error":
                print("error - очередь пуста!")
            else:
                print(f"Результат: {result}")
            return True
        
        elif command == "front":
            result = self.queue.front()
            if result == "error":
                print("error - очередь пуста!")
            else:
                print(f"Результат: {result}")
            return True
        
        elif command == "size":
            print(f"Размер очереди: {self.queue.get_size()}")
            return True
        
        elif command == "clear":
            confirm = input("Вы уверены, что хотите очистить очередь? (y/n): ").lower()
            if confirm == 'y':
                result = self.queue.clear()
                print(f"Результат: {result}")
            else:
                print("Операция отменена")
            return True
        
        elif command == "help":
            self.show_help()
            return True
        
        elif command == "exit":
            print(self.queue.exit())
            print("Возврат в главное меню")
            return False
        
        else:
            print(f"Неизвестная команда: {command}")
            print("Введите 'help' для просмотра доступных команд")
            return True
    
    def run_manual_mode(self):
        """Режим ручного ввода команд"""
        print("\n" + "=" * 60)
        print("     РЕЖИМ РУЧНОГО ВВОДА ДАННЫХ")
        print("=" * 60)
        print("Вводите команды для работы с очередью")
        print("Для просмотра подсказок введите 'help'")
        print("Для выхода введите 'exit'")
        print("=" * 60)
        
        self.show_help()
        
        while True:
            try:
                command_line = input("\nВведите команду: ").strip()
                
                if not command_line:
                    continue
                
                command_parts = command_line.split()
                
                should_continue = self.process_command(command_parts)
                
                if not should_continue:
                    break
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Произошла ошибка: {e}")
    
    def run(self):
        """Запуск главного меню"""
        while True:
            self.display_main_menu()
            
            try:
                choice = input("Выберите действие (1-2): ").strip()
                
                if choice == "1":
                    self.run_manual_mode()
                    
                elif choice == "2":
                    print("\n" + "=" * 60)
                    print(self.queue.exit())
                    print("=" * 60)
                    break
                else:
                    print("Ошибка: неверный выбор!")
                    print("Пожалуйста, выберите 1 или 2")
                
            except KeyboardInterrupt:
                print("\n\nПрограмма прервана пользователем.")
                break
            except Exception as e:
                print(f"Произошла ошибка: {e}")