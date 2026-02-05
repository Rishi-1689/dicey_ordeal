import streamlit as st
import random

st.title("🎲 Dice Battle Game")

# ---- Initialize session state ----
if "round" not in st.session_state:
    st.session_state.round = 1
    st.session_state.user_wins = 0
    st.session_state.computer_wins = 0
    st.session_state.game_over = False

MAX_ROUNDS = 3

# ---- Game logic ----
if not st.session_state.game_over:
    st.write(f"### Round {st.session_state.round}")

    if st.button("Roll Dice 🎲"):
        user_roll = random.randint(1, 6)
        comp_roll = random.randint(1, 6)

        st.write(f"**You rolled:** {user_roll}")
        st.write(f"**Computer rolled:** {comp_roll}")

        if user_roll > comp_roll:
            st.success("You win this round!")
            st.session_state.user_wins += 1
        elif user_roll < comp_roll:
            st.error("Computer wins this round!")
            st.session_state.computer_wins += 1
        else:
            st.info("It's a tie!")

        st.session_state.round += 1

        # ---- End game condition ----
        if (
            st.session_state.round > MAX_ROUNDS
            or st.session_state.user_wins == 2
            or st.session_state.computer_wins == 2
        ):
            st.session_state.game_over = True

# ---- Game over screen ----
if st.session_state.game_over:
    st.write("## 🏁 Game Over")

    st.write(f"**Your wins:** {st.session_state.user_wins}")
    st.write(f"**Computer wins:** {st.session_state.computer_wins}")

    if st.session_state.user_wins > st.session_state.computer_wins:
        st.balloons()
        st.success("🎉 You won the game!")
    elif st.session_state.user_wins < st.session_state.computer_wins:
        st.error("💀 You lost the game!")
    else:
        st.info("🤝 It's a draw!")

    if st.button("Play Again 🔄"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.experimental_rerun()
