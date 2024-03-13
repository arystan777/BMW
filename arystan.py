import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="M5cs", page_icon="🥶", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = load_lottieurl("https://lottie.host/5ddc0ca2-0232-4746-9e5f-abe8129e5230/cqw38AEF9F.json")
img_lottie_animation = ("https://www.aspiringsupercarowners.com/wp-content/uploads/2021/01/bmw_m5_cs_6.jpg")
img_lottie_negr = ("https://i.ytimg.com/vi/5NCR_wWWE2Q/maxresdefault.jpg")
with st.container():
    st.subheader("Wsp, welcome to my very useful page 💯")
    st.title("I am a carspotter from Kazakhstan ")
    st.write("I just spot unique cars in my city. Moreover i meet the owners of the cars, and i love my hobby")
    st.write("[Here's the legendary M5cs>](https://www.aspiringsupercarowners.com/)")   

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("BMW")
        st.write("##")
        st.write(
            """
            Review
            """
        )
        st.write("[Youtube Channel >](https://www.youtube.com/watch?v=uxmQEMIkSvU)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("Info")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("BMW M5cs")
        st.write(
            """
            Under the carbon bonnet, everything points to motor racing: With 467 kW (635 hp) and 750 Nm of torque, 
            the M TwinPower Turbo 8-cylinder petrol engine accelerates the vehicle from 0 to 100 km/h in 3.0 seconds. 
            Thanks to two TwinScroll turbochargers, High-Precision Injection and Valvetronic fully variable valve control, 
            the 4.4-litre engine delivers energetic thrust even from low rpms, direct responsiveness and tremendous power.

            """
        )
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_negr)

    with text_column:
        st.subheader("BMW")
        st.write(
            """
            Get ready for the most powerful BMW M production model there has ever been: With the BMW M5 CS, 
            BMW M expands its model programme of the BMW M5 sedan for the first time in its history with an exclusive CS model.
            CS stands for Competition Sport: The BMW M5 CS delivers ground-breaking performance and motor sport genetics right down to the smallest detail. 
            With exclusive suspension, lightweight-construction and design components, 
            only available for this model, 
            it achieves a unique character in terms of performance and premium sports aspirations.

            """
        )


with st.container():
    st.write("---")
    st.header("By Arystan")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/arystan909@yahoo.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="your name" required>
        <input type="email" name="email" placeholder="your email" required>
        <textarea name="message" placeholder="Your message hear" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    lest_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()