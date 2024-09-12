

# **Bharat Ke Laadlo Ke Naam Prastut GramShiksha: Providing Fast Education To Remotest Places**  
**Low-Bandwidth Solutions for Interactive Education**




## **PROBLEM STATEMENT**
![focus](https://github.com/user-attachments/assets/1ac367d5-52b7-4f04-a56a-8f52986b34fa)


- **Inadequate Educational Infrastructure:** Rural areas in India lack sufficient physical infrastructure such as classrooms and facilities, which limits access to quality education.
- **Limited Internet Connectivity:** Not all villages and towns in India have access to 4G networks or even 3G in some cases.
- **Insufficient Resources:** Schools in rural areas often struggle to provide up-to-date resources, which affects their education quality.
- **User Engagement:** Even if online resources are provided, maintaining student engagement is challenging.

## **OBJECTIVES**
1. **Identify At-Risk Students:** Help identify students who are weaker, have lower attendance, or are at risk of dropping out and improve engagement.
2. **Enhance Resource Access:** Improve access to quality resources for children in rural areas.
3. **Implement Low-Internet Services:** Develop solutions that function well with limited internet connectivity.
4. **AI-Generated Resources:** Provide a one-stop solution for teachers and students with AI-generated resources, saving time and cost compared to physical resources.
5. **Analytics for Decision Making:** Provide detailed analytics on student demographics to aid in decision-making and resource allocation.


## **ARCHITECTURE AND USE CASES**

- ![SIH2024-Page-1 drawio (2)](https://github.com/user-attachments/assets/fb76366d-300e-4f90-b67a-0e9379ba1bff)

## **METHODOLOGY TECH STACK**
- **Web Development:**
  - **Technologies:** Next.js, Flask, Tailwind CSS
- **Generative AI / Machine Learning:**
  - **Models:** Whisper Speech-to-Text, Azure Image Captioning, Mistral 7B LLM, Scikit Learn, Gemini, LangChain, Chroma
  - **Features:**
    1. **Accurate Transcription Generation:** Utilize Whisper Speech-to-Text & Azure Image Captioning model to transcribe spoken content and images from videos into textual format.
    2. **Multi-model Video Summarization:** Combines video frame extraction with transcription analysis for a detailed video summary.
    3. **Gamified Question Generation:** Using Mistral 7B LLM to generate MCQ questions at intervals of 2-5 minutes based on the summary.
    4. **Concept Visualization:** Essential concepts are identified through keyword extraction, and images are generated.
    5. **Flowchart and Notes Generation:** Develop flowcharts and class notes summarizing key concepts and visualizing content structure.
    6. **Engagement Analytics:** Monitor engagement throughout the video and report appropriate feedback to teachers.
- **Low Latency Smart Board:**
  - **Technologies:** WebSockets/WebRTC for audio streaming, pre-downloaded PPT slides
- **Deployment:**
  - **Platforms:** Azure CDN, Docker, Vector DB Atlas, Azure App Services
  - **Database:** MongoDB Atlas, Chroma

## **UNIQUENESS**
1. **Lower Internet Consumption:** Provides remote online classes using just 60-100 MB of data per hour, significantly less than the typical 600 MB-1 GB.
2. **Adaptive Learning Quiz Module:** Developed an adaptive learning quiz system where the difficulty of the next question is determined by the accuracy of previously answered questions.
3. **Individual Attention and Counseling:** Focus on weaker students through engagement, score, and attendance analytics. Offers 1-to-1 counseling by teachers and doubt sessions.
4. **Visualization of Key Concepts:** Generation of images related to key concepts taught in the video, helping students visualize key points.
5. **After-Class Comprehensive Notes:** Streamlined post-lecture review with AI-generated class notes, mind maps, and flowcharts.
6. **Doubts Assistant and Career Guidance Companion:**
   - **Chatbot:** Introduce a RAG-based chatbot trained on platform content to swiftly address student queries.
   - **Career Guidance AI Avatar:** Helps students in choosing careers and assists in personality development.

## **DEPENDENCIES**
- **Cost Management:** Ensuring that the cost for the platform remains manageable. Most materials like MCQs, images, and notes are generated once and stored in Azure Blob and MongoDB Atlas while videos are uploading.
- **Scalability:** Ensuring that databases are deployed on the cloud to balance user load and maintain system scalability.

## **REFERENCES**
1. [AI-Generated Resources and Utilization](https://docs.google.com/document/d/14re6fryT5AbtQjucr57YsmUxMyIjwWaGiusrRAzYcGs/edit?addon_store)
2. [Bandwidth Reduction and Low Latency Streaming](https://docs.google.com/document/d/1nz2BZhKVGAW2OFdqejp5t70CiXt33XkHybpRM6g80zU/edit)

## **BUSINESS RELEVANCE**
- **PaaS:** Our software can function as a Platform as a Service (PaaS) option for low-latency internet networks in rural India.
- **SaaS:** The Engagement Enhancer Module can be integrated into smaller edtech platforms and educational institutions as APIs, tailored to their needs.

## **FUTURE WORK**
- **WebSocket/RTC and ML Integration:** Integrate WebRTC and ML-based models in cameras before videos are sent over the internet. Where full software integration is not possible, models can be used separately with existing services.


## **DEMO VIDEO**
(Watch the demo video on 2X speed if you prefer.t.)
- **Demo Video:** [Watch the demo video](https://www.youtube.com/watch?v=6yJG-DD2b1E)

- IF YOU WANT TO SEE IMAGES, YOU CAN GO TO #IMPLEMENTATION FROM THE TABLE OF CONTENTS OR WATCH THE VIDEO.

[![Watch the demo video]![thumbnail](https://github.com/user-attachments/assets/4a081e46-4828-4e7f-9201-dcf3829fd572)
()](https://www.youtube.com/watch?v=6yJG-DD2b1E)

## **PPT LINK: Edu-connect Prototype**
- [View and Download the PPT Presentation](https://docs.google.com/presentation/d/1FqkkNUAilG22GKpzLw2jHc6gS9xH3AO7hKw9quA5CWw/edit#slide=id.g78bebef4de_0_41)






## **System Architecture**

1. **Segmented Video Content:**
   - Videos are segmented to generate targeted quizzes and analyses.
2. **Real-Time Analytics:**
   - Insights into student engagement and learning patterns.

---

## **Research and Innovations**

1. **AI-Driven Transcription and Summarization:**
   - **Tools:** [Whisper](https://openai.com/research/whisper) for speech-to-text, [Azure Image Captioning](https://learn.microsoft.com/en-us/azure/cognitive-services/computer-vision/overview) for generating textual descriptions of images.
   - **Innovation:** Generates video summaries and interactive content.

2. **Question Generation:**
   - **Tools:** [Mistral 7B LLM](https://mistral.ai) for creating MCQs.
   - **Innovation:** Provides quizzes based on video content.

3. **Concept Visualization:**
   - **Tools:** [AI](https://www.tensorflow.org/) for visual aids and detailed notes.
   - **Innovation:** Creates flowcharts and summaries for better understanding.

4. **Engagement Monitoring:**
   - **Tools:** Real-time analytics for tracking student engagement.
   - **Innovation:** Offers feedback to improve the learning experience.

5. **Adaptive Quiz Module:**
   - **Tools:** [Scikit Learn](https://scikit-learn.org/) for adaptive quiz difficulty.
   - **Innovation:** Personalizes quizzes based on student performance.

6. **Real-Time Query Resolution:**
   - **Tools:** [RAG-based chatbot](https://huggingface.co/docs/transformers/model_doc/rag) for instant support.
   - **Innovation:** Provides real-time answers and assistance.

---

## **Technology Stack**

### **Web Development**

- **Front-End:** [Next.js](https://nextjs.org/), [Tailwind CSS](https://tailwindcss.com/)
  - **Usage:** For server-side rendering, dynamic content, and responsive UI.
- **Back-End:** [Flask](https://flask.palletsprojects.com/)
  - **Usage:** For creating a scalable backend and integrating AI models.

### **Generative AI / Machine Learning**

- **Models:**
  - **[Whisper](https://openai.com/research/whisper):** For speech-to-text transcription.
  - **[Azure Image Captioning](https://learn.microsoft.com/en-us/azure/cognitive-services/computer-vision/overview):** For generating textual descriptions of images.
  - **[Mistral 7B LLM](https://mistral.ai):** For creating multiple-choice questions (MCQs).
  - **[Scikit Learn](https://scikit-learn.org/):** For machine learning algorithms in data analysis.
  - **[Gemini](https://www.google.com/search/about/):** For advanced analytics and content generation.
  - **[LangChain](https://www.langchain.com/):** For language model integration.
  - **[Chroma](https://chroma.com/):** For vector-based data storage and retrieval.

### **Deployment**

- **Platforms:**
  - **[Azure CDN](https://azure.microsoft.com/en-us/services/cdn/):** For efficient content delivery and low latency.
  - **[Docker](https://www.docker.com/):** For application deployment and scaling.
  - **[Vector DB Atlas](https://www.mongodb.com/atlas):** For managing vector-based data.
  - **[Azure App Services](https://azure.microsoft.com/en-us/services/app-service/):** For hosting and managing the web application.
- **Database:**
  - **[MongoDB Atlas](https://www.mongodb.com/atlas):** For storing educational content and user data.
  - **[Chroma](https://chroma.com/):** For vector-based data storage and retrieval.

---

## **Unique Features**

1. **Low Internet Consumption:** Optimized content delivery for low-bandwidth environments.
2. **Adaptive Learning Module:** Customizes quiz difficulty to individual needs.
3. **Personalized Attention:** Provides detailed analytics for tailored support.
4. **Visualization Tools:** AI-generated images and notes to enhance learning.
5. **Custom Flowcharts:** Summarizes content visually for better comprehension.

---

## **Plans for Remote Education**

### **Plan 1: Smartboard + Pre-Downloaded PPT + Audio**

- **Components:** WebSockets/WebRTC for audio; smartboard for PPT slides.
- **Implementation:** Audio streaming with pre-downloaded slides.
- **Advantages:** Low bandwidth, no live slide synchronization needed, high-quality playback via CDN.

### **Plan 2: Real-Time Online Classes with WebRTC/FFmpeg**

- **Components:** WebRTC for live streaming; FFmpeg for encoding.
- **Implementation:** Real-time interaction with no slide synchronization.
- **Advantages:** Interactive experience with minimal latency.

---

## **Technology Comparison**

### **FFmpeg vs. WebRTC vs. WebSocket**

- **FFmpeg:** Media processing, moderate latency, high scalability, and reliability.
- **WebRTC:** Real-time peer-to-peer communication, low latency, encrypted, challenging scalability.
- **WebSocket:** Real-time client-server communication, low latency, high reliability with TCP.

### **Data Usage Comparison**

| **Technology** | **Type**        | **Latency** | **Resolution** | **Data Usage (per hour)** |
|----------------|-----------------|-------------|----------------|---------------------------|
| Google Meet    | Video + Audio   | 500 ms       | 360p-1080p     | 0.6-4 GB                  |
| WebRTC         | Video + Audio   | 100-500 ms   | 720p/1080p     | 1.5-6 GB                  |
| WebSocket      | Video + Audio   | 100-500 ms   | 720p/1080p     | 1.5-6 GB                  |

---

## **Advantages of Azure CDN**

- **Global Reach:** Efficient content delivery worldwide.
- **Low Latency:** Reduces delays and buffering.
- **Scalability:** Handles large traffic volumes.
- **High Availability:** Reliable access, minimizing downtime.
- **Cost Efficiency:** Reduces bandwidth and infrastructure costs.

---

## **Reducing Data Usage**

- **Issue:** High data usage during screen sharing.
- **Solution:** Pre-download PPTs and use a single variable slide number broadcasted via WebSocket.

---

## **AI-Generated Resources**

- **Multiple Choice Questions:** Adaptive difficulty based on lecture content.
- **AI-Generated Notes:** Summarized notes based on lectures.
- **AI-Generated Flow Diagrams:** Summarized and keyword-limited diagrams.
- **Doubt Solving Chatbot:** RAG-based chatbot for lecture-related doubts.
- **Image Visualizations:** Automated visual aids.

---

## **Previous Methodology**

- **Old Approach:** NLP-based question generation was resource-intensive and inaccurate.
- **New Approach:** LLMs like LLAMA and Gemini for improved results.

---

## **Business Relevance**

### **Platform as a Service (PaaS)**

- **Low-Latency Solutions:** Offer scalable educational solutions for rural areas with limited internet.

### **Software as a Service (SaaS)**

- **Integration with EdTech Platforms:** APIs for integration with smaller edtech platforms and institutions.

### **Cost Efficiency**

- **Reduced Physical Resource Costs:** Minimizes the need for physical resources using AI-generated content.

---

## **Future Enhancements**

### **Augmented Reality (AR) and Gamified Learning**

- **Advanced Integration:** Explore AR and gamified learning tools for enhanced educational experiences.

### **Expansion to Additional Tools**

- **New AI Models:** Integrate new tools and models to further enhance learning and engagement.

---

## **Contact and Further Information**

For more details, contact us or visit our website.

---

