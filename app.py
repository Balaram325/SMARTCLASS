import streamlit as st
from src.screen.home_screen import home_screen
from src.screen.student_screen import student_screen
from src.screen.teacher_screen import teacher_screen
from src.components.dialog_auto_enroll import auto_enroll_dialog
# from src.ui.styles import apply_all_styles

# apply_all_styles()


def main():
    st.set_page_config(
        page_title='SmartClass AI',
        page_icon='https://i.ibb.co/YTYGn5qV/logo.png'
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None
    
    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()
        
        case 'student':
            student_screen()
        
        case None:
            home_screen()

    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()

        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)
main()






# def main():
#     st.header("This is a header")
#######    name = st.text_input("Enter your name")

#     col1, col2 = st.columns(2, gap="xsmall")
#   ####  with col1:
#######         if st.button("Hi", type = "primary", key = "def1", width="content"):
####             ###print("Hi", name)

#     with col2:
#         if st.button("Bye", type = "primary", key = "def2", width="content"):
#             print("bye", name)

    # st.markdown("""
    #             # Markdown syntax guide

    #             ## Headers

    #             # This is a Heading h1
    #             ## This is a Heading h2
    #             ###### This is a Heading h6

    #             ## Emphasis

    #             *This text will be italic*  
    #             _This will also be italic_

    #             **This text will be bold**  
    #             __This will also be bold__

    #             _You **can** combine them_

    #             ## Lists

    #             ### Unordered

    #             * Item 1
    #             * Item 2
    #             * Item 2a
    #             * Item 2b
    #                 * Item 3a
    #                 * Item 3b

    #             ### Ordered

    #             1. Item 1
    #             2. Item 2
    #             3. Item 3
    #                 1. Item 3a
    #                 2. Item 3b

    #             ## Images

    #             ![This is an alt text.](/image/Markdown-mark.svg "This is a sample image.")

    #             ## Links

    #             You may be using [Markdown Live Preview](https://markdownlivepreview.com/).

    #             ## Blockquotes

    #             > Markdown is a lightweight markup language with plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz.
    #             >
    #             >> Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.

    #             ## Tables

    #             | Left columns  | Right columns |
    #             | ------------- |:-------------:|
    #             | left foo      | right foo     |
    #             | left bar      | right bar     |
    #             | left baz      | right baz     |

    #             ## Blocks of code

    #             ```
    #             let message = 'Hello world';
    #             alert(message);
    #             ```

    #             ## Mermaid diagrams
    #             ```mermaid
    #             graph TD
    #             A[Start] --> B{Decision}
    #             B -->|Yes| C[Finish]
    #             B -->|No| D[Alternate]
    #             ```

    #             ## Inline code

    #             This web site is using `markedjs/marked`.
    #             """, unsafe_allow_html=True)


#     st.markdown("""
#         <div>
#             <img src='https://media.istockphoto.com/id/1588288383/photo/back-view-of-student-raising-his-hand-to-answer-teachers-question-during-education-training.jpg?s=612x612&w=0&k=20&c=ZSyPrLqe6WdE81WXiESD5AqIVw1a7hKv85UI5I-Vwco=' />
#             <h1> Snap Class </h1>
#         </div>
#         <style>
#                 button{
#                     background:green !important;
#                 }
#         </style>
#     """, unsafe_allow_html=True)

# main()