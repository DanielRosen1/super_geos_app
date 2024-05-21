import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Welcome to the super geo app!
This application is designed to showcase the potential for multiple pages, each with different maps and functionalities. This template allows us to easily add our data and customize features in the future.
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
st.title("Lumenis Super Geo's app")

st.markdown(
    """
    This multipage app template demonstrates various interactive web apps possibillities for using geospatial data. 
    """
)

st.header("Instructions")

markdown = """
1. Click the icons on the left to select different pages.
2. play with the widgets on the sidebar to interact with the map. 

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
