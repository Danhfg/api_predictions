import joblib
import pandas as pd

classe_modelos = ["LinearDiscriminantAnalysis", "QuadraticDiscriminantAnalysis",
                  "AdaBoostClassifier", "BaggingClassifier", 
                  "ExtraTreesClassifier", "RandomForestClassifier", 
                  "LogisticRegression", "BernoulliNB", "GaussianNB", 
                  "KNeighborsClassifier", "MLPClassifier", "LinearSVC", "NuSVC",
                  "SVC", "DecisionTreeClassifier", "ExtraTreeClassifier"]

entradaDf = pd.DataFrame([pd.Series([1,1,1,1,1,1])])
entradaDf.columns = ['SIFT', 'Polyphen', 'PROVEAN', 'ExAC', 'Ndamage', 'COMMON']


modelos = {}
result = {}
for algoritmo in classe_modelos:
    modelos[algoritmo] = (joblib.load('modelos/modelo_ia'+algoritmo+'.pyobj'))
    result[algoritmo] = modelos[algoritmo].predict(entradaDf)[0]

print(result)