from setuptools import find_packages,setup
setup(name="medical-chatbot-assistant",
      version="0.0.1",
      author="nithishkumar",
      author_email="mnithish1231234@gmail.com",
      packages=find_packages(),
      install_requires=["langchain_huggingface","langchain_groq","langchain-community","langchain-core","fastapi[standard]","flask","uvicorn","sentence-transformers==4.1.0"])
