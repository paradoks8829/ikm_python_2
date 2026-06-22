from queue import Queue
from ui import QueueUI

def main():
    queue = Queue()
    ui = QueueUI(queue)
    
    print("=" * 60)
    print("     СИСТЕМА УПРАВЛЕНИЯ ОЧЕРЕДЬЮ")
    print("=" * 60)
    print("Программа для работы с очередью через консоль")
    print("Вы можете:")
    print("  - Вводить команды вручную (push, pop, front, size, clear, exit)")
    print("  - Просматривать подсказки по командам")
    print("  - Выходить из программы")
    print("=" * 60)
    
    ui.run()

if __name__ == "__main__":
    main()