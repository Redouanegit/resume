import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(layout="wide") #,initial_sidebar_state="auto")
st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)

#st.title("This is Red's App")
st.markdown("<h1 style='text-align: center; font-size:50px; '>Ingénieur système</h1>", unsafe_allow_html=True)

st.write("     ")
st.write("     ")
st.write("     ")


st.image("images/red.jpg", width=200)
st.write("""
        # Redouane NOUAF
        E-mail: r.nouaf@gmail.com \n
        Date de naissance: 3 Fevrier 1982 \n
        Mobilité nationale et internationale \n
        Permis de conduire catégorie B
        """)

#st.markdown('<h1 style="float: left;">Kubernetes</h1>', unsafe_allow_html=True)

st.write("## Compétences")
df = pd.DataFrame({
        'Compétence': ["Devops", "Linux", "Virtualisation", "Scripting","Conteneurisation","Gestion des configurations"],
        'Technologies': ["git, Kubernes, Docker, jenkins, \n Ansible, Prometheus, Grafana, AWS ","Debian, Ubuntu, RedHat/CentOS","Virtualbox, Nutanix", "Python, Shell", "Docker, Kubernetes", "Ansible, Puppet"],
        'Niveau/5': ['***', '*****', '***', '****', '*****', '****']
        })
#dfStyler = df.style.set_properties(subset=['Compétence'],**{'text-align': 'right'})
#dfStyler.set_table_styles([dict(selector='th', props=[('text-align', 'right')])])
df.style.set_properties(**{'text-align': 'left'}).set_table_styles([ dict(selector='th', props=[('text-align', 'left')] ) ])

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
df
option = st.selectbox(
    'Selectionnez une compétence',
     df['Compétence'])
'You selected: ', option
left_column, right_column = st.columns(2)
pressed = left_column.button('3fett hna')
if pressed:
    right_column.write("Sriwriw!")
expander = st.expander(option)
expander.write("explanations explanations explanations explanations explanations explanations explanations... \n explanations explanations explanations explanations....")
'Starting a long computation...'
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.05)
'...Saaaafi Saaaaliiina !'
