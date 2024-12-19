import requests


def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/RUB"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['rates']['USD']
    else:
        print("Ошибка при получении данных о курсах валют.")
        return None


def convert_rub_to_usd(rubles, exchange_rate):
    return rubles * exchange_rate


def main():
    print("Программа конвертации рублей в доллары")

    exchange_rate = get_exchange_rate()
    if exchange_rate is None:
        return

    print(f"Текущий курс рубля к доллару: 1 RUB = {exchange_rate} USD")

    while True:
        try:
            rubles = float(input("Введите сумму в рублях (или 'exit' для выхода): "))
            dollars = convert_rub_to_usd(rubles, exchange_rate)
            print(f"{rubles} рублей = {dollars:.2f} долларов")
        except ValueError:
            print("Выход из программы.")
            break


if __name__ == "__main__":
    main()
