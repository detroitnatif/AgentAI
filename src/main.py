from textwrap import dedent
from crewai import Task

class MeetingPrepTasks():
    def research_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description=dedent(f'''\
            Conduct comprehensive research on all the meeting participants and companies involved
            including personal achievements, proffesional background, and any relevant business activities.
            participants: {meeting_participants}
            meeting context: {meeting_context}'''),
            expected_output=dedent(f'''\
            A detailed report summarizing key findings of each participant and company, highlighting information'''),
            agent=agent,
            async_execution=True
)
    
    def industry_analysis_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description=dedent(f'''\
            Analyze the market in question and do comprehensive research on all companies involved
            by using market reports, recent developments, and expert opinions
            participants: {meeting_participants}
            meeting context: {meeting_context}'''),
            expected_output=dedent(f'''\
            A detailed report summarizing key findings from market research that identifies
            major trends, potenital challenges, and strategic oppurtunites'''),
            agent=agent,
            async_execution=True,
)
    
    def meeting_strategy(self, agent, meeting_participants, meeting_context):
        return Task(
            description=dedent(f'''\
            Create a schedule of talking points for this upcoming meeting as well as questions
            to ask and discussion angles based on the analysis conducted.
            participants: {meeting_participants}
            meeting context: {meeting_context}'''),
            expected_output=dedent(f'''\
            Create a detailed report of talking points, questions, and discussion angles 
            based on the analysis conducted.'''),
            agent=agent,
)
    def summarize_meeting(self, agent, meeting_participants, meeting_context):
        return Task(
            description=dedent(f'''\
            Write a summary of all the things that need to be covered in this meeting in 
            a well structured document that is easy to digest and equips the participants
            with neccassary information and strategies.
            participants: {meeting_participants}
            meeting context: {meeting_context}'''),
            expected_output=dedent(f'''\
            Create a detailed report of talking points, questions, and discussion angles 
            based on the analysis conducted.'''),
            agent=agent,
)

