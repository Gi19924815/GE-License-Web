import streamlit as st
import hashlib

# ⚠️ 保持盐值与主程序一模一样！
SECRET_SALT = "LAOYING_EARTH_PRO_2026"

def generate_key(machine_code):
    raw_str = machine_code.strip().upper() + SECRET_SALT
    key_hash = hashlib.md5(raw_str.encode('utf-8')).hexdigest().upper()
    return f"{key_hash[:4]}-{key_hash[4:8]}-{key_hash[8:12]}"

# 设置网页配置
st.set_page_config(page_title="GE 专属算号中心", page_icon="🚀", layout="centered")
st.title("🚀 GE 电影级航线生成器")
st.markdown("### 云端授权签发中心")

user_code = st.text_input("👉 请输入客户发来的机器码：", placeholder="例如 GE-7DC5779B")

if st.button("算号并生成授权文件", type="primary"):
    if user_code.strip():
        activation_key = generate_key(user_code)

        st.success("✅ 授权生成成功！")
        st.info(f"激活码明文：{activation_key}")

        # 魔法下载按钮
        st.download_button(
            label="💾 点击下载授权文件 (.ge_tour_license.dat)",
            data=activation_key,
            file_name=".ge_tour_license.dat",
            mime="application/octet-stream"
        )

        st.markdown("---")
        st.markdown("**交付说明 (可直接复制发给客户)：**\n请将下载的文件放到 `C:\\Users\\您的用户名\\` (Windows) 或 `/Users/您的用户名/` (Mac) 目录下即可生效。")
    else:
        st.error("❌ 请先输入机器码！")
