from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import tools
from crewai_tools import PDFSearchTool, FileWriterTool
from pathlib import Path
from crewai import LLM

llm = LLM(
    model="gpt-3.5-turbo",
    temperature=0.8,
    max_tokens=4000 ,
    top_p=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.1,
    seed=42
)




SCRIPT_DIR = Path(__file__).parent.joinpath('files')
pdf_path = str(SCRIPT_DIR / "plans.pdf")

pdf_search_tool = PDFSearchTool(pdf=pdf_path)

    

@CrewBase
class DataprocessingCrew():
    """data_processing crew"""
    

 

    @agent
    def pdf_reader(self) -> Agent:
        return Agent(
            config=self.agents_config['pdf_reader'],
            tools=[pdf_search_tool], # add tools here or use `agentstack tools add <tool_name>
            verbose=True,
            llm = llm
            
            
        )


    @agent
    def data_cleaner(self) -> Agent:
        return Agent(
            config=self.agents_config['data_cleaner'],
            tools=[], # add tools here or use `agentstack tools add <tool_name>
            verbose=True,
            llm = llm
            
            
        )

    @agent
    def data_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['data_writer'],
            tools=[FileWriterTool()], # add tools here or use `agentstack tools add <tool_name>
            verbose=True,
            llm = llm
        )
        
        

    

    @task
    def read_pdf(self) -> Task:
        return Task(
            config=self.tasks_config['read_pdf'],
        )
        
    @task
    def get_relevant_data(self) -> Task:
        return Task(
            config=self.tasks_config['get_relevant_data'],
        )

   

    @task
    def write_to_file(self) -> Task:
        return Task(
            config=self.tasks_config['write_to_file'],
        )


   

    @crew
    def crew(self) -> Crew:
        """Creates the Test crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            
            verbose=True,
        )