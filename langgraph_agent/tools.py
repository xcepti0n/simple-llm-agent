
from langchain_core.tools import tool
import datetime

@tool
def get_current_time() -> dict:
    '''
    This tool gets the current local time using system commands.
    '''
    now = datetime.datetime.now()
    return {"current_time": now.strftime("%Y-%m-%d %H:%M:%S")}