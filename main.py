import fitdecode
import pandas as pd
import os
import gzip
import shutil

def unzip():
    input_folder = "activities"
    output_folder = os.path.join(input_folder, "unzipped")
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".fit.gz"):
            gz_path = os.path.join(input_folder, filename)
            fit_path = os.path.join(output_folder, filename[:-3]) 

            # Descompacta o arquivo
            with gzip.open(gz_path, 'rb') as f_in:
                with open(fit_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            print(f"Descompactado: {filename} -> {fit_path}")

    print("✅ Todos os arquivos foram descompactados com sucesso!")

def read_fit_file(filename):
    records = []
    with fitdecode.FitReader(filename) as fit_file:
        for frame in fit_file:
            if isinstance(frame, fitdecode.records.FitDataMessage):
                if frame.name == 'record':
                    data = {}
                    for field in frame.fields:
                        data[field.name] = field.value
                    records.append(data)
    
    df = pd.DataFrame(records)
    return df

def read_all_fit_files(folder_path):
    all_dfs = []
    for file in os.listdir(folder_path):
        if file.endswith(".fit"):
            file_path = os.path.join(folder_path, file)
            try:
                df = read_fit_file(file_path)
                df["source_file"] = file  
                all_dfs.append(df)
                print(f"✅ Processado: {file} ({len(df)} registros)")
            except Exception as e:
                print(f"⚠️ Erro ao processar {file}: {e}")
    
    if all_dfs:
        final_df = pd.concat(all_dfs, ignore_index=True)
        print(f"\n📊 Total de registros combinados: {len(final_df)}")
        return final_df
    else:
        print("Nenhum arquivo .fit foi processado.")
        return pd.DataFrame()

# unzip()
folder = "activities/unzipped"
output_csv = "activities/all_runs.csv"

df_final = read_all_fit_files(folder)
df_final.to_csv()

if not df_final.empty:
    df_final.to_csv(output_csv, index=False)
    print(f"\n💾 Arquivo salvo com sucesso em: {output_csv}")
else:

    print("Nenhum dado para salvar.")
