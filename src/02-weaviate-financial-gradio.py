import weaviate
import weaviate.classes as wvc
from weaviate.auth import AuthApiKey
import os
import requests
import json
import ijson
import gradio as gr

def ingest_data(client):

    # ===== Define the collection =====
    symbols = client.collections.create(
        name="Symbols",
        vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_openai(),  # If set to "none" you must always provide vectors yourself. Could be any other "text2vec-*" also.
        generative_config=wvc.config.Configure.Generative.openai()  # Ensure the `generative-openai` module is used for generative queries
    )

    # Settings for displaying the import progress
    counter = 0
    interval = 100  # print progress every this many records; should be bigger than the batch_size

    print("JSON streaming, to avoid running out of memory on large files...")
    with client.batch.fixed_size(batch_size=50) as batch:
        with open("data/symbols.json", "rb") as f:
            objects = ijson.items(f, "item")
            for obj in objects:
                properties = {
                    "Symbol": obj["Symbol"],
                    "Name": obj["Name"],
                    "Description": obj["Description"],
                    "CIK": obj["CIK"],
                    "Exchange": obj["Exchange"],
                    "Currency": obj["Currency"],
                    "Country": obj["Country"],
                    "Sector": obj["Sector"], 
                    "Industry": obj["Industry"],
                    "Address": obj["Address"],
                    "FiscalYearEnd": obj["FiscalYearEnd"],
                    "LatestQuarter": obj["LatestQuarter"],
                    "MarketCapitalization": obj["MarketCapitalization"],
                    "BookValue": obj["BookValue"],
                    "EBITDA": obj["EBITDA"],
                    "PERatio": obj["PERatio"],
                    "PEGRatio": obj["PEGRatio"],
                    "DividendPerShare": obj["DividendPerShare"],
                    "DividendYield": obj["DividendYield"],
                    "EPS": obj["EPS"],
                    "RevenuePerShareTTM": obj["RevenuePerShareTTM"],
                    "ProfitMargin": obj["ProfitMargin"],
                    "OperatingMarginTTM": obj["OperatingMarginTTM"],
                    "ReturnOnAssetsTTM": obj["ReturnOnAssetsTTM"],
                    "ReturnOnEquityTTM": obj["ReturnOnEquityTTM"],
                    "RevenueTTM": obj["RevenueTTM"],
                    "GrossProfitTTM": obj["GrossProfitTTM"],
                    "DilutedEPSTTM": obj["DilutedEPSTTM"],
                    "QuarterlyEarningsGrowthYOY": obj["QuarterlyEarningsGrowthYOY"],
                    "QuarterlyRevenueGrowthYOY": obj["QuarterlyRevenueGrowthYOY"],
                    "AnalystTargetPrice": obj["AnalystTargetPrice"],
                    "AnalystRatingStrongBuy": obj["AnalystRatingStrongBuy"],
                    "AnalystRatingBuy": obj["AnalystRatingBuy"],
                    "AnalystRatingHold": obj["AnalystRatingHold"],
                    "AnalystRatingSell": obj["AnalystRatingSell"],
                    "AnalystRatingStrongSell": obj["AnalystRatingStrongSell"],
                    "TrailingPE": obj["TrailingPE"],
                    "ForwardPE": obj["ForwardPE"],
                    "PriceToSalesRatioTTM": obj["PriceToSalesRatioTTM"],
                    "PriceToBookRatio": obj["PriceToBookRatio"],
                    "EVToRevenue": obj["EVToRevenue"],
                    "EVToEBITDA": obj["EVToEBITDA"],
                    "Beta": obj["Beta"],
                    "fiftytwoWeekHigh": obj["52WeekHigh"],
                    "fiftytwoWeekLow": obj["52WeekLow"],
                    "fiftyDayMovingAverage": obj["50DayMovingAverage"],
                    "twohundredDayMovingAverage": obj["200DayMovingAverage"],
                    "SharesOutstanding": obj["SharesOutstanding"],
                    "DividendDate": obj["DividendDate"],
                    "ExDividendDate": obj["ExDividendDate"]
                }
                batch.add_object(
                    collection="Symbols",
                    properties=properties,
                    # If you Bring Your Own Vectors, add the `vector` parameter here
                    # vector=obj.vector["default"]
                )

                # Calculate and display progress
                counter += 1
                if counter % interval == 0:
                    print(f"Imported {counter} symbols.")


    print(f"Finished importing {counter} symbols.")


def semantic_search(query='computers', limit=2) -> dict:
    print(f'\nSemantic Search, query = {query}.')
    print(f'limit = {limit}')
    response = symbols.query.near_text(
        query=query,
        limit=limit
    )

    return_list = []
    for i in range(limit):
        return_list.append(response.objects[i].properties['name'])
    return return_list


def generative_search(query='computers', task=None, limit=2) -> str:
    print(f'\nPerforming generative search, query = {query}, limit = {limit}.')
    print(f'Prompt: {task}')
    print(f'limit = {limit}')
    response = symbols.generate.near_text(
        query=query,
        limit=limit,
        grouped_task=task
    )
    return response.generated

 
if __name__ == '__main__':
    weaviate_url = os.getenv("WEAVIATE_URL")       
    weaviate_key = os.getenv("WEAVIATE_API_KEY")

    try:
        client = weaviate.connect_to_custom(
                    http_host=weaviate_url,
                    auth_credentials=AuthApiKey(weaviate_key),
                    http_port=80,
                    http_secure=False,
                    grpc_host="weaviate-grpc.weaviate",
                    grpc_port=50051,
                    grpc_secure=False,
                    skip_init_checks=False,
                    headers={"X-OpenAI-Api-key": os.getenv("OPENAI_API_KEY")}
                )

        symbols = client.collections.get("Symbols")
        
        #
        # Build the Gradio user interface.
        #

        #
        # Semantic Search 
        #
        with gr.Blocks(title='Summarizing Financial Data using RAG') as demo:
            gr.Markdown("""# Summarizing Financial Data using Retrieval Augmented Generation (RAG).""")
            semantic_examples = [
                ["Computers"],
                ["Computer Software"],
                ["Pharmaceuticals"],
                ["Consumer Products"],
                ["Commodities"],
                ["Retail"],
                ["Manufacturing"],
                ["Energy"],
                ["National Defense"],
                ["Auto Makers"]
            ]
            gr.Markdown("""### Begin with a search.""")
            semantic_input_text = gr.Textbox(label="Enter a search concept or choose an example below:", value=semantic_examples[0][0])
            gr.Examples(semantic_examples,
                fn=semantic_search,
                inputs=semantic_input_text, label="Example search concepts:"
                )
            limit_slider = gr.Slider(label="Adjust the query return limit. (Optional)",value=2, minimum=1, maximum=5, step=1)
            state = gr.State(value=2)
            vdb_button = gr.Button(value="Search the financial vector database.")
            vdb_button.click(fn=semantic_search, inputs=[semantic_input_text, limit_slider], outputs=gr.Textbox(label="Search Results (Filters = Name)"))
            

            #
            # Generative Search 
            # 
            prompt_examples = [
                ["Summarize the information from a financial perspective."],
                ["Summarize the information from a financial investment perspective."],
                ["Summarize the potential financial investment risks and rewards."]
            ]

            gr.Markdown("""### Summarize""")
            generative_search_prompt_text = gr.Textbox(label="Enter a summarization task or choose an example below.", value=prompt_examples[0][0])
            gr.Examples(prompt_examples,
                fn=generative_search,
                inputs=[generative_search_prompt_text]
            )
            button = gr.Button(value="Generate the summary.")
            button.click(fn=generative_search,
            inputs=[semantic_input_text, generative_search_prompt_text, limit_slider],
            outputs=gr.Textbox(label="Summary"))
            
        demo.queue(max_size=10)
        demo.launch(server_name='0.0.0.0', server_port=8080)

    finally:
        client.close()  # Close client gracefully

