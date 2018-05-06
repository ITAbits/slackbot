from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def stringMatch(searchWord, dataWords):
    if (type(dataWords) == str):
        dataWords = [dataWords]

    similarity = []
    for i in range(len(dataWords)):
        #print(dataWords[i])
        #print(similar(searchWord, dataWords[i]))
        similarity.append(similar(searchWord, dataWords[i]))

    if(max(similarity) == 1):
        return "resultado para "+ searchWord + " encontrado"
    elif(max(similarity) > 0.35):
        return "Voce quis dizer: "+ dataWords[similarity.index(max(similarity))]+ "?"
    else:
        return ''
        #return "Nenhum resultado encontrado. Deseja iniciar um topico para "+ searchWord+ "?"
    #values.index(max(similarity))

lng = ["ruby", "freaking fair", "c++", "iurbriubirub", "r o r", "ror", "Ruby Sinatra", "raoubi", "iiiiii"]
x = stringMatch("c++ eita ruby", lng)
print(x)