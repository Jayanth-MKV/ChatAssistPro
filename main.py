import spacy
import re
import random
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Load the trained model
nlp = spacy.load("intent_model")

# Load FAQs
with open("faq.json") as f:
    faqs = json.load(f)["faqs"]

# Define intents and responses
intents_responses = {
"get_invoice": "Here is a link to download your invoice: [link_to_invoice].",
"payment_issue": "If you're facing payment issues, please check your payment method and try again.",
"check_invoice": "Your invoice details are available here: [link_to_invoice_details].",
"contact_customer_service": "You can reach our customer service at 1-800-123-456 or email support@company.com.",
"complain": "We have logged your complaint. Our team will review it and get back to you shortly.",
"review": "Thank you for your review. We value your feedback and will use it to improve our services.",
"cancel_order": "Your order has been successfully canceled.",
"check_cancellation_fee": "There is no cancellation fee if you cancel within 24 hours of placing the order.",
"check_payment_methods": "We accept Visa, MasterCard, American Express, and PayPal.",
"set_up_shipping_address": "Your shipping address has been updated successfully.",
"track_order": "Your order is currently in transit and will be delivered by the estimated date.",
"place_order": "Your order has been placed successfully. You will receive a confirmation email shortly.",
"check_refund_policy": "Our refund policy states that refunds can be requested within 30 days of purchase.",
"get_refund": "Your refund has been processed and will be credited to your account within 5-7 business days.",
"registration_problems": "If you're having trouble registering, please try clearing your browser cache and cookies.",
"recover_password": "To recover your password, please click the 'Forgot Password' link on the login page.",
"track_refund": "Your refund is being processed and should be completed within 5-7 business days.",
"newsletter_subscription": "You have successfully subscribed to our newsletter.",
"create_account": "Your account has been created successfully. You can now log in using your credentials.",
"delivery_options": "We offer standard, express, and next-day delivery options.",
"delete_account": "Your account has been deleted successfully.",
"delivery_period": "Standard delivery takes 3-5 business days, while express delivery takes 1-2 business days.",
"edit_account": "Your account details have been updated successfully.",
"change_order": "Your order has been updated successfully.",
"switch_account": "You have successfully switched to your new account.",
"change_shipping_address": "You can change the shipping address in the orders section.",
"contact_human_agent": "You are now being connected to a human agent. Please hold on.",
}

# Greeting and farewell patterns
greeting_patterns = re.compile(r'\b(hi|hello|hey|greetings|good morning|good afternoon|good evening|how are you|hiya|howdy|what’s up|sup|yo)\b', re.IGNORECASE)
farewell_patterns = re.compile(r'\b(bye|thankyou|thanks|okay|goodbye|see you|farewell|take care|later|peace|cheers|goodnight|cya)\b', re.IGNORECASE)


# Set the confidence threshold
CONFIDENCE_THRESHOLD = 0.7

def get_intent(text):
    doc = nlp(text)
    intent = max(doc.cats, key=doc.cats.get)
    confidence = doc.cats[intent]
    return intent, confidence

def get_response(text):
    if greeting_patterns.search(text):
        return "Hello! How can I assist you today?"
    elif farewell_patterns.search(text):
        return "Thank you for chatting. Have a great day!"
    else:
        intent, confidence = get_intent(text)
        if confidence >= CONFIDENCE_THRESHOLD:
            return intents_responses.get(intent, "I'm not sure how to respond to that. Can you please rephrase your question?")
        else:
            return "I'm not quite sure what you're asking. Could you please provide more details or rephrase your question?"

app = FastAPI()

class ChatInput(BaseModel):
    message: str

@app.post("/chat")
async def chat(chat_input: ChatInput):
    response = get_response(chat_input.message)
    return {"response": response}

@app.get("/faqs")
async def get_faqs():
    start_index = random.randint(0, len(faqs) - 5)
    end_index = start_index + 5
    return {"faqs": faqs[start_index:end_index]}  # Return the first 5 FAQs


@app.get("/")
def read_root():
    return {"Hello": "World"}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)