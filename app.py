import streamlit as st


with st.form(key ='Form1'):
    with st.sidebar:
        name = st.text_input("NAME","ENTER")    
        age = st.text_input("AGE") 
        dur = st.text_input("HOW DAYS DID YOUR LAST PERIOD LAST?") 
        date= st.text_input("HOW LONG SINCE YOUR LAST PERIOD?") 
        AB = st.radio('Do you suffer from Abdominal cramps?',('NO','Yes'))
        HS = st.radio('Do you suffer from Headaches?', ('NO','Yes'))
        N = st.radio('Do you suffer from Nausea?', ('NO','Yes'))
        C= st.radio( 'Do you suffer from Constipation?', ('NO','Yes'))
        B= st.radio( 'Do you suffer from Bloating?', ('NO','Yes'))
        M= st.radio('Do you suffer from Moodswings?', ('NO','Yes'))
        D= st.radio('Do you suffer from Stress, anxiety and irregular sleep?', ('NO','Yes'))
        PMS = st.radio('Do you suffer from PMS?', ('NO','Yes'))
        exc = st.radio('Have you performed any excercises during your last period?', ('NO','Yes'))
        dis = st.radio('ANY DISCOMFORT DURING YOUR LAST PERIOD?', ('NO','Yes'))
        BP = st.radio('DO YOU HAVE BACK PAIN?', ('NO','Yes'))
        submitted1 = st.form_submit_button(label = 'Submit')
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://ak3.picdn.net/shutterstock/videos/11437253/thumb/1.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
from PIL import Image
image = Image.open('logo.png')
st.image(image, caption='')
if (name!="ENTER"):
    st.write('HELLO',name,'(✿◠‿◠) ')
    st.title('GENERAL EXCERCISES')
    st.header("Excercise Do's")
    st.write("""🎀Cardio""")
    st.write("""🎀walking""")
    st.header("Exercise Don'ts")
    st.write("""🎀Intense cardio vascular workouts""")
    st.write("""🎀Tnverted yoga poses""")
    st.title('FOOD&DRINKS INTAKE')
    st.header("Food Don'ts")
    st.write("""🎀broccoli""")
    st.write("""🎀cabbage""")
    st.write("""🎀beans""")
    st.write("""🎀cauliflower""")
    st.write("""🎀lentils(limit)""")
    st.write("""🎀mushrooms""")
    st.write("""🎀onions""")
    st.write("""🎀peas""")
    st.write("""🎀whole-grain foods(limit)""")
    st.write("""🎀Salt""")
    st.write("""🎀Sugar""")
    st.write("""🎀Coffee""")
    st.write("""🎀Alcohol""")
    st.write("""🎀Spicy foods""")
    st.write("""🎀Red meat""")
    st.header("STRONG FOODS 💪")
    st.write("""🎀yogurt""")
    st.write("""🎀tofu""")
    st.write("""🎀chicken""")
    st.header("SNACKS")
    st.write("""🎀banana""")
    st.write("""🎀popcorn""")
    


if(AB=='Yes'):
    st.header("For Abdonimal cramps")
    st.write("""🎀Cruciferous vegetables""")
    st.write("""🎀Turmeric""")
    st.write("""🎀Dark chocolate""")
    st.write("""🎀Nuts""")
    st.write("""🎀Salmon""")
    st.write("""🎀Peppermint tea""")
    st.write("""🎀Chamomile tea""")
if(HS =='Yes'):
    st.header("For Headaches")
    st.write("""Water-rich foods-""")
    st.write("""🎀cucumbers""")
    st.write("""🎀watermelon""")
if(N =='Yes'):
    st.header("For Nausea")
    st.write("""🎀Ginger""")
    st.write("""🎀Citrus""")
    st.write("""🎀Peppermint tea""")
if( C=='Yes'):
    st.header("For Constipation")
    st.write("""🎀Whole grains""")
    st.write("""🎀Seeds(Flax seeds)""")
if( B=='Yes'):
    st.header("For Bloating")
    st.write("""🎀citrus""")
if( M=='Yes'):
    st.header("For Mood swings")
    st.write("""🎀Fish""")
    st.write("""🎀Dark chocolate""")
    st.write("""🎀citrus""")
if( D=='Yes'):
    st.header("For Stress, anxiety and irregular sleep")
    st.write("""🎀Cruciferous vegetables-calcium and magnesium""")
if( PMS=='Yes'):
    st.header("FOR PMS")
    st.subheader("FOOD INTAKE")
    st.write("""🎀Oatmeal""")
    st.write("""🎀Citrus""")
    st.subheader("EXCERCISES")
    st.write("""Yoga-""")
    st.write("""🎀bridge pose""")
    st.write("""🎀bound angle pose""")
    st.write("""🎀dolphin pose""")
    st.write("""🎀legs up the wall pose""")
    st.write("""🎀lotus pose""")
    st.write("""🎀Camel pose""")
if (BP=='Yes'):
    st.header("FOR BACK PAIN")
    st.subheader("Exercise")
    st.write("""🎀Pilates""")  


