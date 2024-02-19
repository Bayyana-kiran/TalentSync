# Blue Bit Round-1


# TalentSync: Resume Analyzer for Enhanced Talent Acquisition
## Overview:

This project implements a machine learning model capable of classifying the domain of a resume and analyzing the personality traits of the resume holder. The model utilizes Natural Language Processing (NLP) techniques and employs a one-vs-all classification approach using logistic regression. Additionally, Gaussian analysis is used to further understand the personality characteristics inferred from the resume content.

## Features:
1. Resume Domain Classification: The model can classify resumes into different domains based on their content, allowing for efficient sorting and analysis.
2. Personality Analysis: By analyzing the language used in the resume, 3. the model can infer personality traits of the resume holder, providing additional insights for recruiters or HR professionals.
4. NLP Techniques: Natural Language Processing techniques are employed to preprocess and extract meaningful features from the resume text.
5. One-vs-All Classification: Logistic regression with a one-vs-all approach is used for multi-class classification, enabling accurate domain classification.
6. Gaussian Analysis: Gaussian analysis is utilized to further analyze the personality traits inferred from the resume content, providing a deeper understanding of the individual's characteristics.

## Usage:
1. Input: Provide a resume document as input to the model.
2. Processing: The model preprocesses the resume text using NLP techniques.
3. Classification: It classifies the resume into one of the predefined domains using logistic regression.
4. Personality Analysis: The model analyzes the language and infers personality traits of the resume holder.
5. Output: The model generates classification results indicating the domain of the resume and personality traits inferred.

## Screening Resume:

- This project entails text classification utilizing TF-IDF vectorization and logistic regression. Initially, data was sourced from Kaggle, ensuring its relevance to the classification task at hand. 
- The data underwent rigorous preprocessing to eliminate errors, punctuation, numeric, and symbols, thereby cleaning it for further analysis. Subsequently, tokenization techniques, including word tokenization and lemmatization, were employed to break down the text into individual words and normalize them to their base form, respectively. 
- Following this, TF-IDF (Term Frequency-Inverse Document Frequency) vectorization was applied to convert the text data into numerical features, resulting in approximately 20,000 features representing the text corpus. 
- For classification purposes, a one-vs-all classification strategy was adopted, leveraging logistic regression due to its simplicity and effectiveness in multi-class classification tasks.


### Output:
![WhatsApp Image 2024-02-19 at 4 25 35 PM (1)](https://github.com/Bayyana-kiran/TalentSync/assets/99533113/116817cb-a476-4c5c-a626-d2d0abf819e9)
![WhatsApp Image 2024-02-19 at 4 27 15 PM](https://github.com/Bayyana-kiran/TalentSync/assets/99533113/54e7b8dc-2ed1-4643-8ff7-abc4a2d050d0)


### Explaination of Output: 
The output of this project provides a summary of the information extracted from a resume. It includes a list of skills, organizations, and educational background found in the resume. Additionally, the output indicates the category that best matches the resume, helping users understand the type of job or role the applicant may be suitable for. The interactive visualizations further enhance the understanding of the resume by presenting the extracted information in a more accessible and engaging format, making it easier for users to analyze and evaluate resumes effectively.




## Trait Based Analysis and Behavioral Detection:
- The machine learning model build using NLP techniques is used to analyze the resume and find the personality levels of the person. It's used to find the level of openness, whether the person is neurotic, the levels of agreeableness of the person, is the person conscientious, is the person open to new experiences. 
- The machine learning algorithm used for the task is Gaussian Naive Bayes Algorithm. The text is first preprocessed by removing the punctuations, stop words and then the text is tokenized and lemmatized using NLTK and the Word2Vector algorithm is used to convert the text into vectors. Then the Gaussian Naive Bayes Algorithm is applied to train upon this data.

### Output:
![WhatsApp Image 2024-02-19 at 4 05 21 PM](https://github.com/Bayyana-kiran/TalentSync/assets/99533113/1d461ad5-985c-423a-a12a-fe392a991c0e)
![WhatsApp Image 2024-02-19 at 4 05 21 PM (1)](https://github.com/Bayyana-kiran/TalentSync/assets/99533113/0d73451f-a928-41ea-b037-81c0999f9760)
![WhatsApp Image 2024-02-19 at 4 05 21 PM (2)](https://github.com/Bayyana-kiran/TalentSync/assets/99533113/c810161c-fabf-4507-85be-b016b5715b50)
![WhatsApp Image 2024-02-19 at 4 05 21 PM (3)](https://github.com/Bayyana-kiran/TalentSync/assets/99533113/5bfc12a7-4689-47eb-9553-4b30d9fe88a8)
![WhatsApp Image 2024-02-19 at 4 04 54 PM](https://github.com/Bayyana-kiran/TalentSync/assets/99533113/fa4fbf7a-fa9e-465d-bbf0-ff10c4427175)


### Explaination of Output:
The images display the level of accuracy of the machine learning model in identifying the personality traits. The accuracy level of the Machine learning model can increased further as it's used for more prediction tasks. The machine learning model gives the probability levels of each personality trait for a person. For example, in the output, if the openness probability is 73.27 then the person is 73.27% open to new experiences.


## Compatibility for future Tech Stack & Explaination of Output:

Our resume analyzer, built using Python, is a sophisticated tool designed to streamline the hiring process by efficiently evaluating job applicants' resumes and determining their compatibility with specific tech stacks. Leveraging advanced natural language processing (NLP) techniques, our system parses through resumes to extract key information such as skills, experience, and education. It then utilizes machine learning algorithms to analyze this data against predefined criteria for various tech stacks, providing employers with insightful compatibility scores for each applicant. By automating this process, our tool empowers recruiters to quickly identify promising candidates, saving time and resources while ensuring a more effective hiring decision-making process


### Output :
![WhatsApp Image 2024-02-19 at 5 04 21 PM](https://github.com/Bayyana-kiran/TalentSync/assets/99533113/7a119f8d-bcc2-423f-a6bf-640726a4330e)


## Dependencies:
Python 3.x
Libraries: NumPy, pandas, scikit-learn, NLTK, etc




