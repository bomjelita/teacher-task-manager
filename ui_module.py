from task_logic import add_task, get_all_tasks, mark_task_done, delete_task, clear_completed

def show_menu():
    """Отображение главного меню"""
    print("\n=== Менеджер задач педагога ===")
    print("1. Добавить задачу")
    print("2. Показать все задачи")
    print("3. Отметить задачу как выполненную")
    print("4. Удалить задачу")
    print("5. Очистить список выполненных задач")
    print("0. Выход")

def main():
    """Главная функция пользовательского интерфейса"""
    while True:
        show_menu()
        choice = input("Выберите пункт меню: ").strip()
        
        if choice == "1":
            name = input("Введите название задачи: ").strip()
            desc = input("Введите описание (можно пропустить): ").strip()
            task = add_task(name, desc)
            print(f"Задача '{task['name']}' добавлена!")
        
        elif choice == "2":
            tasks = get_all_tasks()
            if not tasks:
                print("Список задач пуст.")
            else:
                print("\nСписок задач:")
                for t in tasks:
                    print(f"[{t['id']}] {t['name']} - {t['status']} ({t['created']})")
        
        elif choice == "3":
            task_id = int(input("Введите ID задачи: "))
            if mark_task_done(task_id):
                print("Задача отмечена как выполненная!")
            else:
                print("Задача не найдена.")
        
        elif choice == "4":
            task_id = int(input("Введите ID задачи для удаления: "))
            delete_task(task_id)
            print("Задача удалена!")
        
        elif choice == "5":
            clear_completed()
            print("Выполненные задачи удалены!")
        
        elif choice == "0":
            print("До свидания!")
            break
        
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()