# import pandas as pd
# import matplotlib.pyplot as plt
# from PIL import Image
# import os
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
# import pyttsx3

# class CarDashboardHelper:
#     def __init__(self, csv_path, email_user, email_password, smtp_host="smtp.gmail.com", smtp_port=587):
#         self.data = pd.read_csv(csv_path)
#         self.email_user = email_user
#         self.email_password = email_password
#         self.smtp_host = smtp_host
#         self.smtp_port = smtp_port
#         self.engine = pyttsx3.init()

#     def speak_to_file(self, text, filename="email_content.mp3"):
#         """Convert text to speech and save it to an audio file."""
#         self.engine.save_to_file(text, filename)
#         self.engine.runAndWait()
#         return filename

#     def send_email_with_voice_attachment(self, to_email, solution, image_path):
#         """Send an email with the solution, image, and voice attachment."""
#         try:
#             # Convert the solution to an audio file
#             audio_filename = self.speak_to_file(solution)

#             # Create the email message
#             msg = MIMEMultipart()
#             msg['From'] = self.email_user
#             msg['To'] = to_email
#             msg['Subject'] = "Solution for Car Dashboard Symbol"

#             # Attach the solution text
#             msg.attach(MIMEText(solution, 'plain'))

#             # Attach the image
#             with open(image_path, 'rb') as img_file:
#                 img = MIMEBase('application', 'octet-stream')
#                 img.set_payload(img_file.read())
#                 encoders.encode_base64(img)
#                 img.add_header('Content-Disposition', f'attachment; filename={os.path.basename(image_path)}')
#                 msg.attach(img)

#             # Attach the audio file
#             with open(audio_filename, 'rb') as audio_file:
#                 audio = MIMEBase('application', 'octet-stream')
#                 audio.set_payload(audio_file.read())
#                 encoders.encode_base64(audio)
#                 audio.add_header('Content-Disposition', f'attachment; filename={audio_filename}')
#                 msg.attach(audio)

#             # Connect to SMTP server and send the email
#             smtp = smtplib.SMTP(self.smtp_host, self.smtp_port)
#             smtp.ehlo()
#             smtp.starttls()
#             smtp.login(self.email_user, self.email_password)
#             smtp.sendmail(self.email_user, to_email, msg.as_string())
#             smtp.quit()

#             print("[*] Email sent successfully with audio attachment!")
#         except Exception as e:
#             print(f"Error sending email: {e}")

#     def generate_report(self, label, to_email):
#         """Generate a report for a label and send it via email."""
#         row = self.data[self.data['label'] == label]
        
#         if row.empty:
#             return f"No data found for label: {label}"

#         image_path = row.iloc[0]['image_path']
#         solution = row.iloc[0]['solution']

#         if os.path.exists(image_path):
#             try:
#                 # Display the solution and image
#                 print("\nSolution:")
#                 print(solution)
#                 image = Image.open(image_path)
#                 plt.imshow(image)
#                 plt.axis('off')
#                 plt.title(f"Solution for Label {label}")
#                 plt.show()

#                 # Send email with solution, image, and voice attachment
#                 self.send_email_with_voice_attachment(to_email, solution, image_path)
#                 return f"Report generated and sent for label: {label}"
#             except Exception as e:
#                 return f"Error displaying image or sending email: {e}"
#         else:
#             return f"Image file not found at path: {image_path}"

# # Example usage as a module
# if __name__ == "__main__":
#     # Configuration
#     CSV_PATH = "car_dasboard_symbol_detection/Symbols23.csv"
#     EMAIL_USER = "bhushannikhade446@gmail.com"
#     EMAIL_PASSWORD = "shws xudn blmp tgae"  # Your generated App Password
#     TO_EMAIL = "krushnansh22@gmail.com"

#     # Initialize the helper
#     helper = CarDashboardHelper(CSV_PATH, EMAIL_USER, EMAIL_PASSWORD)

#     # Get user input and generate report
#     label_input = int(input("Enter label (e.g., 0, 1, 2): "))
#     report_status = helper.generate_report(label_input, TO_EMAIL)
#     print(report_status)
import pandas as pd
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pyttsx3
from PIL import Image

class CarDashboardHelper:
    def __init__(self, csv_path, email_user, email_password, smtp_host="smtp.gmail.com", smtp_port=587):
        self.data = pd.read_csv(csv_path)
        self.email_user = email_user
        self.email_password = email_password
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.engine = pyttsx3.init()

    def speak_to_file(self, text, filename="email_content.mp3"):
        """Convert text to speech and save it to an audio file."""
        self.engine.save_to_file(text, filename)
        self.engine.runAndWait()
        return filename

    def send_email_with_voice_attachment(self, to_email, solution, image_path):
        """Send an email with the solution, image, and voice attachment."""
        try:
            # Convert the solution to an audio file
            audio_filename = self.speak_to_file(solution)

            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.email_user
            msg['To'] = to_email
            msg['Subject'] = "Solution for Car Dashboard Symbol"

            # Attach the solution text
            msg.attach(MIMEText(solution, 'plain'))

            # Attach the image
            with open(image_path, 'rb') as img_file:
                img = MIMEBase('application', 'octet-stream')
                img.set_payload(img_file.read())
                encoders.encode_base64(img)
                img.add_header('Content-Disposition', f'attachment; filename={os.path.basename(image_path)}')
                msg.attach(img)

            # Attach the audio file
            with open(audio_filename, 'rb') as audio_file:
                audio = MIMEBase('application', 'octet-stream')
                audio.set_payload(audio_file.read())
                encoders.encode_base64(audio)
                audio.add_header('Content-Disposition', f'attachment; filename={audio_filename}')
                msg.attach(audio)

            # Connect to SMTP server and send the email
            smtp = smtplib.SMTP(self.smtp_host, self.smtp_port)
            smtp.ehlo()
            smtp.starttls()
            smtp.login(self.email_user, self.email_password)
            smtp.sendmail(self.email_user, to_email, msg.as_string())
            smtp.quit()

            print("[*] Email sent successfully with audio attachment!")
        except Exception as e:
            print(f"Error sending email: {e}")

    def generate_report(self, label, to_email):
        """Generate a report for a label and send it via email."""
        row = self.data[self.data['label'] == label]
        
        if row.empty:
            return f"No data found for label: {label}"

        image_path = row.iloc[0]['image_path']
        solution = row.iloc[0]['solution']

        if os.path.exists(image_path):
            try:
                # Print the solution in the console
                print("\nSolution:")
                print(solution)

                # Send email with solution, image, and voice attachment
                self.send_email_with_voice_attachment(to_email, solution, image_path)
                return f"{label}\n{solution}"
            except Exception as e:
                return f"Error sending email: {e}"
        else:
            return f"Image file not found at path: {image_path}"

# Example usage as a module
if __name__ == "__main__":
    # Configuration
    CSV_PATH = "car_dasboard_symbol_detection/Symbols23.csv"
    EMAIL_USER = "bhushannikhade446@gmail.com"
    EMAIL_PASSWORD = "shws xudn blmp tgae"  # Your generated App Password
    TO_EMAIL = "krushnansh22@gmail.com"

    # Initialize the helper
    helper = CarDashboardHelper(CSV_PATH, EMAIL_USER, EMAIL_PASSWORD)

    # Get user input and generate report
    label_input = int(input("Enter label (e.g., 0, 1, 2): "))
    report_status = helper.generate_report(label_input, TO_EMAIL)
    print(report_status)
