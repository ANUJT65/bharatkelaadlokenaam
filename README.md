

# **Bharat Ke Laadlo Ke Naam Prastut GramShiksha: Providing Fast Education To Remotest Places**  
**Low-Bandwidth Solutions for Interactive Education**
![Theme](https://github.com/user-attachments/assets/a52986d6-b3e1-421b-8366-5216c4ca3bc7)

## **Some Considerations before we begin**
- We are assuming that teachers are given sufficient resources/internet and also infra facilities to stream lectures
- Our Understanding is that we are providing remote education to students until government has enough data on student demographics/attendance etc to provide proper infrastructure to the students.

## **With these things in mind We have divided our project into 2 parts**
- **1)Live ( low latency ) streaming of video lectures Module with use of websockets/webrtc.**
- Here students will just join classroom and teacher would teach like in a regular meet but through low data consumption and better human interaction.
- **2)PreRecorded Lecture VideoPlayback/Engagement Enhancer Module using Azure CDN( low data consumption)**
- Here there is loads of ai generated resources, engagement enhancing resources which generate interests in learning and all given through lowest data consumption on a prerecorded lecture.


## **OUR FOCUS**

1. **Provide AI-Generated Resources:** Provide a one-stop solution for teachers and students with AI-generated resources, saving time and cost compared to physical resources.
2. **Implement Low-Internet Services:** Develop solutions that function well with limited internet connectivity.
3. **Enhance Engagement(MAJOR PROBLEM IN ONLINE EDUCATION):** Even if we provide all resources , many students dont really utilize these things, so we have various modules to encourage students to learn.
4. **Identify At-Risk Students:** Help identify students who are weaker, have lower attendance, or are at risk of dropping out and improve engagement by 1 on 1 counselling by teachers.
5. **Analytics for Decision Making:** Provide detailed analytics on student demographics to aid in decision-making and resource allocation.

## **Our Unique Selling Proposition (USP)**

![USP](https://github.com/user-attachments/assets/6fc488a2-d893-4205-b1e7-4b1b37270ed9)

## **UNIQUENESS OF OUR SOLUTION**
1. **Lower Internet Consumption:(research is given below)**
   - Provides remote online classes using just **60-100 MB** of data per hour, compared to typical 600 MB-1 GB.
2. **Adaptive Learning Quiz Module:**
   - Developed an adaptive learning quiz system where the difficulty of the next question is determined by previously answered questions.
3. **Individual Attention and Counseling:**
   - Focus on weaker students through engagement, score, and attendance analytics. Offers 1-to-1 counseling and doubt sessions.
4. **Visualization of Key Concepts:**
   - Generation of images related to key concepts, helping students visualize key points.
5. **After-Class Comprehensive Notes:**
   - Streamlined post-lecture review with AI-generated class notes, mind maps, and flowcharts.
6. **RAG-Based Doubt Assistant:**
   - Introduce a RAG-based chatbot trained on platform content to swiftly address student queries.
7. **Vocational Learning AI Avatar:**
   - Helps students choose careers, assists in personality development, and vocational learning.


## **ARCHITECTURE AND USE CASES(PLEASE ZOOM IN/SCROLL IN)**

- ![SIH2024-Page-1 drawio (2)](https://github.com/user-attachments/assets/fb76366d-300e-4f90-b67a-0e9379ba1bff)

## **METHODOLOGY TECH STACK**
![Methodology](https://github.com/user-attachments/assets/570f010d-59ab-4e7d-aa0b-d7bc238f2644)



## (For low latency research details scroll down, we have a great innovation)




## OUR RESEARCH ON LOW LATENCY VIDEO STREAMING
**Optimized for Low Data Usage and Enhanced Remote Education**
# Comparison of Our Platform with Google Meet
---
## **How We Reduced Data Usage**

Our platform uniquely addresses data consumption issues, which is a major concern in remote education:


**1) Pre-Downloaded PowerPoint Slides:** (Consumption of data 40-50 mb per hour)
- To optimize data usage, our solution pre-downloads the PowerPoint slides and broadcasts only the slide number that changes.
- This approach significantly reduces the data required for streaming.
- The slide number update is communicated through **WebSocket**, ensuring that the React app synchronizes to the corresponding slide efficiently and **its streamed to all participants**
- Typical data usage is just 30-40 mb as slides switched are not too often and 10mb for ppt download
  
**2) Audio Streaming through WebRTC:** (Consumption of data 30-60 mb per hour)
- We use WebRTC for audio streaming, which ensures low latency and high-quality audio while minimizing data consumption.
  
**3) Jamboard Integration: (5-10 mb per hour)** 
- A streamlined version of Jamboard is included on the right side of the screen to assist teachers in explaining the content of the PowerPoint. This addition ensures that while the slides provide the primary content, the Jamboard supports interactive explanations.

- By focusing on these optimizations, we ensure that data usage remains minimal, with most streaming happening at low latency and with low data consumption.

---

## **Data Usage Comparison and Latency Comparison with existing platforms**

### **Google Meet**

| **Type**           | **Latency** | **Low Quality (360p)** | **Standard Quality (480p)** | **High Quality (720p)** | **HD Quality (1080p)** |
|--------------------|-------------|-------------------------|------------------------------|--------------------------|-------------------------|
| **Video + Audio**  | ~500 ms      |  1 GB per hour         | ~1 GB to 1.5 GB per hour     | ~1.5 GB to 2.5 GB per hour| ~2.5 GB to 4 GB per hour|

### **Our Platform ( Why we only considered websockets(for ppt state variable updation ) and webrtc ( for audio streaming)**

| **Technology**           | **Type**        | **Latency** | **Resolution** | **Data Usage (per hour)** |
|--------------------------|-----------------|-------------|----------------|---------------------------|
| **WebRTC Audio Only**    | Audio Only       | 100-300 ms   | N/A            | 30-60 MB                  |
| **WebSocket Audio Only** | Audio Only       | 100-300 ms   | N/A            | 30-60 MB                  |
| **WebRTC Video + Audio** | Video & Audio    | 100-500 ms   | 720p/1080p     | 1.5-6 GB                  |
| **WebSocket Video + Audio** | Video & Audio | 100-500 ms   | 720p/1080p     | 1.5-6 GB                  |

## This is the reason we only considred audio of webrtc + updation of slides through websockets so that we could have ultimate version of low latency online education.

---

## **Technology Comparison why we chose webrtc and websockets**

| **Feature/Aspect**        | **FFmpeg**                              | **WebRTC**                                | **WebSocket**                           |
|---------------------------|-----------------------------------------|-------------------------------------------|----------------------------------------|
| **Primary Use**           | Media processing, encoding, decoding    | Real-time peer-to-peer communication      | Real-time client-server communication  |
| **Communication Type**    | Typically client-server                 | Peer-to-peer                              | Client-server                          |
| **Protocols Used**        | RTMP, RTP, HTTP, RTSP                    | UDP (primarily), TCP                      | TCP                                    |
| **Latency**               | Moderate to high                        | Low latency                               | Low latency                             |
| **Reliability**           | High for media processing               | Less reliable with UDP (packet loss), more with TCP | High reliability with TCP     |

---

## **Advantages of Our Platform**


1. **Optimized Data Usage:** Our platform reduces data consumption by pre-downloading PowerPoint slides and synchronizing slide changes via WebSocket. This minimizes the bandwidth impact of screen sharing.
2. **Efficient Content Delivery:** Leveraging WebRTC for audio streaming and a streamlined Jamboard integration ensures a low-bandwidth, high-quality educational experience.
3. **Low Bandwidth Requirements:** Designed for low-bandwidth environments, our platform provides a smooth educational experience even in remote areas.
4. **High-Quality Playback:** Azure CDN ensures smooth video playback and reduces buffering.


---

## **Plan Part 1 : Smartboard + Pre-Downloaded PPT + Audio (100MB)**

- **Overview:** Integrates WebSockets/WebRTC for audio streaming and pre-downloaded PowerPoint slides.
- **Components:**
  - **Audio Streaming:** WebSockets/WebRTC for low-latency audio.
  - **PPT Slides:** Pre-downloaded slides with updates broadcasted via WebSocket.
- **Implementation:** Students access audio and slides with minimal data usage. Changes in slides are efficiently communicated to the React app.
- **Bandwidth Usage:**
  - **Audio Only:** ~30 MB - 60 MB per hour.
  - **PPT:** Minimal impact (pre-downloaded).

---
## **Plan part 2 : Enagement Enhancer Module(MAJOR DATA CONSUMPTION WILL ONLY BE IN RETRIEVAL OF RESOURCES)**
- SO After live stream teacher will upload the lecture  where azure cdn and engagement enhancer module will come to play

## **Advantages of Azure CDN for Remote Education for downloading of video/playback of video and also for scalability**
![third-system](https://github.com/user-attachments/assets/918a98ae-1d87-447c-9be9-692177a9d1f9)
src: https://litebreeze.com/blog/2020/11/27/scaling-your-web-applications/

1. **Global Reach:** Efficient content delivery worldwide, including remote areas.
2. **Low Latency:** Reduces delays and buffering, providing smooth access to educational content.
3. **Scalability:** Supports large traffic volumes and spikes.
4. **High Availability:** Ensures reliable access to resources with minimal downtime.
5. **Cost Efficiency:** Lowers bandwidth and infrastructure costs.

## **AI-Generated Resources**

Our platform includes advanced AI-generated resources to enhance the educational experience:
**We are applying RAGs on the transcription of the video + on the captions from video so that we can get better ai generated resources, you could even see in architecture diagram so all resources are generated using this, ensuring accuracy**

1. **Adaptive MCQS Which track Engagement throughout the videos:** Adaptive MCQs generated based on lecture content, increasing in difficulty as the user progresses.
2. **AI-Generated Notes:** Real-time note generation based on the ongoing lecture.
3. **AI-Generated Flow Diagrams and Process Flows:** Summarized and generated using nodes and connections for clear visualizations.
4. **Doubt Solving Chatbot:** RAG-based chatbot for addressing questions related to lecture content.
5. **Image Visualizations:** AI-generated visualizations to support lecture content understanding.
6. **Vocational Learning/Tests through AI Avatar Chatbot:** AI avatar teacher which would give insights on basis of tone of students and also responses given by them to the questions posed by ai avatar module great for personality development.
   ![quizsystem](https://github.com/user-attachments/assets/dd7965c1-5249-4c91-97e6-9d1ad21d77c5)
   ![summarygen](https://github.com/user-attachments/assets/84d1fb47-fc9e-4b5e-b56b-a454566371a3)
   ![doubtsassistant](https://github.com/user-attachments/assets/9d75218d-5eb6-4210-8cdf-30266c862b7e)
   ![engagement analysis](https://github.com/user-attachments/assets/be37fde9-1e05-48dc-8794-037ed6e177c8)


### **Previous Methodology(OUR TRIAL AND ERROR )**

- Previously, NLP-based methods were used for question generation, but they were resource-intensive and less accurate. 
- We transitioned to advanced LLMs like LLAMA and Gemini for better performance.
- We have gone from T5, to BERT to Mistral7B to Groq LLAMA and Gemini.
- So entire process of research has been done to get the best mcqs
## Questions model
![questionsmodel](https://github.com/user-attachments/assets/d78be147-b92e-44e2-9533-648f8a58f121)

Present Models how they generate content(all Rag based)
### Flow diagram and Image Generation module[RAGs based]

![FLOWFLOW](https://github.com/user-attachments/assets/ac51465c-f38a-4cb9-b247-ab03fce91b30)

## Notes Generation Module[RAGs based]
![notesmodel](https://github.com/user-attachments/assets/0ba94766-0a20-474f-8861-cc4dcaa31e33)


### **Business Aspects and Cost Analysis**

### **Cost Effectiveness ALL RESOURCES ARE GENERATED ONLY ONCE WHEN VIDEO IS UPLOADED TO SAVE COSTS**

- **AI-Generated Resources:** Created once and stored in Azure Blob Storage and MongoDB Atlas, reducing repeated generation costs and optimizing resource usage.
- **Storage Costs:** Utilizing Azure Blob and MongoDB Atlas for efficient and cost-effective storage.

### **SaaS Pass Model**

- **Subscription-Based Access:** Offers predictable costs and scalability for educational institutions.
- **Reduced Bandwidth Costs:** Optimized data usage lowers operational costs, making it a cost-effective solution for remote education.

---

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
=

