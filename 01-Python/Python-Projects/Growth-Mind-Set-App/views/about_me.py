import streamlit as st


from form.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()



col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/Profile.jpg" , width=230)
with col2:
    st.title("Hamza Nasir" , anchor=False)
    st.write(
        "A Fullstack Nextjs Developer,Passionate about learning Modern AI and Python, constantly exploring new advancements in the field. Ready to dive into Agentic AI to learn and build intelligent AI agents.oo"
    )
    if st.button("Contact Me"):
        show_contact_form()


st.write("\n")
st.subheader("Experience & Qualification", anchor=False)
st.write("""
    * Experienced in Next.js for building modern, scalable web applications.
    * Strong understanding of TypeScript.
    * Knowledgeable in Web3, Metaverse, and Generative AI technologies.
    * Expertise in Modern AI and Python development.
    * Hands-on experience with Next.js for full-stack web development.
    * Strong foundation in TypeScript and exam-based learning methodologies.
    * Completed multiple milestones in GIAIC (Governor House AI Initiative).
    * Continuously learning and expanding skills in Agentic AI and advanced AI concepts.
""")

st.write("\n")
st.subheader("Hard Skills", anchor=False)

st.write("""
    * Programming Languages: TypeScript, Python, JavaScript.
    * Frontend Development: Next.js, React, Tailwind CSS.
    * Backend Development: Node.js, Express.js.
    * AI & Data Science: Modern AI, Agentic AI, Pandas, NumPy.
    * Web Frameworks: Streamlit (for interactive Python apps).
    * State Management: Redux, Context API.
    * Database Management: MongoDB, Firebase.
    * Version Control: Git, GitHub.
    * Testing & Debugging: Jest, ESLint.
""")