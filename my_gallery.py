
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Apps Gallery", page_icon=":guardsman:", layout="wide")
st.title("Apps Gallery")
st.write("Here are some of the apps:")

col1, col2, col3, col4, col5 = st.columns(5)

# URLs of the images in the GitHub repository
img1_url = "https://github.com/hennypurwadi/my_gallery/blob/main/img/img1.jpeg?raw=true"
img2_url = "https://github.com/hennypurwadi/my_gallery/blob/main/img/img2.jpeg?raw=true"
img3_url = "https://github.com/hennypurwadi/my_gallery/blob/main/img/img3.jpeg?raw=true"
img4_url = "https://github.com/hennypurwadi/my_gallery/blob/main/img/img4.jpeg?raw=true"
img5_url = "https://github.com/hennypurwadi/my_gallery/blob/main/img/img5.jpg?raw=true"

# Display the images and create clickable links
with col1:
    st.markdown(f'[![PDF to Image converter]({img1_url})](https://hennypurwadi-my-gallery-pdf2imgpdf2img-4ogp2m.streamlit.app/)')
    st.write("PDF to Image converter")
    st.markdown('[Go to App →](https://hennypurwadi-my-gallery-pdf2imgpdf2img-4ogp2m.streamlit.app/)')
    st.markdown('[View source code →](https://github.com/hennypurwadi/my_gallery/tree/main/pdf2img)')
    
with col2:
    st.markdown(f'[![Image to Text converter]({img2_url})](https://hennypurwadi-my-gallery-img2txtimg2text-s8grum.streamlit.app/)')
    st.write("Image to text converter")
    st.markdown('[Go to App →](https://hennypurwadi-my-gallery-img2txtimg2text-s8grum.streamlit.app/)')
    st.markdown('[View source code →](https://github.com/hennypurwadi/my_gallery/tree/main/img2txt)')

with col3:    
    st.markdown(f'[![PDF combiner]({img3_url})](https://hennypurwadi-my-gallery-pdf-combinercombine-pdf-fxdm75.streamlit.app/)')
    st.write("PDF combiner")
    st.markdown('[Go to App →](https://hennypurwadi-my-gallery-pdf-combinercombine-pdf-fxdm75.streamlit.app/)')
    st.markdown('[View source code →](https://github.com/hennypurwadi/my_gallery/tree/main/pdf_combiner)')  
    
with col4:    
    st.markdown(f'[![Excel to csv converter]({img4_url})](https://hennypurwadi-my-gallery-xls2csvxls2csv-3uybgt.streamlit.app/)')
    st.write("Excel to csv converter")
    st.markdown('[Go to App →](https://hennypurwadi-my-gallery-xls2csvxls2csv-3uybgt.streamlit.app/)')
    st.markdown('[View source code →](https://github.com/hennypurwadi/my_gallery/tree/main/xls2csv)')
    
with col5:
    st.markdown(f'[![Youtube Video to Audio converter]({img5_url})](https://hennypurwadi-my-gallery-vid2audiovid2audio-j3c9as.streamlit.app/)')
    st.write("Youtube Video to Audio converter")
    st.markdown('[Go to App →](https://hennypurwadi-my-gallery-vid2audiovid2audio-j3c9as.streamlit.app/)')
    st.markdown('[View source code →](https://github.com/hennypurwadi/my_gallery/tree/main/vid2audio)')
    
# #FOR FUTURE APPS    
    
# col6, col7, col8, col9, col10 = st.columns(5)

# # URLs of the images in the GitHub repository
# img6_url = "https://github.com/hennypurwadi/my_gallery/blob/main/img/img6.jpeg?raw=true"
# img7_url = "https://github.com/hennypurwadi/my_gallery/blob/main/img/img7.jpeg?raw=true"
# img8_url = "https://github.com/hennypurwadi/my_gallery/blob/main/img/img8.jpeg?raw=true"
# img9_url = "https://github.com/hennypurwadi/my_gallery/blob/main/img/img9.jpeg?raw=true"
# img10_url = "https://github.com/hennypurwadi/my_gallery/blob/main/img/img10.jpeg?raw=true"
# # Display the images and create clickable links
# with col6:
#     st.write("Speech to text converter")
    
# with col7:
#     st.write("Extract Data from PDF")

# with col8:    
#     st.write("Settlement Predictor App")
    
# with col9:    
#     st.write("Future App")

# with col10:
#     st.write("Other App")
