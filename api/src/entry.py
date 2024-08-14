from js import Response
from urllib.parse import urlparse, parse_qs

async def on_fetch(request, env):
    url = urlparse(request.url)
    print(request.method)
    print(url.path)
    
    

    if url.path == "/add_cart":
        return await handle_request(request, env)
    if url.path == "/list_names":
        results = await env.DB.prepare("SELECT PersonName FROM Tabs").all()
        resp = Response.json(results)
        resp.headers.append("Access-Control-Allow-Origin", "*")
        return resp
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