from langchain_openai import ChatOpenAI
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
#from dotenv import load_dotenv
#load_dotenv()

#chatopenAI초기화
llm = init_chat_model(model="gpt-4o-mini",model_provider = "openai")   # 모델 이름 (gpt-4o-mini, gpt-4, gpt-3.5-turbo 등)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])

# 출력 파서 설정
output_parser = StrOutputParser()

#LLM 체인구성
chain = prompt | llm | output_parser
content = "코딩"
result = chain.invoke({"input": content+"에 대한 시를 써줘"})
print(result)  # 결과 출력

st.title("인공지능 시인")
content = st.text_input("시를 작성할 주제를 입력하세요")
st.write("시의 주제는", content)
st.markdown("_Streamlit_is :blue[cool] :sunglasses:", unsafe_allow_html=False)

if st.button("시 작성하기"):
 with st.spinner("시를 작성하는 중..."):
    result = chain.invoke({"input": content+"에 대한 시를 써줘"})
    st.write("작성된 시는 다음과 같습니다:")
    st.write(result)  # 결과 출력
