import pandas as pd
import grafice

t= pd.read_csv("dataset_vehicle.csv",index_col=0)
grafice.distributie(t,["RADIUS_RATIO","PR.AXIS_ASPECT_RATIO","MAX.LENGTH_ASPECT_RATIO"])
grafice.show()
