##########################################################################################
##   Data Resources:
##   http://guidetodatamining.com/assets/guideChapters/DataMining-ch6.pdf
##
##   Project:
##   this is a naive bayes classifer built in Python.
##
##   Features:
##   -fully compatable with both csv and regular spaced data values.
##   -easy to implement in a class
##
##   Upgrades:
##   by 5/1/17, this code will be upgraded by using a Gaussian distribution, as well as being built into a class method.
##
##   Installation:
##   pip Installation will be available by 5/20/17
def text_input(first_f, marker):
    if marker: #whether or not it is a csv file
        return [i.strip('\n').split(',') for i in first_f]

    else:
        return [i.strip('\n').split() for i in first_f]

def integer_input(first_f, marker):
    if marker:
        return [map(float, i.strip('\n').split(',')) for i in first_f]

    else:
        return [map(float, i.strip('\n').split()) for i in first_f]
answer = raw_input("Enter the type of data: (text/integer) ")
the_type = raw_input("Enter the data formate: (csv/spaces) ")
flag = True
if answer == "csv":
    flag = True

else:
    flag = False


f = open('first.txt').readlines()

if answer == "text":
     f = text_input(f, flag)
else:
    f = integer_input(f, flag)


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
