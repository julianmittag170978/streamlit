

import streamlit as st
import requests

# Constants
API_URL = "https://api.pokemontcg.io/v2/cards"

# Function to get card data from pokemontcg.io
def get_card_info(card_name):
    response = requests.get(API_URL, params={'q': f'name:{card_name}'})
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        return []

# Function to list a card for sale
def list_card_for_sale(card_name, card_price):
    card_info = get_card_info(card_name)
    if card_info:
        listed_cards.append({
            'name': card_info[0]['name'],
            'price': card_price,
            'image': card_info[0]['images']['small']
        })
        return True
    else:
        return False

# App title
st.title("Pokémon Card Marketplace")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose an action", ["Browse Cards", "List a Card for Sale", "View Card Info"])

# List of cards available for sale
listed_cards = []

if page == "Browse Cards":
    st.header("Browse Cards for Sale")
    if listed_cards:
        for card in listed_cards:
            st.image(card['image'], width=150)
            st.write(f"**{card['name']}** - ${card['price']}")
    else:
        st.write("No cards listed for sale yet.")

elif page == "List a Card for Sale":
    st.header("List a Card for Sale")
    card_name = st.text_input("Enter the card name")
    card_price = st.number_input("Enter the card price", min_value=0.0, format="%.2f")
    if st.button("List Card"):
        if list_card_for_sale(card_name, card_price):
            st.success(f"Card '{card_name}' listed successfully!")
        else:
            st.error(f"Could not find card '{card_name}'. Please try again.")

elif page == "View Card Info":
    st.header("Get Information on a Card")
    card_name = st.text_input("Enter the card name to search")
    if st.button("Search"):
        cards = get_card_info(card_name)
        if cards:
            for card in cards:
                st.image(card['images']['small'], width=150)
                st.write(f"**Name:** {card['name']}")
                st.write(f"**Supertype:** {card['supertype']}")
                st.write(f"**Set:** {card['set']['name']}")
                st.write(f"**Rarity:** {card.get('rarity', 'N/A')}")
                st.write(f"**HP:** {card.get('hp', 'N/A')}")
                st.write(f"**Number:** {card['number']}")
        else:
            st.write("No card found with that name.")


