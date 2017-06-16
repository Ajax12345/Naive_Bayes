import collections
from math import e, pi

class Classifier:
    def __init__(self, filename, the_input):
        self.filename = filename
        self.the_input = the_input
        self.final_dictionary = {}

    def functional_density(self, x, o, u):
        if o == 0:
            return 1
        else:
            return 1/float(o*pow(2*pi, 0.5))*pow(e, -0.5*pow(((x-u)/float(o)), 2))

    def make_prediction(self):
        return [a for a, b in self.final_dictionary.items() if b == max(self.final_dictionary.values())][0]



    def classify(self):
        f = open(self.filename).readlines()
        d = collections.defaultdict(list)
        f = [map(float, i.strip('\n').split(",")) for i in f]

        #or

        new_d = collections.defaultdict(list)

        for i in f:
            d[i[-1]].append(i[:-1])

        for a, b in d.items():
            switched = map(list, zip(*b))

            for i in switched:
                ave = sum(i)/float(len(i))

                ssdev = pow(sum(pow(c-ave, 2) for c in i)/float(len(i)-1), 0.5)
                new_d[a].append((ssdev, ave))

        new_d = dict(new_d)

        print new_d


        final_dict = {i:1 for i, b in new_d.items()}

        for i in self.the_input:
            for a, b in new_d.items():
                for c in b:
                    final_dict[a] *= self.functional_density(i, c[0], c[1])

        self.final_dictionary = dict(final_dict)

        #print self.final_dictionary

bayes = Classifier("datafile1.txt", [56, 45])

bayes.classify()

print bayes.make_prediction()
