# Press Enter to roll the dice...
# You rolled: 5
# Computer rolled: 3
# ⭐ You win!
import streamlit as st
import random

# Tile
st.title("Welcome to a dicey game!!")



# Defining a session state for streamlit to follow:
if "rounds" not in st.session_state:
    st.session_state.rounds = 1

    st.session_state.over = False

    st.session_state.comp_win = 0
    st.session_state.your_win = 0



# Total number of rounds:
MAX_ROUNDS = 3



# This where the 'fun' begins:
if not st.session_state.over:

    if st.button("Roll", key="rolling"):
        # You, the user defined:
        your_turn = random.randint(1, 6)

        # The computer defined:
        comp_turn = random.randint(1, 6)

        # Round Logic:
        st.write(f"You roll: {your_turn}")
        st.write(f"The computer rolls: {comp_turn}")

        #If computer wins the round:
        if your_turn < comp_turn:
            st.write("The computer wins this round...BOOOOOO")
            st.session_state.comp_win += 1


        # If You win the round:
        elif your_turn > comp_turn:
            st.write("You win this round!! LETS GOOOO")
            st.session_state.your_win += 1

        # A Draw:
        else:
            st.write("It's a draw...")
            
        st.session_state.rounds += 1

        # Logic for breaking the loop:
        if st.session_state.your_win == 2 or st.session_state.comp_win == 2 or st.session_state.rounds > MAX_ROUNDS:
            st.session_state.over = True

if st.session_state.over:

    st.info(f"Game Over.")
    st.write(f"TOTAL NUMBER OF ROUNDS WON BY USER: {st.session_state.your_win}")
    st.write(f"TOTAL NUMBER OF ROUNDS WON BY THE COMPUTER: {st.session_state.comp_win}")
    # Message for victory:
    if st.session_state.your_win > st.session_state.comp_win:
        st.balloons()
        st.success("Congrats!! You win the game!")
    # Message for losing:
    elif st.session_state.your_win < st.session_state.comp_win:
        st.error("Computer Wins....")
    else:
        st.info("It's a Draw.")
        

    








