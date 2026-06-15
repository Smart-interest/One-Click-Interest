import streamlit as st

# ऐप की हेडिंग और डिजाइन
st.set_page_config(page_title="जनगणना मकान गणना टूल", page_icon="🏢", layout="centered")

st.title("🏢 आवासीय और खाली मकानों की संख्या")
st.write("नीचे दिए गए बॉक्स में अपना डेटा दर्ज करें और तुरंत परिणाम देखें।")
st.markdown("---")

# बाईं और दाईं तरफ दो कॉलम बनाकर इनपुट बॉक्स को सुंदर दिखाना
col1, col2 = st.columns(2)

with col1:
    sink_data = st.number_input("Sink किया गया डेटा संख्या:", min_value=0, value=104, step=1)
    bhavan = st.number_input("भवन संख्या दर्ज करें:", min_value=0, value=10, step=1)
    makaan = st.number_input("कुल जनगणना मकान संख्या:", min_value=0, value=12, step=1)

with col2:
    pariwaar = st.number_input("परिवार संख्या दर्ज करें:", min_value=0, value=8, step=1)
    gair_aawasiya = st.number_input("गैर आवासीय मकान संख्या:", min_value=0, value=2, step=1)
    lock_makaan = st.number_input("लॉक किए गए मकान संख्या:", min_value=0, value=1, step=1)

st.markdown("---")

# गणना (Calculations) ऑटोमैटिक होगी
hunt = sink_data - pariwaar
khali = hunt - gair_aawasiya
aawasiya = makaan - hunt

# परिणाम को सुंदर बॉक्सेस (Metrics) में दिखाना
st.subheader("📊 गणना का परिणाम (Results)")

res_col1, res_col2, res_col3 = st.columns(3)
with res_col1:
    st.metric(label="कुल भवन", value=bhavan)
    st.metric(label="आवासीय मकान", value=aawasiya)

with res_col2:
    st.metric(label="कुल जनगणना मकान", value=makaan)
    st.metric(label="बंद (Lock) मकान", value=lock_makaan)

with res_col3:
    st.metric(label="गैर आवासीय मकान", value=gair_aawasiya)
    st.metric(label="🏠 खाली मकान", value=khali, delta=None)

st.success("गणना सफलतापूर्वक पूरी हो गई है! - Thank You")

