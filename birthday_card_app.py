
import streamlit as st
import streamlit.components.v1 as components

# HTML과 CSS를 사용하여 카드 애니메이션 구현
card_animation = """
<div class="envelope">
    <div class="card">
        <div class="front">🎉 Happy Birthday!</div>
        <div class="inside">🎂 Wishing you a fantastic year ahead! 🎂</div>
    </div>
</div>

<style>
.envelope {
    width: 300px;
    height: 200px;
    position: relative;
    background-color: #F1C40F;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
    cursor: pointer;
    overflow: hidden;
}

.card {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    background-color: white;
    border-radius: 10px;
    transition: transform 1s ease-in-out;
    transform-origin: bottom;
    transform: translateY(100%);
}

.card.open {
    transform: translateY(0);
}

.front {
    font-size: 24px;
    color: #34495E;
    text-align: center;
    line-height: 200px;
}

.inside {
    font-size: 20px;
    color: #34495E;
    text-align: center;
    padding-top: 70px;
    display: none;
}

.envelope.open .inside {
    display: block;
}

.envelope.open .front {
    display: none;
}

.envelope:hover .card {
    transform: translateY(0);
}

.envelope.open .card {
    transform: translateY(0);
}
</style>

<script>
    const envelope = document.querySelector('.envelope');
    envelope.addEventListener('click', function() {
        envelope.classList.toggle('open');
    });
</script>
"""

# Streamlit에 컴포넌트로 HTML 삽입
st.title("Interactive Birthday Card")
components.html(card_animation, height=400)
