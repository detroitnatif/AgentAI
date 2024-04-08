from dotenv import load_dotenv
from crewai import Crew
from tasks import MeetingPrepTasks
from agents import MeetingPrepAgent


def main():
    load_dotenv()
    print("Welcome to the Crew")
    print('---------------------')
    # meeting_participants = input("who is attending the meeting?")
    # meeting_context = input("what is the context of this meeting?")
    # meeting_objective = input('What is your objective for this meeting?')

    meeting_participants = 'Ted Sarandos'
    meeting_context = input("what is the context of this meeting?")
    meeting_objective = input('What is your objective for this meeting?')

    tasks = MeetingPrepTasks()
    agents = MeetingPrepAgent()

    research_agent = agents.research_agent()
    industry_analysis_agent = agents.industry_analysis_agent()
    meeting_strategy_agent = agents.meeting_strategy_agent()
    summarize_agent = agents.summarize()

    research_task = tasks.research_task(research_agent, meeting_participants, meeting_context)
    industry_analysis_task = tasks.industry_analysis_task(industry_analysis_agent, meeting_participants, meeting_context)
    meeting_strategy_task = tasks.meeting_strategy(meeting_strategy_agent, meeting_participants, meeting_objective)
    summarize_meeting_task = tasks.summarize_meeting(summarize_agent, meeting_participants, meeting_objective)

    meeting_strategy_task.context = [research_task, industry_analysis_task]
    summarize_meeting_task.context = [research_task, industry_analysis_task, meeting_strategy_task]

    crew = Crew(
        agents=[research_agent, industry_analysis_agent, meeting_strategy_agent, summarize_agent],
        tasks= [research_task, industry_analysis_task, meeting_strategy_task, summarize_meeting_task]
    )
    result = crew.kickoff()
    print(result)
if __name__ == '__main__':
    main()