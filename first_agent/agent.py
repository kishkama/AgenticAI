from google.adk.agents import Agent

def get_current_time(city: str) -> dict:
    """retrieve current time in the given city.
    :param city (str): city name for which to retrieve current time.:
    :return: dict: status and result
    """
    if city.lower() == 'london':
        return{
            'status': 'success',
            'time': '10 AM'
        }
    else:
        return{
            'status': 'error',
            'error_message': f"time in {city} is not available",
        }
def get_weather(city: str) -> dict:
    """retrieve current weather of the given city.
    :param city (str): city name for which to retrieve current weather.
    :return: dict: status and result
    """
    if city.lower() == 'london':
        return{
            'status': 'success',
            'report': f"Weather for the city {city} is currently available and its cloudy",
        }
    else:
        return{
            'status': 'error',
            'error_message': f"Weather for the city {city} is not available",
        }


root_agent = Agent(
    name = "weather_time_agent",
    model = "gemini-2.5-flash",
    description = ("agent to answer only weater quesion question"),
    instruction = (
        "you are a helpful agent to answer weather question"
    ),
    tools=[get_current_time, get_weather],
)