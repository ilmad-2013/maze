import streamlit as st

st.set_page_config(
    page_title="Escape the Maze",
    page_icon="🧩"
)

st.title("🧩 Escape the Maze")
st.write("You are trapped inside a mysterious maze.")
st.write("Find the key and escape!")

# Game setup
if "location" not in st.session_state:
    st.session_state.location = "Entrance"

if "key" not in st.session_state:
    st.session_state.key = False

if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Game information
st.sidebar.subheader("Inventory")

if st.session_state.key:
    st.sidebar.success("🔑 Key")

else:
    st.sidebar.write("No items yet")

st.sidebar.write(
    "Current location:"
)

st.sidebar.write(
    st.session_state.location
)

# Stop game if finished
if st.session_state.game_over:

    st.success(
        "🎉 Congratulations! You escaped the maze!"
    )

    if st.button("Play Again"):

        st.session_state.clear()

        st.rerun()

else:

    location = st.session_state.location

    # Entrance
    if location == "Entrance":

        st.header("🚪 The Entrance")

        st.write(
            "You see two paths ahead."
        )

        choice = st.radio(
            "Which path do you take?",
            ["Left path", "Right path"]
        )

        if st.button("Continue"):

            if choice == "Left path":

                st.session_state.location = "Library"

            else:

                st.session_state.location = "Dark Hall"

            st.rerun()

    # Library
    elif location == "Library":

        st.header("📚 The Library")

        st.write(
            "Old books cover the walls."
        )

        st.write(
            "Something shiny is hidden behind a book."
        )

        if not st.session_state.key:

            if st.button("Investigate the bookshelf"):

                st.session_state.key = True

                st.success(
                    "You found a 🔑 mysterious key!"
                )

        if st.button("Leave the library"):

            st.session_state.location = "Central Room"

            st.rerun()

    # Dark Hall
    elif location == "Dark Hall":

        st.header("🌑 The Dark Hall")

        st.write(
            "The hallway is completely dark."
        )

        choice = st.radio(
            "What do you do?",
            ["Walk forward", "Go back"]
        )

        if st.button("Choose"):

            if choice == "Walk forward":

                st.session_state.location = "Trap Room"

            else:

                st.session_state.location = "Entrance"

            st.rerun()

    # Trap room
    elif location == "Trap Room":

        st.header("⚠️ Trap Room")

        st.warning(
            "You stepped into a room with a locked door!"
        )

        if st.session_state.key:

            st.write(
                "Luckily, your key fits the lock."
            )

            if st.button("Unlock the door"):

                st.session_state.location = "Central Room"

                st.rerun()

        else:

            st.error(
                "You need a key to continue."
            )

            if st.button("Return"):

                st.session_state.location = "Entrance"

                st.rerun()

    # Central room
    elif location == "Central Room":

        st.header("🏛️ Central Room")

        st.write(
            "You see a huge locked exit door."
        )

        if st.session_state.key:

            if st.button("Use the key"):

                st.session_state.game_over = True

                st.rerun()

        else:

            st.warning(
                "The door requires a key."
            )

        if st.button("Explore again"):

            st.session_state.location = "Entrance"

            st.rerun()