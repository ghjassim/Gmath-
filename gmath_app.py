
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

st.set_page_config(page_title="Gmath - أكاديمية الرياضيات", layout="wide")
st.title("📘 Gmath - أكاديمية علوم الرياضيات")
st.markdown("اختر مجالًا للتعلم 👇")

topic = st.selectbox("📚 اختر المجال", ["الجبر الخطي", "التفاضل والتكامل", "الأنظمة الديناميكية"])

if topic == "الجبر الخطي":
    st.header("🧮 الجبر الخطي")
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5], [6]])
    result = np.dot(A, B)
    st.write("المصفوفة A:"); st.write(A)
    st.write("المصفوفة B:"); st.write(B)
    st.write("الناتج A × B:"); st.write(result)

elif topic == "التفاضل والتكامل":
    st.header("📐 التفاضل والتكامل")
    x = sp.symbols('x')
    expr_input = st.text_input("📌 أدخل دالة مثل: sin(x)*x**2", "sin(x)*x**2")
    try:
        expr = sp.sympify(expr_input)
        deriv = sp.diff(expr, x)
        integral = sp.integrate(expr, x)
        st.latex(f"f(x) = {sp.latex(expr)}")
        st.latex(f"f'(x) = {sp.latex(deriv)}")
        st.latex(f"\int f(x)dx = {sp.latex(integral)}")
        f = sp.lambdify(x, expr, "numpy")
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f(x_vals)
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label=f"${sp.latex(expr)}$")
        ax.set_title("رسم الدالة"); ax.legend()
        st.pyplot(fig)
    except:
        st.error("❌ تأكد من كتابة الدالة بشكل صحيح")

elif topic == "الأنظمة الديناميكية":
    st.header("⚙️ الأنظمة الديناميكية")
    a = st.slider("🔁 اختر معامل النمو a", -2.0, 2.0, 0.5)
    t = np.linspace(0, 10, 100)
    y0 = 1
    y = y0 * np.exp(a * t)
    fig, ax = plt.subplots()
    ax.plot(t, y, label=f"$y(t) = {y0}e^{{{a}t}}$")
    ax.set_title("نمو/تناقص النموذج الأسي")
    ax.set_xlabel("الزمن")
    ax.set_ylabel("y(t)")
    ax.legend()
    st.pyplot(fig)
