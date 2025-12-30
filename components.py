import streamlit as st


def render_chat():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        role = msg["role"]
        content = msg["content"]

        if role == "user":
            st.markdown(
                f"""
                <div style="
                    background:#2563eb;
                    color:white;
                    padding:12px 16px;
                    border-radius:14px;
                    max-width:75%;
                    margin-left:auto;
                    margin-bottom:10px;
                ">
                    {content}
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style="
                    background:#1f2937;
                    color:#e5e7eb;
                    padding:12px 16px;
                    border-radius:14px;
                    max-width:75%;
                    margin-right:auto;
                    margin-bottom:10px;
                ">
                    {content}
                </div>
                """,
                unsafe_allow_html=True
            )


def chat_input():
    user_text = st.text_area(
        "",
        placeholder="Ask anything or describe your goal...",
        key="chat_input",
        height=60
    )

    send = st.button("🚀 Send", use_container_width=True)

    if send and user_text.strip():
        return user_text.strip()

    return None
