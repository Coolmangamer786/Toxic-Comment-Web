import pickle
import warnings

warnings.filterwarnings('ignore')

def predict(s):
    pm = pickle.load(open('models/tvf_model.pkl', 'rb'))
    rmf=pickle.load(open('models/rf_model.pkl', 'rb'))
    str = [s]
    com_vect = pm.transform(str)
    output=rmf.predict_proba(com_vect)
    return f"{round(output[0][1],2)*100}"
