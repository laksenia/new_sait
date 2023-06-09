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

add_bg_from_local("bg2.jpeg")



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
    ('генетика ', 'рандом ', 'нет точного ответа '    'Ни один ответ не верен'))
if question2 == 'генетика ':
    st.write('Ответ верен')
    right_quest += 1
else:
    st.write('Ответ неверен')


question3 = st.radio("При смешании каких цветов не получиться зеленые глаза? ",
    ('голубой-коричневый', 'зеленый-голубой', 'карий-зеленый', 'нет точного ответа'))
if question3 == 'голубой-коричневый':
    st.write('Ответ верен')
    right_quest += 1
else:
    st.write('Ответ неверен')

question4 = st.radio("какую максимальную температуру выдерживае человек ?",
    ('59˚С', '170-180˚С', '130˚С'))
if question4 == '170-180˚С':
    st.write('Ответ верен')
    right_quest += 1
else:
    st.write('Ответ неверен')

question5 = st.radio("с какой скоростью чихает человек ?",
                     ('100 km/h', '190km/h', '160km/h'))
if question5 == '160km/h':
    st.write('Ответ верен')
    right_quest += 1
else:
    st.write('Ответ неверен')


question6 = st.radio("сколько весит кожа средниго мужчины ?",
                     ('9kg', '15kg', '5kg'))
if question6 == '5kg':
    st.write('Ответ верен')
    right_quest += 1
else:
    st.write('Ответ неверен')

question7 = st.radio("во сколько раз кость человека прочнее бетона ?",
                     ('x6', 'x10', 'x4'))
if question7 == 'x4':
    st.write('Ответ верен')
    right_quest += 1
else:
    st.write('Ответ неверен')
question8 = st.radio("какое количество запохов может помнить человек?",
                     ('70k', '150k', '50k'))
if question8 == '50k':
    st.write('Ответ верен')
    right_quest += 1
else:
    st.write('Ответ неверен')
question9 = st.radio("сколько km нервов в теле человека?",
                     ('140km',' 200km ', '72km'))
if question9 == '72km':
    st.write('Ответ верен')
    right_quest += 1
else:
    st.write('Ответ неверен')
question10 = st.radio("из скольки костей состоит череп человека  ?",
                     ('29','30', '47'))
if question10 == '29':
    st.write('Ответ верен')
    right_quest += 1
else:
    st.write('Ответ неверен')




st.write("Количество верных отвтов: ", right_quest)