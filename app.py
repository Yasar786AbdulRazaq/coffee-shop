import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Coffee Heaven",
    page_icon="☕",
    layout="wide"
)

# Load coffee data
def load_coffee_data():
    return {
        "Classic Espresso": {
            "price": 200,
            "image": "https://images.unsplash.com/photo-1614350292382-c448d0110dfa",
            "description": "A rich and intense single-shot espresso."
        },
        "Velvet Cappuccino": {
            "price": 300,
            "image": "https://images.unsplash.com/photo-1572442388796-11668a67e53d",
            "description": "Smooth blend of espresso, steamed milk, and milk foam."
        },
        "Creamy Latte": {
            "price": 450,
            "image": "https://images.unsplash.com/photo-1561047029-3000c68339ca",
            "description": "Light and milky, perfect for a calm morning."
        }
    }

# Navigation
def main():
    with st.sidebar:
        st.markdown("## ☕ Coffee Heaven")
        page = st.radio("Navigate", ["🏠 Home", "📋 Menu", "👨‍💼 About", "📞 Contact"])

    if page == "🏠 Home":
        show_home()
    elif page == "📋 Menu":
        show_menu()
    elif page == "👨‍💼 About":
        show_about()
    elif page == "📞 Contact":
        show_contact()

def show_home():
    st.markdown("""
        <div style='text-align: center; padding: 50px 0;'>
            <h1 style='font-size: 60px;'>Welcome to <span style='color:#6f4e37;'>Coffee Heaven</span> ☕</h1>
            <h3>Your perfect cup of coffee is just a click away.</h3>
            <img src='https://images.unsplash.com/photo-1511920170033-f8396924c348' width='70%' style='margin-top:30px; border-radius:15px;'/>
        </div>
    """, unsafe_allow_html=True)

def show_menu():
    st.markdown("<h1 style='color:#6f4e37;'>Our Signature Coffees</h1><hr>", unsafe_allow_html=True)
    coffee_data = load_coffee_data()

    for coffee_name, details in coffee_data.items():
        with st.container():
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(details["image"], caption=coffee_name, width=250)
            
            with col2:
                st.markdown(f"### {coffee_name}")
                st.markdown(f"<span style='color:green; font-size:18px;'>Rs. {details['price']}</span>", unsafe_allow_html=True)
                st.write(details["description"])
                if st.button(f"Order Now - {coffee_name}"):
                    show_order_form(coffee_name, details["price"])

def show_order_form(coffee_name, price):
    st.markdown("---")
    st.markdown(f"<h3 style='color:#6f4e37;'>Order Your {coffee_name}</h3>", unsafe_allow_html=True)
    name = st.text_input("Your Name")
    address = st.text_area("Delivery Address")
    phone = st.text_input("Phone Number")

    if st.button("Confirm Order"):
        if name and address and phone:
            st.success(f"""
            ✅ Order Confirmed!
            - ☕ Coffee: {coffee_name}
            - 💵 Price: Rs. {price}
            - 🙍 Name: {name}
            - 🏠 Address: {address}
            - 📞 Phone: {phone}
            """)
        else:
            st.error("⚠️ Please fill all the fields.")

def show_about():
    st.markdown("<h1 style='color:#6f4e37;'>About Coffee Heaven</h1>", unsafe_allow_html=True)
    st.write("""
    Since 2015, Coffee Heaven has been brewing the finest flavors from around the world.
    We believe that every cup should be made with passion, precision, and love.

    - ✅ Premium Coffee Beans
    - ✅ Expert Baristas
    - ✅ Freshly Brewed Happiness
    """)

def show_contact():
    st.markdown("<h1 style='color:#6f4e37;'>Contact Us</h1>", unsafe_allow_html=True)
    st.write("""
    📞 **Phone:** +92 3419785494
    📧 **Email:** Yasardeveloper786@gmail.com
    📍 **Location:** Coffee Street,punjab, Lahore ,  Pakistan  
    """)
    
    st.markdown("### Send Us a Message")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send Message"):
        if name and email and message:
            st.success("Thanks for reaching out! We'll respond as soon as possible.")
        else:
            st.error("Please complete all fields.")

if __name__ == "__main__":
    main()
