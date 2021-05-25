#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_cell_magic('writefile', 'app.py', ' \nimport pickle\nimport streamlit as st\n\n# loading the trained model\npickle_in = open(\'model_rf.pkl\', \'rb\') \nclassifier = pickle.load(pickle_in)\n \n@st.cache()\n  \n# defining the function which will make the prediction using the data which the user inputs \ndef prediction(Review):   \n \n    # Pre-processing user input    \n    Review = tfidf.transform(Review)\n \n    # Making predictions \n    prediction = classifier.predict(Review)\n     \n    if prediction == 0:\n        pred = \'Negative Review\'\n    else:\n        pred = \'Positive Review\'\n    return pred\n      \n# this is the main function in which we define our webpage  \ndef main():       \n    # front end elements of the web page \n    html_temp = """ \n    <div style ="background-color:yellow;padding:13px"> \n    <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> \n    </div> \n    """\n      \n    # display the front end aspect\n    st.markdown(html_temp, unsafe_allow_html = True) \n      \n    # following lines create boxes in which user can enter data required to make prediction \n    Review = st.input(\'Type Review Here\')\n    result =""\n      \n    # when \'Predict\' is clicked, make the prediction and store it \n    if st.button("Predict"): \n        result = prediction(Review) \n        st.success(\'Your Review is {}\'.format(result))\n        print(LoanAmount)\n     \nif __name__==\'__main__\': \n    main()')

