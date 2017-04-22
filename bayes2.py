
f = open('first.txt').readlines() #first.txt

f = [i.strip('\n').split() for i in f]

new_dict1 = {}
second_dict1 = {}

new_dict2 = {}
second_dict2 = {}

tree = {}
the_input = ["health", "sedentary", "agressive", "no"]
models = list(zip(*f)[len(f[0])-1])


model1 = list(set(models))[0]
model2 = list(set(models))[1]

flag = True
sorted_data = zip(*f)


the_model = sorted_data[len(sorted_data)-1]
new_sorted_data = sorted_data[:len(sorted_data)-1]
tree.setdefault(model1, {})
tree.setdefault(model2, {})


for i, column in enumerate(new_sorted_data):
    new_dict1 = {}
    second_dict1 = {}

    new_dict2 = {}
    second_dict2 = {}
    for b, sample in enumerate(column):

        if the_model[b] == model1:
            if sample not in new_dict1.keys():
                new_dict1[sample] = 1

                second_dict1[i+1] = new_dict1
                tree[model1].update(second_dict1)

            else:
                new_dict1[sample] += 1

                second_dict1[i+1] = new_dict1
                tree[model1].update(second_dict1)

        else:
            if sample not in new_dict2.keys():
                new_dict2[sample] = 1

                second_dict2[i+1] = new_dict2
                tree[model2].update(second_dict2)

            else:
                new_dict2[sample] += 1

                second_dict2[i+1] = new_dict2
                tree[model2].update(second_dict2)


print tree


###################

model1_prob = models.count(model1)/float(len(models))
model2_prob = models.count(model2)/float(len(models))

print model1_prob
print model2_prob


user_input = ["health", "active", "aggressive", "no"]



probabilites1 = [tree[model1][i+1][user_input[i]]/float(models.count(model1)) for i in range(len(user_input))]

probabilites2 = [tree[model2][i+1][user_input[i]]/float(models.count(model2)) for i in range(len(user_input))]

print probabilites1

print probabilites2

probabilites1.append(model1_prob)
probabilites2.append(model2_prob)

final_prob1 = 1

final_prob2 = 1

for i in probabilites1:
    final_prob1 *= i

for i in probabilites2:
    final_prob2 *= i

if final_prob1 > final_prob2:
    print "i500"

else:
    print "i100"
#it finally works!!!!!!!!
