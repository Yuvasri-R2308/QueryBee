import re
from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

orders = {
    "ord001": "Your order ORD001 is currently in transit and will arrive in 2 days.",
    "ord002": "Your order ORD002 has been delivered successfully.",
    "ord003": "Your order ORD003 is being processed and will be shipped soon.",
    "ord004": "Your order ORD004 is out for delivery.",
    "ord005": "Your order ORD005 has been cancelled."
}

def get_response(message):

    user_message = message.lower().strip()

    # Order ID Detection
    order_match = re.search(r"ord\d{3}", user_message)

    if order_match:
        order_id = order_match.group(0)

        if order_id in orders:
            return orders[order_id]

        return f"Order ID {order_id.upper()} was not found."

    # Gemini AI
    try:

        prompt = f"""
You are QueryBee, a professional customer support chatbot.

Help customers with:
- Orders
- Refunds
- Shipping
- Product information
- Payment issues
- Customer support

Customer Message:
{message}

Give a short, professional response.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"