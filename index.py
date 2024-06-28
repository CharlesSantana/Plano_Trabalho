#https://phylos.net/tag/pandas
#https://medium.com/horadecodar/gr%C3%A1ficos-de-barra-com-matplotlib-85628bfc4351
#https://medium.com/@coutinholps/dashbohttps://medium.com/@coutinholps/dashboard-r%C3%A1pido-com-python-e-streamlit-6aa7df1fda49ard-r%C3%A1pido-com-python-e-streamlit-6aa7df1fda49
#https://medium.com/@coutinholps/dashboard-r%C3%A1pido-com-python-e-streamlit-6aa7df1fda49

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.io as pio
import locale
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


#locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

#Layout e Apresentacao
st.set_page_config(page_title='Dataset Olist', layout='wide')
#st.title("Trabalho Dataset Olist")

#Sidebar - Configuracao
st.sidebar.title('DashBoard Olist')
st.sidebar.info('Grupo Data4')
st.sidebar.image('data:image/png;base64,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',width=100)

#Conexao com o Dataset
#df = pd.read_csv("/home/master/projetos/datasets/dataset_olist.csv")

url = 'https://drive.google.com/file/d/1Ls5oSgYzL6NoFn0k1jrP_QCB-p-42bfC/view'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df = pd.read_csv(url)

