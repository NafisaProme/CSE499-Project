import streamlit as st
import pickle
import numpy as np
import sklearn

# setting the page configuration 
st.set_page_config(page_title="Disease Detection", page_icon="", layout="wide")
st.title("Disease Detection")

# importing the model and the pickle dataset 
symptoms = pickle.load(open("symptoms.pkl", "rb"))
pipe = pickle.load(open("model.pkl", "rb"))
symptoms_list = symptoms.to_dict(orient='records')

# Dynamic selection box 
if 'selectbox_data' not in st.session_state:
    st.session_state.selectbox_data = {'count': 0, 'values': []}

# Function to add a selectbox
def add_selectbox():
    st.session_state.selectbox_data['count'] += 1
    st.session_state.selectbox_data['values'].append(f"Selectbox {st.session_state.selectbox_data['count']}")

# Function to remove a selectbox
def remove_selectbox(selectbox_index):
    st.session_state.selectbox_data['count'] -= 1
    st.session_state.selectbox_data['values'].pop(selectbox_index)

# Create a "plus" button to add a selectbox
if st.button("Add Symptom"):
    add_selectbox()

# Create selectboxes
symptoms_map = {symptom['Symptoms']: 0 for symptom in symptoms_list}
for i, selectbox_value in enumerate(st.session_state.selectbox_data['values']):
    # keeping track of the symptoms
    disease_name = st.selectbox(f"Symptom {i + 1}", symptoms["Symptoms"].unique())
    symptoms_map[disease_name] = 1
    if st.button(f"Remove Symptom {i + 1}"):
        remove_selectbox(i)

user_input = []
for data in symptoms:
    user_input.append(data)
    # user_input.append(symptoms_map[data])

if st.button("Get Disease"):
    print(len(user_input))
    
# cnt = st.session_state.selectbox_data['count']

# headings = ['Brand', 'Processor Brand','Processor Model','Generation','RAM','RAM Type','Storage Capacity','Battery Capacity']
# max_len = len(headings)

# ind = 0
# for row in range(0, 5):
#     if ind == max_len:
#         break
#     taken = st.columns(4)
    
#     for col in range(0, 3):
#         if ind == max_len:
#             break

#         with taken[col]:
#             # storing the results in the heading_map
#             heading_map[headings[ind]] = st.selectbox(headings[ind], df[headings[ind]].unique())
#             ind += 1

# # collecting the user input from the map 
# user_input = []
# for data in range(len(heading_map)):
#     user_input.append(heading_map[headings[data]])

# # predict the price only if the button is pressed
# if st.button("Predict Price"):

#     # passing the user input as queries 
#     query = np.array(user_input)
#     query = query.reshape(1, 8)

#     st.title("The Predicted Price of Laptop = Taka " + str(int(np.exp(pipe.predict(query)[0]))))