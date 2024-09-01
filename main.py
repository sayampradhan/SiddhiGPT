import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

st.title("SiddhiGPT")

# Set the default model
if "ollama_model" not in st.session_state:
    st.session_state["ollama_model"] = "mistral"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Define the prompt template
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer: 
"""
prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model=st.session_state["ollama_model"])
chain = prompt | model 

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
# Display user message immediately after input
if prompt := st.chat_input("You: "):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Prepare context
    context = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state.messages])

    
    # try:
        # Generate AI response
    if "your name" in prompt.lower():
        response = "My name is Siddhi, your helpful chatbot!"
    else:
        response = chain.invoke({"context": context, "question": prompt})
    
    # Add AI response to chat history with the name "Siddhi"
    st.session_state.messages.append({"role": "Siddhi", "content": response})
    
    # Display AI response with the name "Siddhi"
    with st.chat_message("Siddhi"):
        st.markdown(response)
    # except Exception as e:
    #     # Handle errors gracefully
    #     error_message = f"An error occurred: {str(e)}"
    #     st.session_state.messages.append({"role": "Siddhi", "content": error_message})
        
    #     with st.chat_message("Siddhi"):
    #         st.markdown(error_message)
