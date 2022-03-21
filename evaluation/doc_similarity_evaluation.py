from scipy import spatial
import gensim.downloader as api
import numpy as np

model = api.load("glove-wiki-gigaword-300") #choose from multiple models https://github.com/RaRe-Technologies/gensim-data

def preprocess(s):
    return [i.lower() for i in s.split()]

def get_vector(s):
    return np.sum(np.array([model[i] for i in preprocess(s) if i in model]), axis=0)


def doc_similarity_evaluation(topic,sentence):

    open("docs\\evaluation\\doc_similarity_evaluationx.txt", 'w').close()
    f = open("docs\\evaluation\\doc_similarity_evaluationx.txt", "a")

    count = 1
    input1 = topic
    output1 = sentence

    for x, y in zip(input1, output1):

        z = 1 - spatial.distance.cosine(get_vector(x), get_vector(y))
        print(z)

        f.write(str(count) + "\n" + str(z) + "\n\n")
        count += 1

    f.close()

    return z

# doc_similarity_evaluation(["What is UX?"], ["User experience is the process of designing a product."])