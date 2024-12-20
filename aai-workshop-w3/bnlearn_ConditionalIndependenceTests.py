import bnlearn as bn
import pandas as pd

# definition of directed acyclic graphs (predefined structures)
edges_lungcancer1 = [('Lung_cancer', 'Smoking'), ('Lung_cancer', 'Yellow_Fingers'), ('Lung_cancer', 'Anxiety'), ('Lung_cancer', 'Peer_Pressure'), ('Lung_cancer', 'Genetics'), ('Lung_cancer', 'Attention_Disorder'), ('Lung_cancer', 'Born_an_Even_Day'), ('Lung_cancer', 'Car_Accident'), ('Lung_cancer', 'Fatigue'), ('Lung_cancer', 'Allergy'), ('Lung_cancer', 'Coughing')]
edges_lungcancer2 = [] # up to you

# examples of training data include 'data\lung_cancer-train.csv' or  'data\lang_detect_train.csv', etc.
# examples of net structure (as below): edges_langdet1, edges_langdet2, edges_lungcancer1, edges_lungcancer2
# choices of CI test: chi_square, g_sq, log_likelihood, freeman_tuckey, modified_log_likelihood, neyman, cressie_read
TRAINING_DATA = 'data\lung_cancer-train.csv'
NETWORK_STRUCTURE = edges_lungcancer1
CONDITIONAL_INDEPENDENCE_TEST = 'cressie_read'

# data loading using pandas
data = pd.read_csv(TRAINING_DATA, encoding='latin')
print("DATA:\n", data)

 # creation of the directed acyclic graph (DAG)
DAG = bn.make_DAG(NETWORK_STRUCTURE)
print("DAG:\n", DAG)

# parameter learning using Maximum Likelihood Estimation
model = bn.parameter_learning.fit(DAG, data, methodtype="maximumlikelihood")
print("model=",model)

# statististical test of independence
model = bn.independence_test(model, data, test=CONDITIONAL_INDEPENDENCE_TEST, alpha=0.05)
ci_results = list(model['independence_test']['stat_test'])
num_edges2remove = ci_results.count(False)
print(model['independence_test'])
print("num_edges2remove="+str(num_edges2remove))
