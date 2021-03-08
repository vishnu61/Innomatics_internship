import pickle
from pickle import load
import streamlit as st

# loading the trained model
serial=load(open('pickle/rbf_pickle.pkl','rb'))
@st.cache()
# defining the function which will make the prediction using the data which the user inputs

def prediction(column1,column2):
    prediction =serial.predict([[column1,column2]])
    if prediction == 0:
        pred = "No :hourglass: "
    elif prediction == 1:
        pred = "Yes :white_check_mark: "
    else:
        pred=None
    return pred
# this is the main function in which we define our webpage
def main():
    html_temp = """
    <div style ="background-color:skyblue;padding:13px">
    <h1 style ="color:black;text-align:center;">Deployment using ML</h1>
    </div>
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)
    column1 = st.number_input('Enter value 1')
    st.write('The current number is ', column1)
    column2 = st.number_input('Enter value 2')
    st.write('The current number is ', column2)

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(column1,column2)
        st.success(result)

if __name__=='__main__':
    main()
