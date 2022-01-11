from flask import Flask, request, jsonify
import json
import pandas as pd
import joblib

classe_modelos = ["LinearDiscriminantAnalysis", "QuadraticDiscriminantAnalysis",
                  "AdaBoostClassifier", "BaggingClassifier", 
                  "ExtraTreesClassifier", "RandomForestClassifier", 
                  "LogisticRegression", "BernoulliNB", "GaussianNB", 
                  "KNeighborsClassifier", "MLPClassifier", "LinearSVC", "NuSVC",
                  "SVC", "DecisionTreeClassifier", "ExtraTreeClassifier"]

modelos = {}
for algoritmo in classe_modelos:
    modelos[algoritmo] = (joblib.load('modelos/modelo_ia'+algoritmo+'.pyobj'))

app = Flask(__name__)
app.run(debug=False,port=5050)

@app.route('/results',methods=['POST'])
def getResults():
    entrada = request.data.decode("utf-8").split(',')
    #entrada = [request.get_json()['SIFT'], request.get_json()['Polyphen'],
    # request.get_json()['PROVEAN'], request.get_json()['ExAC'], 
    # request.get_json()['Ndamage'], request.get_json()['COMMON']]
    entradaDf = pd.DataFrame([pd.Series(entrada)])
    entradaDf.columns = ['SIFT', 'Polyphen', 'PROVEAN', 'ExAC', 'Ndamage', 'COMMON']

    result = {}
    resultStr = ""
    for algoritmo in classe_modelos:
        result[algoritmo] = str(modelos[algoritmo].predict(entradaDf)[0])
        resultStr += algoritmo + ':' + str(modelos[algoritmo].predict(entradaDf)[0]) + "\n"

    return resultStr, 200
