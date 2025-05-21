import streamlit as st

# Pages Setup

about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

project_1_page = st.Page(
    page="views/Colour-Palatte-Generator.py",
    title="Color Palatte Generator",
    icon=":material/chat:",
)

project_2_page = st.Page(
    page="views/Unit-Converter.py",
    title="Unit Converter",
    icon=":material/chat:",
)

project_3_page = st.Page(
    page="views/Possword-Strenght-Meter.py",
    title="Possword Strenght Meter",
    icon=":material/chat:",
)

project_4_page = st.Page(
    page="views/Personal-Library-Manager.py",
    title="Personal Library Manager",
    icon=":material/chat:",
)


# Navigation Setup

pg = st.navigation(
    {
        "info" : [about_page],
        "projects" : [project_1_page,project_2_page,project_3_page,project_4_page]
    }
)

st.logo("assets/logo.png")
st.sidebar.text("Made By Hamza Nasir.")



pg.run()