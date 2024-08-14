from js import Response
from urllib.parse import urlparse
import json

async def on_fetch(request, env):
    url = urlparse(request.url)
    print(request.method)
    print(url.path)
    
    

    if url.path == "/add_info":
        return await handle_request(request, env)
    elif url.path == "/buying_page":
        results = await env.DB.prepare("SELECT * FROM Products").all()
        resp = Response.json(results)
        resp.headers.append("Access-Control-Allow-Origin", "*")
        return resp
    else:
        results = await env.DB.prepare("SELECT * FROM Tabs").all()
        resp = Response.json(results)
        resp.headers.append("Access-Control-Allow-Origin", "*")
        return resp

    # Query D1 - we'll list all tables in our database in this example

    # Return a JSON response
    

async def handle_request(request, env):
    try:
        print("Try thing")


        if request.method == "OPTIONS":
            print("Handling OPTIONS request")
            r.headers.append("Access-Control-Allow-Origin", "*")
            # r.headers.append("Content-Type", "application/json")
            # r.headers.append("Access-Control-Allow-Headers", "Content-Type")

            # r.headers.append("Access-Control-Allow-Headers", "content-type")
            # # Handle preflight requests
            # headers = {
            #     "Access-Control-Allow-Origin": "*",
            #     "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            #     "Access-Control-Allow-Headers": "Content-Type"
            # }

            return r
        print("Hello")

        print("Reading JSON data")
        # data = await request.json()

        try:
            data = await request.json()
            print("Data received:", json.dumps(data, indent=2))
        except Exception as json_error:
            print(f"Error reading JSON data: {json_error}")
            r = Response.json({"error": "Failed to parse JSON"}, status=400)
            return r.append.headers.append("Access-Control-Allow-Origin", "*")


        print("did the await")
        print("Data received:", data.dumps(data, indent=2))

        print("JSON data read successfully")
        print(f"Data received: {data}")


        data = await request.json()
        name_value = data.get("name")
        amount_value = data.get("amount")
        


        print(f"Name: {name_value}, Amount: {amount_value}")  # Debugging line
        
        # Adjust SQL statement to use variables
        sql = 'UPDATE Tabs SET PersonTab = PersonTab + ? WHERE PersonName = ?'
        stmnt = env.DB.prepare(sql)
        await stmnt.bind(amount_value, name_value).run()
        
        results = {"message": "Data updated successfully", "status": 200}
        
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        }
        resp = Response.json(results, headers=headers)
        resp.headers.append("Access-Control-Allow-Origin", "*")
        # resp.headers.append("Access-Control-Allow-Headers", "content-type")
        return resp
    except Exception as e:
        error_response = {"error": str(e), "status": 500}
        resp = Response.json(error_response)
        resp.headers.append("Access-Control-Allow-Origin", "*")
        return resp









# async def handle_request(request, env):
#     name_value = "John Doe"
#     tab_value = 100

#     sql = 'INSERT INTO Tabs (PersonName, PersonTab) VALUES (?, ?)'
#     # stmnt = env.DB.prepare(sql)
#     # await stmnt.bind(name_value, tab_value).run()

    
#     stmnt = env.DB.prepare(sql)
#     await stmnt.bind(name_value, tab_value).run()
    
#     try:
#         # Assume results is a dictionary you want to return as JSON
#         results = {"message": "Data inserted successfully", "status": 200}

#         # Create a Response object with JSON content
#         resp = Response.json(results)

#         # Set CORS headers
#         resp.headers.append("Access-Control-Allow-Origin", "*")

#         return resp
#     except Exception as e:
#         # Return a Response object with error details and status code
#         error_response = {"error": str(e), "status": 500}
#         resp = Response.json(error_response)
#         resp.headers.append("Access-Control-Allow-Origin", "*")
#         return resp