import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))


st.title("SMS Spam Classification Application")
st.write("This is a Machine Learning Projrct to classify SMS as spam or ham")

user_input = st.text_area("Enter the SMS to classify", height=150)

if st.button("Classify") :
    if user_input:
        data = [user_input]
        vect = cv.transform(data).toarray()
        result = model.predict(vect)
        if result[0] == 0:
            st.success("This is not a Spam SMS")
        else:
            st.error("This is a Spam SMS")
    else:
        st.warning("Please enter the SMS to classify")        