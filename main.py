import base64

import streamlit as st

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local("photo1686134773.jpeg")



st.balloons()



st.header("Проект Ксении")
right_quest = 0
question1 = st.radio("Какой самый большой орган ?", ('тонкая кишка', 'кожа', 'печень', 'Ни один ответ не верен'))
if question1 == 'кожа':
    st.write('Ответ верен')
    right_quest += 1
else:
    st.write('Ответ неверен')

question2 = st.radio("От чего зависит цвет глаз ? ",
    ('гинетика ', 'рандом ', 'нет точного ответа '    'Ни один ответ не верен'))
if question2 == 'гинетика ':
    st.write('Ответ верен')
    right_quest += 1
else:
    st.write('Ответ неверен')

st.write('Правильных ответов:', right_quest)


question3 = st.radio("При смешании каких цветов не получиться зеленые глаза? ",
    ('голубой-коричневый', 'зеленый-голубой', 'карий-зеленый', 'нет точного ответа'))
if question3 == 'голубой-коричневый':
    st.write('Ответ верен')
    right_quest += 1
else:
    st.write('Ответ неверен')

st.write('Правильных ответов:', right_quest)
question4 = st.radio("сколько цветов видит человек?",
    ('50k', '500k', '1 мил'))
if question4 == '1 мил  ':
    st.write('Ответ верен')
    right_quest += 1
else:
    st.write('Ответ неверен')

st.write('Правильных ответов:', right_quest)