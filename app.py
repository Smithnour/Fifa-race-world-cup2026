import streamlit as st
import random
import time

st.set_page_config(page_title="World Cup 2026 Race", layout="centered")

st.title("🏆 كأس العالم 2026 - سباق المنتخبات")

teams_input = st.text_area(
    "أدخل المنتخبات (كل منتخب في سطر):",
    "المغرب\nفرنسا\nالبرازيل\nالأرجنتين"
)

def run_race(teams):
    progress = {team: 0 for team in teams}
    winner = None
    placeholder = st.empty()

    while winner is None:
        for team in teams:
            progress[team] += random.randint(1, 8)

            if progress[team] >= 100:
                progress[team] = 100
                winner = team
                break

        with placeholder.container():
            for team in teams:
                bar = "🟢" * (progress[team] // 10)
                st.write(f"{team}: {bar} {progress[team]}%")

        time.sleep(0.3)

    return winner


if st.button("🚀 بدء السباق"):
    teams = [t.strip() for t in teams_input.splitlines() if t.strip()]

    if len(teams) < 4:
        st.error("أدخل 4 منتخبات على الأقل")
    else:
        winner = run_race(teams)
        st.balloons()
        st.success(f"🏁 الفائز هو: {winner}")
