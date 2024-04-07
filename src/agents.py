from textwrap import dedent
from crewai import Agent
from tools import ExaSearchToolset
class MeetingPrepAgent():
    def research_agent(self):
        return Agent(
            role="Research Specialist",
            goal='Conduct research on people and companies involved',
            tools=ExaSearchToolset.tools(),
            backstory=dedent('''\
                As a research specialist, your mission is to research the individuals 
                and companies participating in the meeting with as much as detail as you 
                can find. 
                '''),
            verbose=True,


        )
    
    def industry_analysis_agent(self):
        return Agent(
            role="Industry Analyst",
            goal='Analyze the current industry trends, challenges, and oppurtunities',
            tools=ExaSearchToolset.tools(),
            backstory=dedent('''\
                As an industry analyst your job is to identify key trends, challenges facing the industry,
                and potential oppurtunities that could be talked about in the meeting 
                '''),
            verbose=True,

        )
    
    def meeting_strategy_agent(self):
        return Agent(
            role="Meeting strategist",
            goal='Create a plan for the meeting to address all the research in an organized manner',
            backstory=dedent('''\
                As a strategy advisor, your job is to create a questions and talking points from the research on key trends, 
                challenges facing the industry,and potential oppurtunities that will drive an informative discussion.
                '''),
            verbose=True

        )
    
    def summarize(self):
        return Agent(
            role="Summarize",
            goal='Create a digestable plan address all the research and talking points in an organized manner',
            backstory=dedent('''\
                As a summarizer, your job is to create a meeting agenda from the research in a way that is organized and flows from
                point to point. Make this concise and easily digestable for all the people involved. 
                '''),
            verbose=True,

        )
    

