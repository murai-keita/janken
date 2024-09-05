import streamlit as st

st.title("野球拳アプリ")
st.caption("君は脱がすことができるか！？")

st.subheader("操作方法")
st.text("グー、チョキ、パーのボタンを押しだけ！")

gu_btn = st.button("グー")
choki_btn = st.button("チョキ")
pa_btn = st.button("パー")

if gu_btn == True:
    st.text("グーが押されました！あなたの価値！")
if choki_btn == True:
    st.text("チョキ出すの？")
if pa_btn == True:
    st.text("パーは逃げ")