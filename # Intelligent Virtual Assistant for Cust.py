# Intelligent Virtual Assistant for Customer Support
# Extended version with more response categories

def get_response(user_input):
    user_input = user_input.lower()

    # Greeting
    if any(word in user_input for word in ["hello", "hi", "hey", "good morning", "good evening"]):
        return "Hello! How can I assist you today?"

    # Order tracking
    elif "track" in user_input or "order status" in user_input or "where is my order" in user_input:
        return "You can track your order through the 'Track Order' link sent to your email."

    # Return policy
    elif "return" in user_input or "return item" in user_input or "return product" in user_input:
        return "To return an item, go to your orders, select the item, and click on 'Return'."

    # Refund query
    elif "refund" in user_input or "money back" in user_input:
        return "Refunds are usually processed within 5-7 business days after we receive the returned item."

    # Product information
    elif "product" in user_input or "details" in user_input or "specifications" in user_input:
        return "Please specify the product you're asking about, and I can provide more details."

    # Delivery time
    elif "delivery" in user_input or "shipping" in user_input:
        return "Delivery typically takes 3-5 business days, depending on your location."

    # Cancel order
    elif "cancel" in user_input and "order" in user_input:
        return "You can cancel your order within 1 hour of placing it through your orders page."

    # Complaint
    elif "complaint" in user_input or "problem" in user_input or "issue" in user_input:
        return "I'm sorry to hear that. Please describe your issue and I will assist or forward it to a support agent."

    # Payment issue
    elif "payment" in user_input or "billing" in user_input:
        return "For payment issues, please check your bank first. If the issue continues, contact support with your transaction ID."

    # Thanks
    elif "thank" in user_input or "thanks" in user_input:
        return "You're welcome! Let me know if there's anything else I can help with."

    # Goodbye
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Thank you for contacting support."

    # Default fallback
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase or provide more details?"

# Virtual assistant loop
def virtual_assistant():
    print("Virtual Assistant: Welcome to Customer Support. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Virtual Assistant: Thank you for using our support. Have a great day!")
            break
        response = get_response(user_input)
        print("Virtual Assistant:", response)

# Run the assistant
virtual_assistant()

