
hamilton=[essay1,essay6,essay7,essay8,essay9,essay11,essay65,essay71,essay74,essay82,essay83]
john_jay=[essay2,essay3,essay4,essay5,essay64]
madison=[essay10,essay14,essay18,essay19,essay20,essay37,essay40,essay45,essay47,essay48]
disputed=[essay50,essay51]
total_essays=hamilton+john_jay+madison+disputed

import numpy as np
import pandas as pd
import random as rd
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt

ham_essays=['h1','h6','h7','h8','h9','h11','h65','h71','h74','h82','h83']
jay_essays=['j2','j3','j4','j5','j64']
madison_essays=['m10','m14','m18','m19','m20','m37','m40','m45','m47','m48']
disputed_essays=['Disputed 1',"Disputed 2"]
var=['sentences', 'total_words', 'average_words_in_a_sentence','average_length_of_words']+['to', 'with', 'from', 'but', 'in', 'upon', 'and', 'or']

data=pd.DataFrame(columns=[*ham_essays,*jay_essays,*madison_essays,*disputed_essays],index=var)
#print(data.head())
#for essay in data.index:
    #data.loc[essay,'sentences':'or']=np.matrix(clean_text(essay))
for i in range(len(total_essays)):
    matrix=np.matrix(clean_text(total_essays[i]))
    data.iloc[0:12,i]=matrix
    
print(data.head())

scaled_data=preprocessing.scale(data.T)
pca=PCA()
pca.fit(scaled_data)
pca_data=pca.transform(scaled_data)
per_var=np.round(pca.explained_variance_ratio_*100,decimals=1)
labels=['sen', 'totwords', 'awISen','a_w_l','to', 'with', 'from', 'but', 'in', 'upon', 'and', 'or']

plt.bar(x=range(1,len(per_var)+1),height=per_var,tick_label=labels)
plt.ylabel('Percentage of Explained Variance')
plt.xlabel("Principal Component")
plt.show()

pca_df=pd.DataFrame(pca_data,index=[*ham_essays,*jay_essays,*madison_essays,*disputed_essays],columns=labels)

plt.scatter(pca_df.sen,pca_df.totwords)
plt.title('PCA Graph')
plt.xlabel('PC1-{0}%'.format(per_var[0]))
plt.ylabel('PC2-{0}%'.format(per_var[1]))

for sample in pca_df.index:
    plt.annotate(sample,(pca_df.sen.loc[sample],pca_df.totwords.loc[sample]))
    
plt.show()
