import json

import requests
from langchain.tools import tool
from crewai import Agent, Task
from unstructured.partition.html import partition_html

class EbayTools:
    @tool("Ebay Search Tool")
    def search_ebay(search_query: str) -> str:
        """Search for products on eBay"""
        url = "http://ubuntu.orb.local:3000/chrome/content"
        payload = json.dumps({"url": f"https://www.ebay.com/sch/i.html?_nkw={search_query}"})
        headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        elements = partition_html(text=response.text)
        content = "\n\n".join([str(el) for el in elements])
        content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
        summaries = []
        for chunk in content:
            agent = Agent(
                role='Principal Researcher',
                goal=
                'Do amazing data extraction based on the content you are working with',
                backstory=
                "You're a Principal Researcher at a big company and you need to do data extraction based on a given content.",
                allow_delegation=False)
            task = Task(
                agent=agent,
                description=
                f'Analyze and extract item name, price, and url from the content below, return only the item name, url, price in JSON format and nothing else.\n\nCONTENT\n----------\n{chunk}'
            )
            summary = task.execute()
            summaries.append(summary)
        return "\n\n".join(summaries)
        
        