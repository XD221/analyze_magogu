from module import *
from datetime import datetime

def read_csv_file(data):
    df = p.read_csv(data)
    return df

def read_ftr_file(data):
    df = p.read_feather(data)
    return df

class Load_data:
    def __init__(self):
        data = None
        uploaded_files = st.file_uploader('Subir archivo CSV o FTR', type=['csv', 'ftr'], accept_multiple_files=True)
        if uploaded_files:
            for uploaded_file in uploaded_files:
                file_type = uploaded_file.name.split('.')[-1]
                if file_type == 'csv':
                    data = read_csv_file(uploaded_file)
                elif file_type == 'ftr':
                    data = read_ftr_file(uploaded_file)
                st.write(data)
        btn_save = st.button('Guardar Datos')
        if btn_save:
            if data is None:
                st.warning('Sin datos', icon="⚠️")
            else:
                file_name = datetime.now().strftime("%y%m%d%I%M%S")
                #data.to_feather(f'./bin/{file_name}.ftr')
                ##redis_con.hset('')
                st.warning('Datos Guardados', icon="⚠️")