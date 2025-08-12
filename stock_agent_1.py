from phi.agent import Agent
from phi.model.groq import Groq
from dotenv  import load_dotenv
from phi.tools.yfinance import YFinanceTools
load_dotenv()
def get_company_symbol(company: str) -> str:
    """Use this function to get the symbol for a company.

    Args:
        company (str): The name of the company.

    Returns:
        str: The symbol for the company.
    """
    symbols = {
        "Oracle": "orc",
    
    }
    return symbols.get(company, "Unknown")

agent=Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True),get_company_symbol],
    show_tools_calls= True,
    markdown = True,
    instructions=["use table to display data.","If you don't know the company symbol, Pleasue use get_company_symbol, even if it is not public company"],
    debug_mode=True,
)

agent.print_response("Summarize and compare analyst recommendations and fundamentals for SAP and Oracle. Show in tables.", stream=True)