import streamlit as st
import random

st.set_page_config(page_title="Pattern Generator", layout="wide")

st.title("🎨 Simple SVG Pattern Generator")
st.write("Paste this code first, then commit and push.")

def generate_svg(seed_text):
    seed = sum(ord(c) for c in seed_text)
    random.seed(seed)

    size = 500
    shapes = []

    for _ in range(50):
        x = random.randint(0, size)
        y = random.randint(0, size)
        w = random.randint(20, 80)
        h = random.randint(20, 80)

        color = f"rgb({random.randint(40,200)}, {random.randint(40,200)}, {random.randint(40,200)})"
        shapes.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}" opacity="0.8" />'
        )

    svg = f"""
    <svg width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg">
        {' '.join(shapes)}
    </svg>
    """

    return svg

prompt = st.text_input("Enter a prompt:", "daisy, sakura, star, pastel")
generate = st.button("Generate Pattern")

if generate:
    svg_code = generate_svg(prompt)
    st.subheader("Generated Pattern")
    st.markdown(svg_code, unsafe_allow_html=True)
