from module import *

class Show_data:
    def __init__(self):
        col1, col2 = None, None
        df = None
        search_input = None
        select_column = None
        path = "./bin/*.ftr"
        datas = glob(path)
        if len(datas):
            df = p.concat(p.read_feather(f) for f in datas)
            col1, col2 = st.columns([1, 1])
            with col1:
                search_input = st.text_input("Filtro", placeholder="Que Desea Buscar")
            with col2:
                select_column = st.selectbox("", (col for col in df.columns))
            st.write(
                df[df[f"{select_column}"].astype(str).str.contains(search_input)]
            )
        else:
            st.warning("No Existen datos", icon="⚠️")