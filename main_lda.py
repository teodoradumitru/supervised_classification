import pandas as pd
import sklearn.discriminant_analysis as discrim
import grafice_lda
import sklearn.metrics as metrics
import numpy as np

set_invatare = pd.read_csv("dataset_vehicle.csv", index_col=0)
variabile = list(set_invatare)
nr_variabile = len(variabile)
variabile_predictor = variabile[:(nr_variabile - 1)]
variabila_tinta = variabile[nr_variabile - 1]

x = set_invatare[variabile_predictor].values
y = set_invatare[variabila_tinta].values
print(x,y,sep="\n")

# Construire model
model_lda = discrim.LinearDiscriminantAnalysis()
model_lda.fit(x, y)

# Preluare rezultate si aplicare model
# Preluare etichete clase
clase = model_lda.classes_
print(clase)
# Calcul scoruri discriminante
z = model_lda.transform(x)
n, q = z.shape
etichete_z = ["z" + str(i) for i in range(1, q + 1)]
nume_instante = list(set_invatare.index)
t_z = pd.DataFrame(z, nume_instante, etichete_z)
t_z.to_csv("z.csv")
g = model_lda.means_
zg = model_lda.transform(g)
if q>1:
    grafice_lda.biplot(z, zg, y, clase)
for i in range(q):
    grafice_lda.distributie(z, i, y, clase)

# Clasificare in setul de antrenare
clasificare_b = model_lda.predict(x)
tabel_clasificare_b = pd.DataFrame(
    data={
        "Clasa": y,
        "Predictie": clasificare_b
    }, index=nume_instante
)
tabel_clasificare_b.to_csv("clasif_b.csv")

tabel_clasificare_err = tabel_clasificare_b[y != clasificare_b]
tabel_clasificare_err.to_csv("clasif_err.csv")

# Calcul matrice mal-clasificari
mat_conf = metrics.confusion_matrix(y, clasificare_b)
t_mat_conf = pd.DataFrame(mat_conf, clase, clase)
t_mat_conf["Acuratete"] = np.diagonal(mat_conf) * 100 / np.sum(mat_conf, axis=1)
print(t_mat_conf)
t_mat_conf.to_csv("mat_conf.csv")
print("Acuratete globala:", sum(np.diagonal(mat_conf)) * 100 / n)


grafice_lda.show()