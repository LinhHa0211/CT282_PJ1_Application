import io
import streamlit as st
from PIL import Image
from src.preprocess import preprocess
from src.model import ModelLoader, Predictor

model_loader = ModelLoader()
predictor = Predictor()

# Initialize session state
if 'result' not in st.session_state:
    st.session_state['result'] = "Chưa có kết quả."

# Page configuration
st.set_page_config(
    page_title="Nhận dạng ảnh lễ hội truyền thống tại Việt Nam bằng mô hình CNN",
    layout="wide",
    initial_sidebar_state="auto"
)

# Title
st.markdown(
    "<h2 style='text-align: center;'>Website nhận dạng ảnh lễ hội truyền thống tại Việt Nam bằng mô hình CNN</h2>",
    unsafe_allow_html=True
)

# Layout
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Tải ảnh lên")
    uploaded_file = st.file_uploader(
        "Chọn ảnh",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=False
    )

    image = None
    st.session_state['result'] = "Chưa có kết quả."
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file).convert('RGB')
            st.image(image, caption="Ảnh đã tải", use_container_width=True)
        except Exception as e:
            st.error(f"Lỗi khi xử lý ảnh: {str(e)}")

with col2:
    st.subheader("Chọn mô hình")
    selected_model = st.selectbox(
        "Phiên bản",
        options=list(model_loader.get_all_versions()),
        index=0
    )

    
    if st.button("▶ Nhận dạng", key="predict_button"):
        if image is not None:
            try:
                image = preprocess(image)
                model = model_loader.get_model(selected_model)
                result = predictor.predict(model, image)
                st.session_state['result'] = result
                st.success("Nhận dạng thành công!")
            except Exception as e:
                st.error(f"Lỗi khi nhận dạng: {str(e)}")
        else:
            st.warning("Vui lòng tải ảnh trước khi nhận dạng.")
    st.subheader("Kết quả nhận dạng")
    st.info(st.session_state['result'])