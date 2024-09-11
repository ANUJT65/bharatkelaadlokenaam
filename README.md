

# **Bharat Ke Laadlo Ke Naam Prastut GramShiksha: Providing Fast Education To Remotest Places**  
**Low-Bandwidth Solutions for Interactive Education**

## **TRACK CHOSEN**
![Track Image](https://your-image-link-here) <!-- Replace with actual track image link if available -->



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

## **INSIGHTS ON TRADITIONAL LEARNING**
1. **Student-Teacher Ratios:**
   - **Secondary Education:** The student-teacher ratio is notably higher, at 60:1, indicating larger class sizes and potentially reduced individualized attention.
   - **Online Education:** The ratio can be even higher, making individual attention for each student difficult.
2. **Internet Access:**
   - Many areas in India still lack sufficient internet networks.
   - During the COVID era, students in rural areas struggled with education due to inadequate internet connections and lower speeds.

## **ARCHITECTURE AND USE CASES**
- **Demo Video:** [Watch the demo video](https://www.youtube.com/watch?v=6yJG-DD2b1E)

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

- IF YOU WANT TO SEE IMAGES, YOU CAN GO TO #IMPLEMENTATION FROM THE TABLE OF CONTENTS OR WATCH THE VIDEO.

[![Watch the demo video]![thumbnail](https://github.com/user-attachments/assets/4a081e46-4828-4e7f-9201-dcf3829fd572)
()](https://www.youtube.com/watch?v=6yJG-DD2b1E)

## **PPT LINK: Edu-connect Prototype**
- [View and Download the PPT Presentation](https://docs.google.com/presentation/d/1FqkkNUAilG22GKpzLw2jHc6gS9xH3AO7hKw9quA5CWw/edit#slide=id.g78bebef4de_0_41)
