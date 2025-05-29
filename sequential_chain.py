from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain


def create_learning_chains(llm):
    """
    Create and return the three sequential chains for programming language learning
    
    Args:
        llm the initialized language model

    Returns:
        tuple:(roadmap_chain,schedule_chain,timeline_chian,sequential_chain)
    
    """


    roadmap_template = """
    You are an Instrutcor with year of experience teaching {language} to students

    Create a Comprehensive learning roadmap for someone who is a {experience_level} wanting to learn {language}

    The roadmap Should Include: 
    1. Prerequisite and setup requirements
    2. Fundamental concepts to master first
    3. Core programing concept
    4. Intermediate topics and practical applications
    5. Advanced Concepts and best practise
    6. Real-world projects to build
    7. Career opportunities and next steps

    Make a detailed and well-structured format with clear heading and bullet points
    Focus on practical learning with hands-on example and projects

    Language: {language}
    Experience Level: {experience_level}

    Learning Roadmap:
    
    """


    roadmap_prompt = PromptTemplate(
        input_variables=['language','experience_level'],
        template=roadmap_template
    )

    roadmap_chain = LLMChain(
        llm = llm
        prompt = roadmap_prompt,
        output_key = 'roadmap'
    )


    schedule_template = """
    Based on the following learning roadmap for {language}, create a detailed daily learning schedule.

    Learning Roadmap:
    {roadmap}

    Create a daily Learning plan considering:

    - The Learner {experience_level}
    - The {daily_hours} hours they can dedicate
    - Assign daily task by breaking down the roadmap
    - Include exercises for coding practise
    - Suggest break and review session
    - Provide weekly milestone

    Make the Schedule realistic, achievable, and engaging. Include these things:
    - Daily Learning Objectives
    - Time Allocation for each topic
    - Practical exercise and coding tasks
    - Review and practise session
    - weekly goals and check points
    
    Daily Learning Schedule
    """

    schedule_prompt =PromptTemplate(
        input_variables=['language','roadmap','experience_level','daily_hours']
        template = schedule_template
    )

    schedule_chain = LLMChain(
        llm = llm
        prompt = schedule_prompt
        output_key = 'schedule'
    )


    timeline_template = """
    Based on the learning roadmap and daily schedule for {language}, provide a realistic timeline estimation

    Learning Roadmap:
    {roadmap}

    Daily Schedule:
    {schedule}

    Consider:
    - Experience level: {experience_level}
    - Daily Time Commitment: {daily_hours} hours
    - Complexity of {language}
    - Time needed for practise and projects
    
    Provide a detailed timeline that includes:

    1. Total estimated time to basic proficiency
    2. Time to intermediate level
    3. Time to advanced/job-ready level
    4. Monthly milestone and achievements
    5. Factors that might affect the timeline
    6. Tips for staying on track

    Be Realistic and Encouraging. Explain what 'proficiency levels' mean in practical terms.

    Learning Timeline Estimation

    """
    
    timeline_prompt = PromptTemplate(
        input_variables=['language','roadmap','experience_level','daily_hours','schedule']
        template= timeline_template
    )

    timeline_chain = LLMChain(
        llm = llm
        prompt = timeline_prompt
        output_key = 'timeline'
    )

    sequential_chain = SequentialChain(
        chains = [roadmap_chain,schedule_chain,timeline_chain],
        input_variables = ['language','experience_level','daily_hours'],
        output_key = ['roadmap','schedule','timeline'],
        verbose = True
    )

    return roadmap_chain,schedule_chain,timeline_chain,sequential_chain


def get_supported_language():
    """
    Return a list of supported programing languages

    Returns:
        List: List of supported programing languages
    
    """

    return ["Python", "JavaScript", "Java", "C++","PHP", "Ruby",
        "TypeScript", "Swift"]

def validate_input(language,experience_level,daily_hours):
    """
    Validate the Parameters
    
    Args:
        language (str): Programming Language
        experience_level (str): Experience Level
        daily_hours (float): Daily hours commitment

    Returns:
        tuple: (is_valid,error_message)

    """

    supported_language = get_supported_language()
    valid_experience_level = [
        "Complete Beginner",
        "Intermediate",
        "Experienced in Other Language"
    ]

    if language not in supported_language:
        return False, f"Language {language} is not supported language: {', '.join(supported_language)}"
    
    if experience_level not in valid_experience_level:
        return False, f"Invalid Experience. Valid Experience levels are: {', '.join(valid_experience_level)}"
    
    if daily_hours < 0 or daily_hours > 24:
        return False, f"Daily Hours Must be a positive number between 0.1 to 24 hours"
    
    return True, ""


def create_custom_roadmap(llm,language,experience_level,daily_hours,focus_area = None):
    """
    
    Create a Custom Learning roadmap with specific focus areas
    
    Args:
        llm: the initialized Langugae model
        language (str) : Programming language
        experience_level (str) : Experience Level
        daily_hours (float) : Daily Hours Commitment
        focus_area (list) : Specific Areas to focus on (optional)
    
        
    Returns:
        dict: Generated Learning Plan
    """

    is_valid, error_msg = validate_input(language,experience_level,daily_hours)
    if not is_valid:
        raise ValueError(error_msg)
    
    roadmap_chain, schedule_chain, timeline_chain, sequential_chain = create_learning_chains(llm)

    chain_input = {
        "language" : language,
        "experience_level" : experience_level,
        "daily_hours" : daily_hours
    }

    try:
        result = sequential_chain(chain_input)
        return result
    except Exception as e:
        raise Exception(f"Error Generating Learning plan: {str(e)}")
    

def format_roadmap_output(roadmap_text):
    """Format the roadmap output for better display"""
    return roadmap_text.strip()

def format_schedule_output(schedule_text):
    """Format the schedule output for better display"""
    return schedule_text.strip()

def format_timeline_output(timeline_text):
    """Format the timeline output for better display"""
    return timeline_text.strip()
