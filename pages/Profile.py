from pathlib import Path

import streamlit as st
from PIL import Image

st.set_page_config(page_title="Profile",
                   page_icon='./images/profile.png')

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / ".." /  "styles" / "main.css"
resume_file = current_dir / ".." / "assets" / "cv.pdf"
profile_pic = current_dir / ".." / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Profile"
PAGE_ICON = ":wave:"
NAME = "Fauzi Taufik Hidayat"
DESCRIPTION = """
Informatics Engineering Student At Tanri Abeng University.
"""
EMAIL = "fauzi.taufik@student.tau.ac.id"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/fauzi-taufik-35b3b6195/",
}

# Load CSS, PDF & Profile PIC
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EDUCATION ---
st.write('\n')
st.subheader("EDUCATION")
st.write(
    """
- ✔️ Tanri Abeng University - Informatics Engineering - 2019 s.d present
- ✔️ SMAK DITKESAD  - Health Analyst - 2013 s.d 2016
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Administration Staff | Suku Badan Perencanaan Pembangunan Kabupaten Administrasi Kepulauan Seribu**")
st.write("January 2021 - Present")
st.write(
    """
- ► Establish cooperative relationships with vendors
- ► Checking vendor invoices
- ► Make letters for correspondence needs
- ► Help the treasurer do his job
- ► Make employee attendance schedule
- ► Verify employee absences
- ► As an operator to input the system
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**General Support Officer | PT. Sriwijaya Air**")
st.write("August 2019 - July 2020")
st.write(
    """
- ► Establish cooperative relationships with vendors
- ► Make reports in and out of warehouse goods
- ► Checking vendor invoices
- ► Serving employees who make requests for goods such as stamps, shoes, raincoats and others.
- ► Make letters for correspondence needs
- ► Making Purchase Requests
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Electircal Engineering | PT. Sriwijaya Air**")
st.write("August 2018 - July 2019")
st.write(
    """
- ► Performing electrical maintenance in the Sriwijaya Air office in the Soekarno Hatta Airport Terminal 2F area
- ► Performing AC maintenance services
- ► Make daily reports
"""
)


# --- Certificate ---
st.write('\n')
st.subheader("CERTIFICATE")
st.write(
    """
- ► Artificial Intelligence Associate - Logical Operations
- ► Database Progamming With SQL - Oracle
- ► Data Scientist - Digital Talent Scholarship
- ► Internet Of Things (IOT) - Digital Talent Scholarship
- ► Junior Mobile Progammer - Digital Talent Scholarship
"""
)
