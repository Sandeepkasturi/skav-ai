import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QTextEdit, QGridLayout, QWidget, QSplashScreen
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from urllib.parse import urlparse
from google.generativeai import configure, GenerativeModel
from IPython.display import Markdown
import textwrap
import webbrowser

# Set up the Generative AI configuration with the API key
configure(api_key='Your Google AI API key')

# Function to convert plain text to Markdown format
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

class GenerativeApp(QMainWindow):
    def __init__(self):
        super(GenerativeApp, self).__init__()

        # Create a splash screen
        self.splash = QSplashScreen(QPixmap('sk.jpg'))
        self.splash.show()
        QTimer.singleShot(4000, self.show_main_window)  # Close splash screen after 4 seconds

    def show_main_window(self):
        self.splash.close()

        self.setWindowTitle("SKAV AI")
        self.setGeometry(200, 300, 800, 600)

        # Styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 14px;
                font-weight: bold;
            }
            QLineEdit {
                font-size: 14px;
                padding: 5px;
            }
            QPushButton {
                font-size: 14px;
                padding: 5px;
                border-radius: 5px;
            }
            QTextEdit {
                font-size: 14px;
                border-radius: 5px;
            }
        """)

        # Widgets
        self.label_url = QLabel("Enter URL:", self)
        self.entry_url = QLineEdit(self)
        self.label_question = QLabel("Ask the model a question:", self)
        self.entry_question = QLineEdit(self)
        self.button_generate = QPushButton("Generate Response", self)
        self.button_extract_html = QPushButton("Extract Code from URL", self)
        self.result_text = QTextEdit(self)

        # Layout
        layout = QGridLayout()
        layout.setSpacing(5)
        layout.addWidget(self.label_url, 0, 0)
        layout.addWidget(self.entry_url, 0, 1, 1, 2)
        layout.addWidget(self.label_question, 1, 0, 1, 3)
        layout.addWidget(self.entry_question, 2, 0, 1, 3)
        layout.addWidget(self.button_generate, 2, 3, 1, 1)
        layout.addWidget(self.button_extract_html, 0, 3, 1, 1)
        layout.addWidget(self.result_text, 3, 0, 1, 4)

        # Additional Buttons
        self.setup_additional_buttons(layout)

        # Central Widget
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connect the "Generate Response" button to the function
        self.button_generate.clicked.connect(self.generate_response)
        self.button_extract_html.clicked.connect(self.extract_html)

        self.show()

    def setup_additional_buttons(self, layout):
        button_stargpt = QPushButton("StarGPT")
        button_stargpt.clicked.connect(lambda: self.open_url("https://star-programmer.vercel.app"))
        button_stargpt.setStyleSheet(self.get_button_style("#FFD700"))
        layout.addWidget(button_stargpt, 4, 0, 1, 1)

        button_starmgpt = QPushButton("Star-MGPT")
        button_starmgpt.clicked.connect(lambda: self.open_url("https://star-mgpt.w3spaces.com"))
        button_starmgpt.setStyleSheet(self.get_button_style("#8A2BE2"))
        layout.addWidget(button_starmgpt, 4, 1, 1, 1)

        button_dataverse = QPushButton("DataVerse AI")
        button_dataverse.clicked.connect(lambda: self.open_url("https://dataverse-ai.vercel.app/"))
        button_dataverse.setStyleSheet(self.get_button_style("#20B2AA"))
        layout.addWidget(button_dataverse, 4, 2, 1, 1)

        button_ulink = QPushButton("Ulink")
        button_ulink.clicked.connect(lambda: self.open_url("https://ulink-io.vercel.app"))
        button_ulink.setStyleSheet(self.get_button_style("#FF4500"))
        layout.addWidget(button_ulink, 4, 3, 1, 1)

    def get_button_style(self, color):
        return f"""
            background-color: {color};
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 14px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 5px;
        """

    def open_url(self, url):
        webbrowser.open(url)

    def generate_response(self):
        user_query = self.entry_question.text()
        response = model.generate_content(user_query)
        display_text = to_markdown(response.text)
        self.result_text.setPlainText(display_text.data)

    def extract_html(self):
        url = self.entry_url.text()
        try:
            # Send a GET request to the URL to retrieve the HTML content
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the URL to get the filename for saving
                parsed_url = urlparse(url)
                filename = parsed_url.netloc + "-index.html"

                # Save the HTML content to a file
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(response.text)

                self.result_text.setPlainText(f"HTML content saved to {filename}")
            else:
                self.result_text.setPlainText(f"Failed to retrieve HTML content. Status code: {response.status_code}")
        except Exception as e:
            self.result_text.setPlainText(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create a Generative Model instance (assuming 'gemini-pro' is a valid model)
    model = GenerativeModel('gemini-pro')

    main_window = GenerativeApp()
    sys.exit(app.exec_())
