import pandas as pd
import os
#creating the metadata dataframe for the .txt files in ./data

def load_metadata(file_path):
    """
    Create metadata for VectorSpaceModel from ./data directory
    """
    metadata = {'filename': [], 'content': []}
    for file in os.listdir(file_path):
        if file.endswith(".txt"):
            with open(os.path.join(file_path, file), 'r') as f:
                content = f.read()
                metadata['filename'].append(file)
                metadata['content'].append(content)
                
    metadata = pd.DataFrame(metadata)
    #writes it to the ./data/wedding_data.csv
    metadata.to_csv(file_path + 'wedding_data.csv', index=False)
    return metadata