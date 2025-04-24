 #streamlit
import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="★")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("welcome to your Growth Journey!")
st.write("Embrace Challenges: View obstacles as opportunities to learn rather than as setbacks.")

#quote section
st.header("💡 Today's Growth Mindset Quote")
st.write("Success is not final,failure is not fatal:it is the courage to continue that counts.- Winston Churchill")
st.header("🔧What,s Your Challenge Today")
user_input= st.text_input("Describe a Challenge you're facing:")

#condition
if user_input:(f"💪🏼 You're facing:{user_input}. Keep pushing forward towards you goal!")

else:
    st.warning("Tell us about your challenge to get started!")
    reflection = st.text_area("write your reflection here")

    if reflection:
        st.success(f"⭐Great insight! Your reflection:{reflection}")
    else:
         st.info("Reflecting on past experience help you grow! Share your difficulties")

#acheivements
st.header(f"🏆Celebrate Your Wins!")
acheivements = st.text_input("Share  something you've recently accomplished:")

if acheivements:
    st.success(f"⭐Amazing! Your achieved:{acheivements}")
else:
    st.info("Big or small, every acheivements counts!Share one now  👍")

#footer

st.write("- - -")
st.write("Keep believing in yourself. Growth is a journey, not a destination! ")
st.write("**⛔️ Created By Haseeb abbasi**")



