import streamlit as st
from src.components.footer import footer_home
from src.components.header import header_home
from src.ui.base_layout import style_base_layout, style_background_home, style_home_portal_cards


def home_screen():

    login_param = st.query_params.get("login")
    if login_param in ("student", "teacher"):
        st.session_state["login_type"] = login_param
        st.query_params.clear()
        st.rerun()

    header_home()

    style_background_home()
    style_base_layout()
    style_home_portal_cards()

    st.markdown("""
        <section class="portal-grid">
            <article class="portal-card">
                <h2>I'm<br>Student</h2>
                <img src="https://i.ibb.co/844D9Lrt/mascot-student.png" alt="Student mascot">
                <a href="?login=student" target="_self">
                    Student Portal
                    <span class="material-symbols-rounded" aria-hidden="true">arrow_outward</span>
                </a>
            </article>
            <article class="portal-card">
                <h2>I'm<br>Teacher</h2>
                <img src="https://i.ibb.co/CsmQQV6X/mascot-prof.png" alt="Teacher mascot">
                <a href="?login=teacher" target="_self">
                    Teacher Portal
                    <span class="material-symbols-rounded" aria-hidden="true">arrow_outward</span>
                </a>
            </article>
        </section>
    """, unsafe_allow_html=True)

    footer_home()
