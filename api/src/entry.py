from js import Response
from urllib.parse import urlparse, parse_qs

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
        if request.method == "OPTIONS":
            r = Response("")
            r.headers.append("Access-Control-Allow-Origin", "*")
            r.headers.append("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
            r.headers.append("Access-Control-Allow-Headers", "Content-Type")
            return r

        print("Reading form data")

        # Read the request body as text
        body = await request.text()
        # Parse form data
        data = parse_qs(body)
        name_value = data.get("name", [""])[0]
        amount_value_str = data.get("amount", ["0"])[0]

        print(f"Raw Name: {name_value}, Raw Amount: {amount_value_str}")

        # Convert amount to an integer
        try:
            amount_value = int(amount_value_str)
        except ValueError:
            print(f"Invalid amount: {amount_value_str}")
            amount_value = 0

        print(f"Parsed Name: {name_value}, Parsed Amount: {amount_value}")

        if name_value == "" or amount_value == 0:
            print("Error: Missing name or invalid amount")
            raise ValueError("Name or amount not provided correctly")

        # Adjust SQL statement to use variables
        sql = 'UPDATE Tabs SET PersonTab = PersonTab + ? WHERE PersonName = ?'
        stmnt = env.DB.prepare(sql)
        await stmnt.bind(amount_value, name_value).run()

        results = {"message": "Data updated successfully", "status": 200}

        resp = Response.json(results)
        resp.headers.append("Access-Control-Allow-Origin", "*")
        resp.headers.append("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        resp.headers.append("Access-Control-Allow-Headers", "Content-Type")
        return resp

    except Exception as e:
        error_response = {"error": str(e), "status": 500}
        resp = Response.json(error_response)
        resp.headers.append("Access-Control-Allow-Origin", "*")
        return resp





# async def handle_request(request, env):
#     try:
#         print("Try thing")


#         if request.method == "OPTIONS":
#             print("Handling OPTIONS request")
#             r.headers.append("Access-Control-Allow-Origin", "*")
#             # r.headers.append("Content-Type", "application/json")
#             # r.headers.append("Access-Control-Allow-Headers", "Content-Type")

#             # r.headers.append("Access-Control-Allow-Headers", "content-type")
#             # # Handle preflight requests
#             # headers = {
#             #     "Access-Control-Allow-Origin": "*",
#             #     "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
#             #     "Access-Control-Allow-Headers": "Content-Type"
#             # }

#             return r
#         print("Hello")

#         print("Reading JSON data")
#         # data = await request.json()
#         data = await request.json()
#         name_value = data.name
#         amount_value = data.get("amount")
        


#         print(f"Name: {name_value}, Amount: {amount_value}")  # Debugging line
        
#         # Adjust SQL statement to use variables
#         sql = 'UPDATE Tabs SET PersonTab = PersonTab + ? WHERE PersonName = ?'
#         stmnt = env.DB.prepare(sql)
#         await stmnt.bind(amount_value, name_value).run()
        
#         results = {"message": "Data updated successfully", "status": 200}
        
#         headers = {
#             "Access-Control-Allow-Origin": "*",
#             "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
#             "Access-Control-Allow-Headers": "Content-Type"
#         }
#         resp = Response.json(results, headers=headers)
#         resp.headers.append("Access-Control-Allow-Origin", "*")
#         # resp.headers.append("Access-Control-Allow-Headers", "content-type")
#         return resp
#     except Exception as e:
#         error_response = {"error": str(e), "status": 500}
#         resp = Response.json(error_response)
#         resp.headers.append("Access-Control-Allow-Origin", "*")
#         return resp









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