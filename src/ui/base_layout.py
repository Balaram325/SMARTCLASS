import streamlit as st
# from src.ui.styles import 

def style_background_home():

    st.markdown("""
    
        <style>
            .stApp{
                background: #5865F2 !important;
            }
        </style>
    
    """, unsafe_allow_html=True)


def style_home_portal_cards():

    st.markdown("""

        <style>
            @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,400,0,0');

            .portal-grid{
                display: flex !important;
                flex-direction: row !important;
                flex-wrap: nowrap !important;
                gap: 3.25rem !important;
                justify-content: center !important;
                align-items: stretch !important;
                margin: 2.2rem auto 0 auto !important;
                width: min(100%, 56rem) !important;
            }

            .portal-card{
                box-sizing: border-box !important;
                flex: 0 1 21rem !important;
                width: 21rem !important;
                background: #E9ECFF !important;
                border-radius: 4.5rem !important;
                min-height: 20.5rem !important;
                padding: 2.45rem 2.4rem 2.2rem 2.4rem !important;
                box-shadow: 0 1.5rem 3rem rgba(26, 31, 76, 0.12);
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
                justify-content: center !important;
            }

            .portal-card h2{
                width: 100% !important;
                color: #202333 !important;
                font-size: 2.3rem !important;
                text-align: left !important;
                line-height: 0.86 !important;
                margin-bottom: 0.35rem !important;
            }

            .portal-card img{
                display: block !important;
                width: 8.9rem !important;
                height: 8.9rem !important;
                object-fit: contain !important;
                margin: 0.15rem auto 0.6rem auto !important;
            }

            .portal-card a{
                display: inline-flex !important;
                align-items: center !important;
                justify-content: center !important;
                gap: 0.35rem !important;
                min-width: 10.5rem !important;
                min-height: 2.8rem !important;
                padding: 0 1.15rem !important;
                border-radius: 1.5rem !important;
                background: #5865F2 !important;
                color: #ffffff !important;
                font-family: 'Outfit', sans-serif !important;
                font-size: 0.95rem !important;
                font-weight: 700 !important;
                text-decoration: none !important;
                box-shadow: 0 0.55rem 1.1rem rgba(88, 101, 242, 0.22);
                transition: transform 0.25s ease-in-out !important;
            }

            .portal-card a:hover{
                transform: scale(1.05);
            }

            .portal-card .material-symbols-rounded{
                font-size: 1.15rem !important;
                line-height: 1 !important;
            }

            @media (max-width: 640px){
                .portal-grid{
                    flex-direction: column !important;
                    gap: 1.4rem !important;
                    width: min(100%, 24rem) !important;
                }

                .portal-card{
                    flex: 1 1 auto !important;
                    width: 100% !important;
                    border-radius: 3.25rem !important;
                    min-height: 18rem !important;
                    padding: 2rem 1.7rem !important;
                }

                .portal-card h2{
                    font-size: 1.9rem !important;
                }
            }
        </style>

    """, unsafe_allow_html=True)



def style_background_dashboard():

    st.markdown("""
    
        <style>
                

            .stApp{
                background: #E0E3FF !important;
                }
                
            div[data-testid="column"]{
                background-color:#E0E3FF !important;
                padding:2.5rem !important;
                border-radius: 5rem !important;
                }

            h2,
            h3{
                color: #202333 !important;
            }

            div[data-testid="stWidgetLabel"] label,
            div[data-testid="stWidgetLabel"] p,
            div[data-testid="stTextInput"] label,
            div[data-testid="stTextInput"] label p,
            div[data-testid="stTextInput"] label div,
            div[data-testid="stCameraInput"] label,
            div[data-testid="stCameraInput"] label p,
            div[data-testid="stCameraInput"] label div,
            div[data-testid="stAudioInput"] label,
            div[data-testid="stAudioInput"] label p,
            div[data-testid="stAudioInput"] label div{
                color: #202333 !important;
            }

            div[data-baseweb="input"]{
                background-color: #ffffff !important;
            }

            div[data-baseweb="input"] input{
                background-color: #ffffff !important;
                color: #202333 !important;
                caret-color: #202333 !important;
            }

            div[data-baseweb="input"] input::placeholder{
                color: #5F6475 !important;
                opacity: 1 !important;
            }

            div[data-testid="stDialog"]{
                color: #ffffff !important;
            }

            div[data-testid="stDialog"] h1,
            div[data-testid="stDialog"] h2,
            div[data-testid="stDialog"] h3,
            div[data-testid="stDialog"] p,
            div[data-testid="stDialog"] span,
            div[data-testid="stDialog"] label,
            div[data-testid="stDialog"] div[data-testid="stMarkdownContainer"],
            div[data-testid="stDialog"] div[data-testid="stWidgetLabel"] p,
            div[data-testid="stDialog"] div[data-testid="stTextInput"] label p{
                color: #ffffff !important;
            }

            div[data-testid="stDialog"] div[data-testid="column"]{
                background-color: transparent !important;
                padding: 0 !important;
                border-radius: 0 !important;
            }

            div[data-testid="stDialog"] div[data-testid="stCodeBlock"],
            div[data-testid="stDialog"] pre{
                background-color: #171C28 !important;
                color: #ffffff !important;
                border-radius: 0.75rem !important;
            }

            div[data-testid="stDialog"] div[data-testid="stCaptionContainer"] p{
                color: #D8DCF5 !important;
            }

            div[data-testid="stDialog"] button[aria-label="Close"]{
                min-width: 5rem !important;
                height: 2.2rem !important;
                padding: 0 1rem !important;
                border-radius: 1.5rem !important;
                background: #5865F2 !important;
                color: #ffffff !important;
                font-family: 'Outfit', sans-serif !important;
                font-size: 0 !important;
                font-weight: 800 !important;
                line-height: 1 !important;
                display: inline-flex !important;
                align-items: center !important;
                justify-content: center !important;
                gap: 0.35rem !important;
            }

            div[data-testid="stDialog"] button[aria-label="Close"]::before{
                content: "Back" !important;
                color: #ffffff !important;
                font-size: 0.9rem !important;
            }

            div[data-testid="stDialog"] button[aria-label="Close"] svg{
                display: none !important;
            }

            hr{
                border: none !important;
                border-top: 2px solid rgba(32, 35, 51, 0.18) !important;
                margin: 1.9rem auto 1.6rem auto !important;
            }
        </style>
    
    """, unsafe_allow_html=True)
    st.markdown("""
        <style>
        /* Make spinner/status text dark */
        [data-testid="stStatus"] * ,
        [data-testid="stSpinner"] * {
            color: #202333 !important;
        }
        </style>
        """, unsafe_allow_html=True)




def style_base_layout():

    st.markdown("""
    
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');



            /* Hide Top Bar of streamlit*/
                #MainMenu, footer, header{
                    visibility: hidden;
                }
                .block-container{
                    padding-top:1.5rem !important;
                }
                h1{
                    font-family: 'Climate Crisis', sans-serif !important;
                    font-size: 3.5rem !important;
                    line-height: 1.1 !important;
                    margin-bottom: 0rem !important;
                    
                }
                h2{
                    font-family: 'Climate Crisis', sans-serif !important;
                    font-size: 2rem !important;
                    line-height: 0.9 !important;
                    margin-bottom: 0rem !important;
                }

                h3, h4, p {
                    font-family: 'Outfit', sans-serif;

                }


                button{
                    border-radius: 1.5rem !important;
                    background: #5865F2 !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }


                button[kind="secondary"]{
                    border-radius: 1.5rem !important;
                    background: #EB459E !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button[kind="tertiary"]{
                    border-radius: 1.5rem !important;
                    background: black !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button:hover{
                    transform:scale(1.05)
                }

                .home-footer{
                    visibility: visible !important;
                    margin: 2.5rem auto 0 auto !important;
                    padding: 1rem 0 0.5rem 0 !important;
                    text-align: center !important;
                }

                .home-footer p{
                    color: #202333 !important;
                    font-family: 'Outfit', sans-serif !important;
                    font-size: 0.95rem !important;
                    font-weight: 600 !important;
                    margin: 0 !important;
                }





        </style>
    
    """, unsafe_allow_html=True)
