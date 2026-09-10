import streamlit as st
import random

st.set_page_config(page_title="Prompt-Based Pattern Generator", layout="wide")

st.title("✨ Prompt-Based Pattern Generator")
st.write("Type ANY text prompt. The app will turn it into a pattern.")

def generate_svg_from_prompt(prompt: str):
    # Use prompt as a seed
    seed = sum(ord(c) for c in prompt)
    random.seed(seed)

    size = 600
    elements = []

    # Color palette reacts to prompt length
    base_colors = [
        "#FFB3BA",  # soft pink
        "#FFDFBA",  # peach
        "#FFFFBA",  # pale yellow
        "#BAFFC9",  # mint
        "#BAE1FF",  # light blue
    ]

    # Add abstract shapes
    for _ in range(40):
        x = random.randint(0, size)
        y = random.randint(0, size)
        w = random.randint(30, 120)
        h = random.randint(30, 120)
        color = random.choice(base_colors)
        opacity = random.uniform(0.4, 0.9)
        rotation = random.randint(0, 360)

        elements.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
            f'fill="{color}" opacity="{opacity}" '
            f'transform="rotate({rotation} {x} {y})" />'
        )

    # Add repeated prompt text as a visual motif
    for i in range(8):
        tx = random.randint(50, size - 150)
        ty = random.randint(80, size - 50)
        font_size = random.randint(14, 26)
        text_color = random.choice(["#333333", "#555555", "#777777"])

        elements.append(
            f'<text x="{tx}" y="{ty}" '
            f'fill="{text_color}" font-size="{font_size}" '
            f'font-family="sans-serif" opacity="0.8">'
            f'{prompt}</text>'
        )

    svg = f"""
    <svg width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg">
        {' '.join(elements)}
    </svg>
    """

    return svg

prompt = st.text_input("Enter ANY prompt:", "elegant tropical leaves")
generate = st.button("Generate Pattern")

if generate:
    svg_code = generate_svg_from_prompt(prompt)
    st.subheader("Generated Prompt-Based Pattern")
    st.markdown(svg_code, unsafe_allow_html=True)
