import streamlit as st
import requests
import cv2
import numpy as no

st.set_page_config(layout="wide")
st.title("Test App")

col_left, _, col_right = st.columns([5, 1, 5])


with col_left:
    x = st.camera_input(label="AAA", key="camera_input_file")

with col_right:
    if x is not None:
        st.image(x.getvalue(), caption="Your photo", use_column_width=True)


##image = camera_input_live()
#$image = back_camera_input()
image = x


if image is not None:
    st.image(image)
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    detector = cv2.QRCodeDetector()

    data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)

    if data:
        st.write("# Found QR code")
        st.write(data)
        ##with st.expander("Show details"):
          ##  st.write("BBox:", bbox)
          ##  st.write("Straight QR code:", straight_qrcode)

          
