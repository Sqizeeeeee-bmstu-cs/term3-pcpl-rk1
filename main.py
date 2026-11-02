from classes import Driver, Autopark, ConnectionDriverToAutopark

autoparks = [
    Autopark(1, "Автоколонна №1"),
    Autopark(2, "Авангард-Транс"),
    Autopark(3, "Центральный таксопарк"),
    Autopark(11, "Автобаза №2"),
]

drivers = [
    Driver(1, "Иванов И.И.", 55000, 1),
    Driver(2, "Петров П.П.", 72000, 1),
    Driver(3, "Сидоров С.С.", 48000, 2),
    Driver(4, "Кузнецов А.В.", 95000, 2),
    Driver(5, "Смирнов К.Д.", 60000, 3),
]

connections = [
    ConnectionDriverToAutopark(1, 1),
    ConnectionDriverToAutopark(1, 2),
    ConnectionDriverToAutopark(2, 3),
    ConnectionDriverToAutopark(2, 4),
    ConnectionDriverToAutopark(3, 5),
    ConnectionDriverToAutopark(3, 1),
    ConnectionDriverToAutopark(11, 4),
]


def main():
    one_to_many = [
        (d.name, d.salary, ap.name)
        for ap in autoparks
        for d in drivers
        if d.autopark_id == ap.id
    ]

    many_to_many_temp = [
        (ap.name, conn.driver_id)
        for ap in autoparks
        for conn in connections
        if ap.id == conn.autopark_id
    ]

    many_to_many = [
        (ap_name, d.name)
        for ap_name, driver_id in many_to_many_temp
        for d in drivers
        if d.id == driver_id
    ]

    print('Задание Г1')
    res_g1 = {
        ap.name: [
            driver_name
            for driver_name, _, autopark_name in one_to_many
            if autopark_name == ap.name
        ]
        for ap in autoparks
        if ap.name.startswith('А')
    }
    print(res_g1)

    print('\nЗадание Г2')
    res_g2 = sorted(
        (
            (ap.name, max(salary for _, salary, autopark_name in one_to_many
                         if autopark_name == ap.name))
            for ap in autoparks
            if any(autopark_name == ap.name for _, _, autopark_name in one_to_many)
        ),
        key=lambda item: item[1],
        reverse=True,
    )
    print(res_g2)

    print('\nЗадание Г3')
    res_g3 = sorted(many_to_many, key=lambda item: item[0])
    print(res_g3)


if __name__ == '__main__':
    main()
