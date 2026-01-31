# LangChain 集成案例

## 场景
使用 LangChain 构建 AI 应用

## 安装

```bash
pip install langchain openai
```

## 基本使用

### LLM 调用

```python
from langchain.llms import OpenAI

llm = OpenAI(model_name="gpt-4", temperature=0.7)

response = llm("用 Python 写一个快速排序")
print(response)
```

### Chat Model

```python
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

chat = ChatOpenAI(model_name="gpt-4", temperature=0)

messages = [
    SystemMessage(content="你是一个 Python 专家"),
    HumanMessage(content="解释一下装饰器是什么")
]

response = chat(messages)
print(response.content)
```

## 提示词模板

### PromptTemplate

```python
from langchain import PromptTemplate

template = """
请根据以下信息写一篇{length}的文章：

主题: {topic}
关键点:
{points}

文章：
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["length", "topic", "points"]
)

formatted_prompt = prompt.format(
    length="短篇",
    topic="人工智能",
    points="1. AI 发展历程\n2. 当前应用\n3. 未来展望"
)
```

### ChatPromptTemplate

```python
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个{role}专家，擅长用通俗易懂的语言解释专业概念。"),
    ("human", "请解释什么是{concept}？")
])
```

## 链 (Chains)

### 简单链

```python
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.7)
chain = LLMChain(llm=llm, prompt=prompt)

result = chain.run(length="中篇", topic="区块链", points="1. 定义\n2. 原理\n3. 应用")
print(result)
```

### Sequential Chain

```python
from langchain.chains import SequentialChain

# 链 1: 翻译
translation_chain = LLMChain(llm=llm, prompt=translation_prompt, output_key="chinese_text")

# 链 2: 总结
summary_chain = LLMChain(llm=llm, prompt=summary_prompt, output_key="summary")

# 组合
overall_chain = SequentialChain(
    chains=[translation_chain, summary_chain],
    input_variables=["english_text"],
    output_variables=["chinese_text", "summary"]
)

result = overall_chain({"english_text": "LangChain is a framework for developing applications powered by language models."})
```

## 文档加载器

```python
# 文本文件
from langchain.document_loaders import TextLoader
loader = TextLoader("article.txt")
documents = loader.load()

# PDF
from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("document.pdf")
pages = loader.load_and_split()

# 网页
from langchain.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://example.com/article")
documents = loader.load()
```

## 向量存储

```python
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(documents, embeddings)
results = vectorstore.similarity_search("AI 的应用", k=5)
```

## RAG 应用

```python
from langchain.chains import RetrievalQA
from langchain.indexes import VectorstoreIndexCreator

loader = TextLoader("knowledge.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    index=index,
    return_source_documents=True
)

result = qa_chain({"query": "什么是机器学习？"})
print(result["result"])
```

## 文件位置
`cases/ai-ml/langchain-integration.md`
