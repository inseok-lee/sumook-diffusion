import streamlit as st


def main():
    st.set_page_config(
    page_title="Sumook Diffusion Playground",
    page_icon="✨",
    layout="wide",
    )

    st.write("# Sumook Diffusion Playground ✨")

    st.markdown(
    """
    한국 전통 수묵화 화풍별 제작 데이터로 학습한 Diffusion text-to-image 모델, 그리고 추론 예제.  
    **👈 Select a demo from the sidebar** to see examples!  

    ### ✨ Text to Sumook Painting  
    Generate Sumook Painting Image from text prompts.
    - [한국 전통 수묵화 화풍별 제작 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71380)
    - [Huggingface Diffusers Library](https://github.com/huggingface/diffusers)
    """
    )


if __name__ == "__main__":
    main()