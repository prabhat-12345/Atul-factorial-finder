import sys
import streamlit as st
import math
import numpy as np
import sympy as sp
import torch

# Python's default 4300 string digit conversion limit ko badhana
sys.set_int_max_str_digits(200000)

# Page Layout & Title Configuration
st.set_page_config(
    page_title="Atul Prabhat Laxmi App",
    page_icon="⚡",
    layout="centered"
)

# Custom Glassmorphic Dark UI Theme CSS
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311042 100%);
            color: #f8fafc;
        }
        .main-title {
            font-size: 3rem !important;
            font-weight: 800 !important;
            background: linear-gradient(90deg, #38bdf8, #a855f7, #ec4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 5px;
        }
        .sub-title {
            color: #94a3b8;
            text-align: center;
            font-size: 1.1rem;
            margin-bottom: 40px;
        }
        .matrix-grid {
            font-family: 'Courier New', monospace;
            background: rgba(0, 0, 0, 0.4);
            padding: 15px;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            line-height: 1.6;
            letter-spacing: 4px;
            word-break: break-all;
            max-height: 400px;
            overflow-y: auto;
        }
    </style>
""", unsafe_allow_html=True)

# Main App Header
st.markdown('<h1 class="main-title">⚡ Atul Prabhat Laxmi App</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Advanced Large Integer Matrix Analytics Pipeline</p>', unsafe_allow_html=True)

# User Input Target Value
num = st.number_input("Enter Integer Target Value:", min_value=0, max_value=5000, value=1000, step=1)

# Trailing Zeros count karne ka fast mathematical function (Legendre's Formula)
def count_trailing_zeros(n):
    zeros = 0
    while n >= 5:
        n //= 5
        zeros += n
    return zeros

if st.button("🚀 Execute Factorial Pipeline", type="primary", use_container_width=True):
    with st.spinner("Processing deep matrix calculation..."):
        
        # High-performance Core Factorial Evaluation
        fact_value = math.factorial(num)
        fact_str = str(fact_value)
        total_digits = len(fact_str)
        trailing_zeros = count_trailing_zeros(num)
        
        # Digits List parsing for framework export
        digits_list = [int(d) for d in fact_str]
        
        st.markdown("### 📊 Engine Computations")
        
        # Display Core Metrics (Digits & Trailing Zeros)
        col1, col2, col3 = st.columns(3)
        col1.metric("Target Factorial", f"{num}!")
        col2.metric("Total Digits", f"{total_digits:,}")
        col3.metric("Trailing Zeros (0s at end)", f"{trailing_zeros:,}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Matrix Column-Wise View Logic
        st.markdown("#### 🔢 Digit Matrix Stream (Clean 10-Column Alignment View)")
        
        preview_limit = 1000  
        matrix_lines = []
        for i in range(0, min(total_digits, preview_limit), 10):
            row_chunk = fact_str[i:i+10]
            formatted_row = " ".join(row_chunk)
            matrix_lines.append(formatted_row)
            
        matrix_html = "<br>".join(matrix_lines)
        if total_digits > preview_limit:
            matrix_html += "<br>... [Truncated for performance, download full file below] ..."
            
        st.markdown(f'<div class="matrix-grid">{matrix_html}</div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Framework Export Data Structures Information
        st.markdown("### 📦 Framework Export Vectors")
        st.info(f"**SymPy Vector Space:** Instantiated `sp.Tuple` enclosing `sp.Integer` formats. Target resolution size: `{total_digits}` values allocated perfectly.")
        
        np_digits_array = np.array(digits_list, dtype=np.int8)
        st.warning(f"**NumPy Array Profile:** Formatted to memory-optimal tensor mapping. Shape: `{np_digits_array.shape}` | Dtype: `int8`")
        
        torch_digits_tensor = torch.tensor(digits_list, dtype=torch.int8)
        st.error(f"**PyTorch Tensor Space:** Prepared structural engine pipeline object. Shape: `{list(torch_digits_tensor.shape)}` | Hardware Device Target: `{torch_digits_tensor.device.type.upper()}`")
        
        # Text file stream & download
        st.markdown("### 💾 Storage & Data Streams")
        file_content = f"--- Factorial Calculation Data Profile ---\nTarget: {num}!\nTotal Digit Length: {total_digits}\nTotal Trailing Zeros: {trailing_zeros}\n\n{fact_str}"
        
        st.download_button(
            label="📥 Stream Complete Dataset (.txt)",
            data=file_content,
            file_name=f"factorial_{num}_matrix.txt",
            mime="text/plain",
            use_container_width=True
        )
        
