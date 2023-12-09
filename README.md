
# Lung Cancer Prediction using deep learning with gene expression data
BTP Code - B23SA01





## Authors
- Guide - [Dr. Amilpur Santhosh](https://scholar.google.co.in/citations?user=JaOWIGEAAAAJ&hl=en)
- [Akash Yadav - S20200010009](https://github.com/AK-aShH)
- [Sachin Meena - S20200010181](https://github.com/sachin492002)
- [Seshu Medapi - S20200010124](https://www.github.com/octokatherine)



## Data and Preprocessing Block 

- The data folder contains data for multiple patients in which each patient have it's own tsv data file containing gene expresion data. 

- MergeHelp contains data into csv for each patient.

- preprocess.ipynb contains the Preprocessing code.

-  TCGA_Labeled.csv file contains the preprocessed data.
## Feature Selection(KL Divergence) 
- KL_Divergence jupyter notebook contains code for Kl divegence gene selection.

- Labeled_Final_Features csv file contains the data selected after kl divergence gene selection.

## Model 

- Training jupyter source file coatains the model code for prediction of lung cancer.

- Results coatains the output after model Training.
## Gene Augmentation and Particle Swarm optimization


- Augmentation jupyter source file conatains code for the gene expression data.

- Augmentation_Data1.csv contains data for weighted mixed observations.

- Augmentation_Data2.csv contains data for generative adversarial networks. 

- Optimizations jupyter notebook contains the code for particle Swarm optimization.
 
-  TCGA_Labled_PSO constains the data with genes selected after PSO optimization.

- TCGA_Labled_PSO_KL contains the data after pso and kl divergence.

## Run Locally

Download the project



Go to the project directory

```bash
  cd Btp
```

Install dependencies

```bash
  pip install scikit-learn,pandas,pytorch,matplotlib,seaborn,scipy,tensorflow,shutil
```




## DATA
- You can find all the data and csv's at 
```https://drive.google.com/drive/folders/1X4EUCgavlefy46yt4XpEVxs8hoy5MnXU?usp=drive_link```