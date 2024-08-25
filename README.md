# EcoVision
## Inspiration
As a kid, I was terrible at distinguishing between recyclable and non-recyclable materials so I would often just throw it in the waste section. However, this isn’t only an issue with children, as people of all ages still participate in improper recycling practices. Thus, leading me to build EcoVision to provide accessible and responsive tools that encourage eco-friendly practices.

## What it does
EcoVision is a web application that uses real-time video analysis to classify objects as wasteful or recyclable. By leveraging advanced machine learning models, EcoVision provides instant feedback, helping users accurately sort their materials and manage waste effectively.

## How I built it
Flask for handling web server operations and routing.
OpenCV for capturing and processing real-time video feeds.
TensorFlow and MobileNetV2 for machine learning-based object classification.
SocketIO for real-time communication between the server and the web client.
HTML, CSS for the front-end interface.
Javascript to handle back-end connections between the python and HTML
Voiceflow for the AI Assistant

## Challenges I ran into
One of the main challenges was achieving accurate object classification in real-time. Ensuring that the AI model could correctly identify a wide range of materials under different lighting conditions required extensive testing and tuning. Additionally, integrating real-time video processing with web technologies posed technical challenges, particularly in maintaining smooth performance and minimising latency. 
Training the AI Assistant was also a challenge as there was a lot of information that needed to be created and passed on to the AI Assistant in order for it to provide accurate and useful information to the user.

## Accomplishments that I am proud of
I am proud of achieving real-time classification with a high degree of accuracy and creating a website that had a clean design that supported the environmentalism theme of the project. Achieving real-time communications from the python code and logic to the website was also something that took a lot of time. Additionally, training the AI Assistant to provide comprehensive responses to the user was something I am proud of.

## What I learned
Throughout the development process, I learned valuable lessons about combining various technologies to solve complex problems. I gained insights into optimizing machine learning models for real-time use, integrating different tech stacks, and addressing user experience challenges. The project also highlighted the importance of thorough testing and iterative improvements in achieving a polished final product.

## What's next for EcoVision
Future plans for EcoVision include expanding the range of detectable materials and improving the accuracy of the AI model. We also aim to enhance the user interface and add features like personalized recycling tips and analytics. Additionally, we are exploring opportunities to integrate EcoVision with smart home systems and extend its capabilities to support more advanced waste management solutions.


https://github.com/user-attachments/assets/a84385dd-1332-4691-88b2-8e8fac36b5fb

