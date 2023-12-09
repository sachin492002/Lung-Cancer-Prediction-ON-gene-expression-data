import json, os
import shutil
import pandas as pd

def preprocess_tcga_data(json_file, source_dirctory, target_dirctory):
   
    if not json_file or json_file == '':
        return False
    if not os.path.exists(source_dirctory):
        return False
    if not os.path.exists(target_dirctory):
        os.makedirs(target_dirctory)
    
    # read json_file
    with open(json_file, 'r') as jf:
        json_data = jf.read()
    
    json_info = json.loads(json_data)
    
    for file_info in json_info:
        file_id = file_info['file_id']
        file_name = file_info['file_name']
        submit_id = file_info['associated_entities'][0]['entity_submitter_id']
        source_file = source_dirctory + '/' + file_id + '/' + file_name
        target_file = target_dirctory + '/' + submit_id + '.tsv'
        shutil.copy(source_file, target_file)
        print('file_name :{} copy done'.format(file_name))
        
# preprocess_tcga_data("D:\BTp\data\metadata.cart.2023-03-02.json","D:\BTp\data","D:\BTp\processdata")

def prodata(source_dirctory,target_dirctory):
    if not os.path.exists(source_dirctory):
        return False
    if not os.path.exists(target_dirctory):
        os.makedirs(target_dirctory)
    files = os.listdir(source_dirctory) 
    
    for file in files:
        if file.endswith('.tsv'): 
            file_path = os.path.join(source_dirctory, file)
            df = pd.read_csv(file_path, sep='\t',header=None,skiprows=[0,2,3,4,5],usecols=[0,1,2,3])
            f= os.path.splitext(file)[0]
            df.to_csv(target_dirctory+'/'+f+'.csv',index=False,header=False)
            print("done")

# prodata("D:\BTp\processdata","D:\BTp\Process1data")


GFF3 = pd.read_csv(
    filepath_or_buffer='Homo_sapiens.GRCh38.103.gtf',
    sep='\t', 
    header=None,
    names=['seqid','source', 'type','start', 'end','score','strand', 'phase', 'attributes'],
    skiprows=[0,1,2,3,4]
)
GFF3 = GFF3[GFF3['source'].notnull()]

GFF3 = GFF3[GFF3['type']=='gene']

GFF3['gene_id'] = GFF3.apply(lambda x : x.attributes.split(';')[0].strip().split(' ')[1].strip('"'), axis=1)  
GFF3['gene_name'] = GFF3.apply(lambda x : x.attributes.split(';')[2].strip().split(' ')[1].strip('"'), axis=1)
GFF3['gene_biotype'] = GFF3.apply(lambda x : x.attributes.split(';')[4].strip().split(' ')[1].strip('"'), axis=1)

GFF3 = pd.DataFrame(GFF3, columns = ['gene_id', 'gene_name', 'gene_biotype'])
# print(GFF3)


def all_data(source_dirctory,df):
    if not os.path.exists(source_dirctory):
        return False
   
    files = os.listdir(source_dirctory) 

    for file in files:
        f= os.path.splitext(file)[0]
        data = pd.read_csv(
            filepath_or_buffer=source_dirctory + '/' + file,header=None,names=['gene_id',f])
        data['gene.id'] = data.apply(lambda x:x.gene_id.split('.')[0],axis=1)
        df = pd.merge(df,data,on='gene_id')
    return df

                           
df = all_data("./Process1data",GFF3)
print(df)