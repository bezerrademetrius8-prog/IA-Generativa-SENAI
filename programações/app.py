import streamlit as st


st.title('TITULO H1')


n1  = st.number_input('numero:', )
n2  = st.number_input('numero:', value = 0.0)


if st.button('Soma'):
    calcular   =  n1  + n2 
    st.success(calcular)
elif st.button('subtração'):    
    calcular   =  n1  - n2 
    st.success(calcular)    
elif st.button('Divisão'):    
    calcular   =  n1  / n2 
    st.success(calcular)       0
elif st.button('Multiplicação'):    
    calcular   =  n1  * n2 
    st.success(calcular)      