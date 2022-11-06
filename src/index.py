from module import *
from template import *

from random import randint


#Section prove
#st.subheader('Magogu Analítica')


# ============= Config ============
st.set_page_config(
    #layout="wide",
    page_title="Magogu",
    page_icon="😊",
    )
# ============= Variables ============
if 'num' not in st.session_state:
    st.session_state.num = 1
if 'page_id' not in st.session_state:
    st.session_state.page_id = 1
if 'page_update' not in st.session_state:
    st.session_state.page_update = 0
if 'data' not in st.session_state:
    st.session_state.data = []
arr = np.array([1,2,3,4,5], ndmin=5)

# ============= Functions ============

def btn_1_action():
    action_write = """
    ##### Accion del boton 1
    """
    with st.empty():
        st.write(action_write)
def upload_file():
    upload_file = st.file_uploader('Agregar archivo de datos')
    return upload_file

def read_csv_file(data):
    df = p.read_csv(data)
    return df

def write_data(data):
    st.write(data)

# ============= Classes =============
class Header:
    def __init__(self, body):
        self.title = """
             ### Magogu Analitica
             """
        self.help_link = """
            [Ayuda](https://hyper-drizzle-93f.notion.site/Machine-learning-9397f1e008324cd7888fd71950fe55e4 'Redirección a notion del autor')
        """
        #self.tab1, self.tab2, self.tab3, self.tab4 = None, None, None, None
        self.col1, self.col2 = st.columns([1, 0.2])
        with self.col1:
            st.write(self.title)
        with self.col2:
            st.write(self.help_link)
        body_data = body.tabs(["Home", "Mostrar", "Cargar Datos", "Entrenar"])
        self.tab1 = body_data[0]
        self.tab2 = body_data[1]
        self.tab3 = body_data[2]
        self.tab4 = body_data[3]

class Pages:
    def __init__(self, page_id):
        match str(page_id):
            case '1':
                self.home()
            case '2':
                self.show_data()
            case '3':
                self.load_data()
            case '4':
                self.training()
            case _:
                self.error_404()
    def home(self):
        Home()
    def show_data(self):
        Show_data()

    def load_data(self):
        Load_data()
        
    def training(self):
        Training()
    
    def error_404(self):
        self.title = "Error 404"
        return st.write(self.title)

# ============= Main =============
def main():
    # ? Params principal
    header = st.empty()
    body = st.empty()
    footer = st.empty()
    
    # ? Params secondary
    header_data = None
    body_data = None
    footer_data = None
    
    while True:
        num = st.session_state.num
        page_id = st.session_state.page_id
        update = st.session_state.page_update
        with header.container():
            header_data = Header(body)
        #with body.container():
        #    body_data = Pages(page_id)
        with header_data.tab1:
            body_data = Pages(1)
        with header_data.tab2:
            body_data = Pages(2)
        with header_data.tab3:
            body_data = Pages(3)
        with header_data.tab4:
            body_data = Pages(4)
        if update == 1:
            body.empty()
        else:
            st.stop()
    

if __name__ == "__main__":
    main()
    