import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_fee_reminder():
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    sender_email = "venkatujji.01@gmail.com"
    sender_password = "tdvj ecda rjvh kyqt"

    receiver_email = input("Enter receiver's email: ").strip()
    if "@" not in receiver_email or "." not in receiver_email:
        print("Invalid email address. Please check and try again.")
        return

    receiver_name = input("Enter receiver's name: ").strip()
    try:
        fee_paid = float(input("Enter the amount paid by the student: ").strip())
    except ValueError:
        print("Invalid fee input. Please enter a numeric value.")
        return

    total_fee = 40000
    remaining_fee = total_fee - fee_paid

    subject = "Fee Payment Reminder"

    body = f"""Dear {receiver_name},

Hope you're doing well.

This is a kind reminder that your remaining fee amount is ₹{remaining_fee:.2f}. Please make the payment at the earliest convenience to avoid any late charges.

Total Fee       : ₹{total_fee:.2f}
Amount Paid     : ₹{fee_paid:.2f}
Remaining Due   : ₹{remaining_fee:.2f}

If you have already completed the payment, kindly disregard this message.

Thank you for your cooperation.

Warm regards,  
Venkatujji  
Accounts Department  
venkatujji.01@gmail.com
"""

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print(f"Email sent successfully to {receiver_email}.")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
        
send_fee_reminder()
