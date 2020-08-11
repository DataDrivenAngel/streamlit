### imports

import streamlit as st
from random import randint


st.title('test_application')

st.subheader('your random number is:')
st.write(randint(1,5))


if st.checkbox('Get me my lucky number'):
    st.subheader('Lucky Number')
    st.write(randint(1,5))