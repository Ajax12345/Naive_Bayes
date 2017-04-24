#to do: implement in a class
from math import e, pi
def mssdev(the_list, x):

    o = pow(sum([pow(i-sum(the_list)/float(len(the_list)), 2) for i in the_list])/float((len(the_list)-1)), 0.5)

    u = sum(the_list)/float(len(the_list))
    return (1/(float(pow(2*pi, 0.5)*o)))*pow(e, ((-1*(x-u)**2)/float(2*pow(o, 2))))

def functional_density(o, u, x):
    return (1/(float(pow(2*pi, 0.5)*o)))*pow(e, ((-1*(x-u)**2)/float(2*pow(o, 2))))

def prediction(ssdevs, mu, user_input, all_models):
    total_prob = {}
    for model in all_models:
        density = [functional_density(ssdevs[model][column+1], mu[model][column+1], value) for column, value in enumerate(user_input)]
        multiplyer = 1
        for i in density:
            multiplyer *= i

        total_prob[model] = multiplyer

    fitted_results = {prob:model for model, prob in total_prob.items()}
    return fitted_results[max(fitted_results.keys())]


def standard_deviation(thelst):
    average = sum(thelst)/float(len(thelst))
    variance = sum([pow(i-average, 2) for i in thelst])
    return pow(variance/float(len(thelst)-1), 0.5)

def means(thelst):
    return sum(thelst)/float(len(thelst))

f = open('first.txt').readlines()

f = [map(float, i.strip('\n').split()) for i in f]


totals = {}

models = [i[len(i)-1] for i in f]

for i in models:
    totals.setdefault(i, {})


#below, the sum of all values in each column in our data structure

for i in f:
    for b in range(1, len(i[:len(i)])): #used to be :len(i)-1
        totals[i[len(i)-1]][b] = 0


for i in f:
    for b in range(1, len(i[:len(i)])):
        totals[i[len(i)-1]][b] += i[b-1]



######################Below, the list of all the data in the columns
numericValues = {}

for i in models:
    numericValues.setdefault(i, {})



for i in f:
    for b in range(1, len(i[:len(i)])): #used to be :len(i)-1
        numericValues[i[len(i)-1]][b] = []

for i in f:
    for b in range(1, len(i[:len(i)])):
        numericValues[i[len(i)-1]][b].append(i[b-1])


##############################################################################################################
#Below, calculate standard deviation for the data in each column:
ssd = {}

for i in models:
    ssd.setdefault(i, {})

for i in list(set(models)):

    for b in range(1, len(f[0])):

        standard = standard_deviation(numericValues[i][b])
        ssd[i][b] = standard

print ssd
#Calculate the means for each column
the_means = {}

for i in models:
    the_means.setdefault(i, {})

for i in list(set(models)):
    for b in range(1, len(f[0])):
        the_means[i][b] = means(numericValues[i][b])

print the_means


the_input = [6, 80, 74, 39, 48, 46.1, 0.250, 40]

print prediction(ssd, the_means, the_input, list(set(models)))
