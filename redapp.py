import streamlit as st
import pandas as pd
import numpy as np
import time


#st.title("This is Red's App")
st.markdown("<h1 style='text-align: center;'>Ingénieur système</h1>", unsafe_allow_html=True)

st.image("images/red.jpg", width=200)
st.write("""
        ### Redouane NOUAF
        Date de naissance: 3 Fevrier 1982 
        Mobilité nationale et internationale 
        Permis de conduire catégorie B
        """)

#st.markdown('<h1 style="float: left;">Kubernetes</h1>', unsafe_allow_html=True)

st.write("Compétences")
st.write(pd.DataFrame({
    'Compétence': ["Devops", "Linux", "Virtualisation", "Scripting","Conteneurisation","Gestion des configurations"],
    'Niveau/5': ['***', '*****', '***', '****', '*****', '****']
}))
df = pd.DataFrame({
        'Compétence': ["Devops", "Linux", "Virtualisation", "Scripting","Conteneurisation","Gestion des configurations"],
        'Niveau/5': ['***', '*****', '***', '****', '*****', '****']
        })
df
option = st.selectbox(
    'Selectionnez une compétence',
     df['Compétence'])
'You selected: ', option
left_column, right_column = st.columns(2)
pressed = left_column.button('3fett hna')
if pressed:
    right_column.write("Sriwriw!")
expander = st.expander("FAQ")
expander.write("explanations explanations explanations explanations explanations explanations explanations... \n explanations explanations explanations explanations....")
'Starting a long computation...'
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)
'...Saaaafi Saaaaliiina !'
