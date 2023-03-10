from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from Uniandes_Framework.ml_tools.abstract_classifier import Abstract_Classifier

class Log_Reg_Classifier(Abstract_Classifier):
    def __init__(self,*args,**kwargs):
        self.model_name="Logistic_Regression"
        self.model = make_pipeline(StandardScaler(), LogisticRegression())
        super().__init__(*args,**kwargs)
