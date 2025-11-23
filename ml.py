import streamlit as st
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title='Marks Predictor')
st.title('Students Mark Predictor')
st.write('Enter The Number Of Hours (1-10) Studied In A Day And **Click Predict** To See The Predicted Marks')

# Load the model
def load_model(path:str='SLR.pkl'):
    with open(path,'rb') as f:
        model = pickle.load(f)
    return model

try:
    model = load_model('SLR.pkl')
except Exception as e:
    st.write(e)
    st.stop()



hours = st.number_input(label='Hours_Studied',
                         min_value=1.0,
                         max_value=10.0,
                         value=1.0,
                         step=0.1,
                         format='%.1f')

# Predict button
if st.button('Predict Button'):
    try:
        X = np.array([[hours]])
        prediction = model.predict(X)
        predicted_marks = prediction[0]
        st.success(f'Predicted Marks: {predicted_marks}')
        st.balloons()
    except Exception as e:
        st.error(f'Prediction Failed: {e}')