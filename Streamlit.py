import requests
import streamlit as st
from streamlit_lottie import st_lottie 
from PIL import Image

# Page Title
st.set_page_config(page_title = "Shopping List", page_icon = ":shopping_trolley:", layout = "wide")


# Function to access JSON data of the lottie files
def load_lottieurl(url):
	r = requests.get(url)
	#If the request is successful it will return 200, otherwise nothing
	if r.status_code != 200:
		return None
	return r.json()

# Use Local CSS
def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

# Load Assets
lottie_trolley = load_lottieurl(
	"https://lottie.host/114aa104-9810-4516-a75b-9f60e56c01f7/KE7gS2r5PP.json"
	)
img_lady_shopping = Image.open("assets/ai shopping lady.jpg")

# Header Section
with st.container():
	st.title("Title - Welcome to your shopping list! :wave:")
	st.subheader("Sub header - Let's add some stuff to your list!")
	st.write("This is the write box")#

# Next Section

with st.container():
	# This adds a divider into the page
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("Header - Your List!")
		# This adds a space
		st.write('##')
		st.write(
			'''
			What shall we put in your trolley?
			- Milk
			- Fruit
			- Some beer
			'''
			)
	with right_column:
		st_lottie(lottie_trolley, key = "Shopping Trolley")	

with st.container():
	st.write("---")
	st.header("Some more stuff down here")
	st.write("##")
	# The column bit tells it that the second column should be twice as wide as the first
	image_column, text_column = st.columns((1,2))
	with image_column:
		# Insert image
		st.image(img_lady_shopping)
	with text_column:
		st.subheader("I am using Lottie Animations!")
		st.write("[Check out Lottie here!](https://lottiefiles.com/)")

# Putting in a contact form!
with st.container():
	st.write("---")
	st.header("Get in Touch!")
	st.write("##")

	# See formsubmit.co for this!
	contact_form = """
	<form action="https://formsubmit.co/c4035047462462ba12743863626eb1a6" method="POST">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
	</form>
	"""
left_column, right_column = st.columns(2)
with left_column:
	st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
	st.empty()


