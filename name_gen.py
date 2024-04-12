import random
import streamlit as st

st.title("Let's generate you a number:")

if st.button("Click me!"):
        k = random.randint(1,15)
        st.write(k)
else:
    st.write("Waiting for you to click the button")
    
st.text('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀  ___
　　　　　／＞　　フ
　　　　　| 　^　 ^ l
　 　　　／` ミ＿xノ
　　 　 /　　　 　 |
　　　 /　 ヽ　　 ﾉ
　 　 │　　|　|　|
　／￣|　　 |　|　|
　| (￣ヽ＿_ヽ_)__)
　＼二つ                                                                                                                                                       
''')
