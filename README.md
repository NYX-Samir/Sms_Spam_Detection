# SMS Spam Detection

A **Real-Time SMS Spam Detection System** built using **Streamlit** and **Multinomial Naive Bayes (MNB)**.  
It classifies messages as **spam** or **ham** by analyzing text features using **CountVectorizer**.  

The project includes a **Streamlit Web App** for user input and instant predictions, with a simple and clean interface.  

---

## 📌 Features

- ✅ Real-Time SMS Classification  
- ✅ Preprocessing: cleaning, tokenization, normalization  
- ✅ Uses Multinomial Naive Bayes for prediction  
- ✅ Streamlit UI for easy interaction  
- ✅ Serialized model and vectorizer for fast loading  

---

## 🛠️ Tech Stack

- Python  
- scikit-learn (`MultinomialNB`, `CountVectorizer`)  
- pandas, numpy  
- Streamlit  
- Pickle (serialization)  

---

## 📂 Project Structure

### Mermaid Diagram
```mermaid
graph TD
  root[📂 Sms_Spam_Detection]
  root --> app[▶️ app.py]
  root --> utils[📄 text_utils.py]
  root --> data[📂 data]
  data --> spam_csv[📄 spam.csv]
  root --> model[📦 model artifacts]
  model --> model_pkl[📦 model.pkl]
  model --> vectorizer_pkl[📦 vectorizer.pkl]
  root --> notebooks[📂 notebooks]
  notebooks --> nb[📓 Spam detection.ipynb]
  root --> req[📝 requirements.txt]
