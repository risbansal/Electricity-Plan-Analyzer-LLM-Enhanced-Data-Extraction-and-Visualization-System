from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import tools
from langchain_openai import ChatOpenAI

@CrewBase
class DataprocessingCrew():
    """data_processing crew"""

    def __init__(self) -> None:

        # Ollama
        self.ollama_llm = ChatOpenAI(
            model="mistral",
            base_url="http://localhost:11434/v1",
            api_key="ollama",  # something random
            temperature=0,
        )

    

    # Agent definitions
    @agent
    def data_collector(self) -> Agent:
        return Agent(
            config=self.agents_config['data_collector'],
            tools=[tools.file_read_tool, tools.web_crawl, tools.web_scrape
    ],  # Pass in what tools this agent should have
            # llm = self.ollama_llm,
            verbose=True,
            
            
        )

    # @agent
    # def data_analyzer(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['data_analyzer'],
    #         tools=[], # add tools here or use `agentstack tools add <tool_name>
    #         verbose=True,
    #     )

    # @agent
    # def data_writer(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['data_writer'],
    #         tools=[tools.composio_tool], # add tools here or use `agentstack tools add <tool_name>
    #         verbose=True,
    #     )
        
    

    # @agent
    # def graph_creator(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['graph_creator'],
    #         tools=[tools.web_scrape, tools.web_crawl, tools.retrieve_web_crawl], # add tools here or use `agentstack tools add <tool_name>
    #         verbose=True,
    #     )

    # Task definitions
   
    @task
  
    @task
    def read_efl(self) -> Task:
        return Task(
            config=self.tasks_config['read_efl'],
        )

    # @task
    # def get_relevant_data(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['get_relevant_data'],
    #     )

    # @task
    # def write_to_file(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['write_to_file'],
    #     )

    # @task
    # def create_graph(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['create_graph'],
    #     )

    @crew
    def crew(self) -> Crew:
        """Creates the Test crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            
            verbose=True,
        )