import json


def main():
    print('Cargando datos... esto demora unos segundos...')
    with open('data/farmers-protest-tweets-2021-03-5.json', 'r') as f:
        data = []
        for d in f:
            data.append(json.loads(d))
    print('Carga de datos completada.')
    while True:
        x = input("Que función quieres ejecutar? (1, 2, 3, 4): ")
        if x == '1':
            func_1(data)
        elif x == '2':
            func_2(data)
        elif x == '3':
            func_3(data)
        elif x == '4':
            func_4(data)
        else:
            print("Programa cerrado.")
            exit()


# Retweeted Top 10
def func_1(data):
    pass


# Tweet count Top 10
def func_2(data):
    pass


# Dates tweeted Top 10
def func_3(data):
    pass


# Hashtags Top 10
def func_4(data):
    pass


if __name__ == "__main__":
    main()

