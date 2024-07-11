import streamlit as st
import cv2
import numpy as np

st.set_page_config(layout="wide")
st.title("Test App")


image = st.camera_input(label="Camera View", key="camera_input_file")


if image is not None:
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)

    if data:
        st.write("### Found QR code")
        st.write(data)
        if data == 'P02 V1C T01 S000':
            st.write('Match!')
        else:
            st.write('No match.')

    else:
        st.write("### No QR code")
