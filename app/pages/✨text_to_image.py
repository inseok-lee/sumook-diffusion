import typing as T
import util as st_util
import streamlit as st


def main():
    st.set_page_config(page_title="text to image", page_icon="✨")

    st.markdown("# Text To Image")
    st.sidebar.header(" Text To Image")
    st.write(
        """This demo Generate Sumook Painting Image from text prompts. Enjoy!"""
    )   

    with st.expander("Help", False):
        st.write(
        """
        This tool runs diffusion in simplest text to image...
        """
        )

    device = st_util.select_device(st.sidebar)
    model = st_util.select_checkpoint(st.sidebar)

    with st.form("Inputs"):
        prompt = st.text_input(label="Prompt(You can type Korean into the prompt)", value='잔잔한 강 뒤에 있는 높은 산')

        row = st.columns(2)

        seed = T.cast(
            int,
            row[0].number_input(
                "Seed",
                value=46,
                help="Change this to generate different variations",
            ),
        )

        submit_button = st.form_submit_button("Start", type="primary")
        if submit_button:
            st_util.inference_model(model, device, prompt, seed)


if __name__ == "__main__":
    main()