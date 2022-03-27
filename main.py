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
    count = []
    for elem in data:
        count.append((elem['retweetCount'], elem['content']))
    top_10 = sorted(count, key=lambda x: x[0], reverse=True)[:10]
    print("Top 10 tweets con más retweets: \n")
    for elem in range(len(top_10)):
        string = f'\nretweets: {top_10[elem][0]}\ntweet: {top_10[elem][1]}'
        print(f'{elem + 1}. {string}\n')


# Tweet count Top 10
def func_2(data):
    count = {}
    for elem in data:
        if elem['user']['username'] in count:
            count[elem['user']['username']] += 1
        else:
            count[elem['user']['username']] = 1
    top_10 = sorted(count.items(), key=lambda x: x[1], reverse=True)[:10]
    print("Top 10 users con más tweets: \n")
    for elem in range(len(top_10)):
        string = f'\nusername: {top_10[elem][0]}\ntweets: {top_10[elem][1]}'
        print(f'{elem + 1}. {string}\n')


# Dates tweeted Top 10
def func_3(data):
    pass


# Hashtags Top 10
def func_4(data):
    pass


if __name__ == "__main__":
    main()

