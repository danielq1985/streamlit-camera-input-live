import streamlit as st
from streamlit_back_camera_input import back_camera_input
import cv2
import numpy as np
from camera_input_live import camera_input_live




"# Test app"
"### tap image when centered and in focus"

##image = camera_input_live()
image = back_camera_input()

if image is not None:
    st.image(image)
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    detector = cv2.QRCodeDetector()

    data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)

    if data:
        st.write("# Found QR code")
        st.write("Straight QR code:", straight_qrcode)
        ##st.write(data)
        ##with st.expander("Show details"):
          ##  st.write("BBox:", bbox)
          ##  st.write("Straight QR code:", straight_qrcode)
