
f = open('my_data.txt', 'a')

key_words = {"fetch":3, "show":4, "check":1, "display":2, "set":6, "who":7, "what":7, "where":7, "how":7}

listings = [["weather", "forecast"], ["event", "activity", "schedule"], ["news", "headlines"], ["scores", "stats", "standings", "results"]]
models = [3, 4, 5, 6]

for i in key_words.values():
    if i == 7:
        data = str(i)+" 4 4 4 4 6"
        f.write(data)
        f.write('\n')

    else:
        data = str(i)+" 4 4 4 4 4"

        f.write(data)
        f.write('\n')

values = [i for i in key_words.values() if i != 7]

for i in range(4):
    data = ["4", "4", "4", "4"]
    data[i] = "5"
    for b in values:

        f.write(str(b)+" "+' '.join(data)+" "+str(models[i]))
        f.write('\n')



f.close()
