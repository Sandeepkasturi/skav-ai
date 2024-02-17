## SKAV AI: Interactive Generative Model and HTML Extractor

Welcome to SKAV AI, your gateway to interactive generative models and effortless HTML extraction from web pages! SKAV AI offers a sleek and user-friendly interface built with PyQt5, enabling seamless interaction with powerful generative models and effortless extraction of HTML content from URLs.

### Installation and Setup

To get started with SKAV AI, ensure you have the following prerequisites installed:

- Python 3.x
- PyQt5
- requests
- google.generativeai
- IPython
- textwrap
- webbrowser

You can install the necessary dependencies using pip:

```bash
pip install PyQt5 requests google
```

### Usage

Explore the exciting features of SKAV AI:

1. **Run the Application**: Launch SKAV AI by executing the Python script `skav_ai.py`.

2. **Main Window**: Experience the intuitive main window equipped with various input fields and buttons.

3. **Generating Responses**:
   - Input a URL in the "Enter URL" field.
   - Click on "Extract Code from URL" to effortlessly retrieve HTML content from the provided URL.
   - Pose your inquiries in the "Ask the model a question" field.
   - Initiate response generation by clicking on "Generate Response".

4. **Additional Features**:
   - Access related resources effortlessly via dedicated buttons:
     - StarGPT
     - Star-MGPT
     - DataVerse AI
     - Ulink

5. **Splash Screen**: Be greeted by a captivating splash screen featuring an image, providing an engaging start to your SKAV AI journey.

6. **Styling**: Immerse yourself in the visually appealing interface and beautifully styled buttons, enhancing your user experience.

### API Configuration

Prior to utilizing the generative model, configure the API key using the following method:

```python
configure(api_key='Your Google AI API key')
```

### Classes and Methods

- **GenerativeApp Class**: Embodies the essence of the main application window.
  - **Methods**:
    - `show_main_window()`: Unveils the main window of the application.
    - `setup_additional_buttons(layout)`: Elevates user experience with additional buttons for accessing related resources.
    - `get_button_style(color)`: Elevates button aesthetics with custom CSS styling.
    - `open_url(url)`: Seamlessly opens URLs in the default web browser.
    - `generate_response()`: Unleashes the power of generative models to craft responses based on user queries.
    - `extract_html()`: Simplifies HTML content extraction from specified URLs.

### External Dependencies

- PyQt5: Facilitates seamless integration with the Qt application framework.
- requests: Empowers effortless HTTP requests.
- google.generativeai: Unlocks the potential of Google's generative models.
- IPython.display: Enhances user experience with captivating Markdown content display.
- textwrap: Provides elegant text wrapping and formatting capabilities.
- webbrowser: Streamlines URL navigation with effortless web page openings.

### Conclusion

SKAV AI redefines the landscape of interactive generative models and HTML extraction, offering an immersive and enriching user experience. Dive into the world of AI-powered capabilities with SKAV AI and unlock endless possibilities in content generation and extraction. Let SKAV AI be your companion in the journey towards innovation and discovery!
