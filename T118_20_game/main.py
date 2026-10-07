
def read_choice(prompt, allowed):
    while True:
        user_input = input(prompt).strip()
        if user_input in allowed:
            return user_input
        print("Некорректный ввод. Попробуйте снова.")


def inspect_table():
    print("\n[Стол] Вы внимательно осмотрели стол и нашли записку с кодом: 314")
    return True


def try_cabinet(has_clue, code):
    return has_clue and code.strip() == "314"


def can_escape(has_key):
    return bool(has_key)


def show_rules():
    print("\n=== ПРАВИЛА ИГРЫ: ПОБЕГ ИЗ КОМНАТЫ ===")
    print("• Вы заперты в комнате. У вас есть ровно 6 ходов, чтобы сбежать.")
    print("• В комнате есть: стол, шкаф и дверь.")
    print("• Порядок действий: осмотреть стол -> открыть шкаф кодом -> открыть дверь ключом.")
    print("• Каждое игровое действие расходует 1 ход (даже неудачное).")
    print("• Ошибка при выборе пункта меню ход НЕ расходует.\n")


def play_game():
    attempts = 6
    has_clue = False
    has_key = False

    print("\n--- Вы очнулись в запертой комнате. Нужно найти выход! ---")

    while attempts > 0:
        print(f"\nОсталось ходов: {attempts}")
        print("1 — Осмотреть стол")
        print("2 — Открыть шкаф")
        print("3 — Открыть дверь")

        action = read_choice("Выберите действие (1-3): ", ["1", "2", "3"])

        if action == "1":
            has_clue = inspect_table()
            attempts -= 1

        elif action == "2":
            user_code = input("Введите код от замка шкафа: ")
            if try_cabinet(has_clue, user_code):
                has_key = True
                print("[Шкаф] Код подошел! Замок щелкнул, и вы забрали ключ.")
            else:
                if not has_clue:
                    print("[Шкаф] Замок заперт. Вы даже не знаете кодовую комбинацию!")
                else:
                    print("[Шкаф] Неверный код!")
            attempts -= 1

        elif action == "3":
            if can_escape(has_key):
                print("\n[Дверь] Вы вставили ключ, повернули его и успешно сбежали! ПОБЕДА!")
                return
            else:
                print("[Дверь] Дверь заперта на замок. Нужен ключ!")
            attempts -= 1

    print("\n[Поражение] У вас закончились ходы! Вы остались заперты навсегда.")


# Главное меню
def main():
    while True:
        print("\n=== ГЛАВНОЕ МЕНЮ ===")
        print("1 - Начать")
        print("2 - Правила")
        print("0 - Выход")

        choice = read_choice("Выберите пункт: ", ["0", "1", "2"])

        if choice == "1":
            play_game()
        elif choice == "2":
            show_rules()
        elif choice == "0":
            print("Спасибо за игру! До свидания.")
            break


if __name__ == "__main__":
    main()
