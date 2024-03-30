from flask import Flask, render_template, request
from langchain.llms import OpenAI
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import AgentType, Agent, Tool, initialize_agent, load_tools


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
      
        prompt= PromptTemplate.from_template("Provide an analysis on the sport {title}?")
        llm=OpenAI(temperature=0.3)
      
        chain=LLMChain(llm=llm,prompt=prompt)
        prompt = request.json.get('prompt')
        output= chain.run(prompt)
        
        return output
    else:
        return jsonify({"error": "Invalid request method"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)