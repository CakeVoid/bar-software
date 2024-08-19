from js import Response
from urllib.parse import urlparse, parse_qs


async def on_fetch(request, env):
    url = urlparse(request.url)
    print(request.method)
    print(url.path)

    if url.path == "/add_cart":
        return await handle_request(request, env)
    elif url.path == "/add_product":
        return await handle_product_request(request, env)
    elif url.path == "/new_tab":
        return await new_tab(request, env)
    elif url.path == "/add_person":
        return await handle_person_request(request, env)
    elif url.path == "/list_names":
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
    if request.method == "OPTIONS":
        r = Response("")
        r.headers.append("Access-Control-Allow-Origin", "*")
        r.headers.append(
            "Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS"
        )
        r.headers.append("Access-Control-Allow-Headers", "Content-Type")
        return r

    # Read the request body as text
    body = await request.text()
    # Parse form data
    data = parse_qs(body)
    name_value = data.get("name", [""])[0]
    amount_value_str = data.get("amount", ["0"])[0]

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
    sql = "UPDATE Tabs SET PersonTab = PersonTab + ? WHERE PersonName = ?"
    stmnt = env.DB.prepare(sql)
    await stmnt.bind(amount_value, name_value).run()

    results = {"message": "Data updated successfully", "status": 200}

    resp = Response.json(results)
    resp.headers.append("Access-Control-Allow-Origin", "*")
    resp.headers.append(
        "Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS"
    )
    resp.headers.append("Access-Control-Allow-Headers", "Content-Type")
    return resp


async def handle_product_request(request, env):
    if request.method == "OPTIONS":
        r = Response("")
        r.headers.append("Access-Control-Allow-Origin", "*")
        r.headers.append(
            "Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS"
        )
        r.headers.append("Access-Control-Allow-Headers", "Content-Type")
        return r

    # Read the request body as text
    body = await request.text()
    # Parse form data
    data = parse_qs(body)
    product_name = data.get("product_name", [""])[0]
    product_price = data.get("product_price", ["0"])[0]

    print(f"Parsed Name: {product_name}, Parsed Amount: {product_price}")

    if product_name == "" or product_price == 0:
        print("Error: Missing name or invalid amount")
        raise ValueError("Name or amount not provided correctly")

    # Adjust SQL statement to use variables
    sql = "INSERT INTO Products (ProductName, ProductPrice) VALUES (?, ?)"
    stmnt = env.DB.prepare(sql)
    await stmnt.bind(product_name, product_price).run()

    results = {"message": "Data updated successfully", "status": 200}

    resp = Response.json(results)
    resp.headers.append("Access-Control-Allow-Origin", "*")
    resp.headers.append(
        "Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS"
    )
    resp.headers.append("Access-Control-Allow-Headers", "Content-Type")
    return resp


async def handle_person_request(request, env):
    if request.method == "OPTIONS":
        r = Response("")
        r.headers.append("Access-Control-Allow-Origin", "*")
        r.headers.append(
            "Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS"
        )
        r.headers.append("Access-Control-Allow-Headers", "Content-Type")
        return r

    # Read the request body as text
    body = await request.text()
    # Parse form data
    data = parse_qs(body)
    person_name = data.get("person_name", [""])[0]

    if person_name == "":
        print("Error: Missing name or invalid amount")
        raise ValueError("Name or amount not provided correctly")

    # Adjust SQL statement to use variables
    sql = "INSERT INTO Tabs (PersonName, PersonTab) VALUES (?, ?)"
    stmnt = env.DB.prepare(sql)
    await stmnt.bind(person_name, 0).run()

    results = {"message": "Data updated successfully", "status": 200}

    resp = Response.json(results)
    resp.headers.append("Access-Control-Allow-Origin", "*")
    resp.headers.append(
        "Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS"
    )
    resp.headers.append("Access-Control-Allow-Headers", "Content-Type")
    return resp


async def new_tab(request, env):
    if request.method == "OPTIONS":
        r = Response("")
        r.headers.append("Access-Control-Allow-Origin", "*")
        r.headers.append(
            "Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS"
        )
        r.headers.append("Access-Control-Allow-Headers", "Content-Type")
        return r

    # Read the request body as text
    body = await request.text()
    # Parse form data
    data = parse_qs(body)
    name_value = data.get("name", [""])[0]
    amount_value_str = data.get("amount", ["0"])[0]

    # Convert amount to an integer

    amount_value = float(amount_value_str)

    print(f"Parsed Name: {name_value}, Parsed Amount: {amount_value}")

    sql = "UPDATE Tabs SET PersonTab = ? WHERE PersonName = ?"
    stmnt = env.DB.prepare(sql)
    await stmnt.bind(amount_value, name_value).run()

    results = {"message": "Data updated successfully", "status": 200}
    resp = Response.json(results)
    resp.headers.append("Access-Control-Allow-Origin", "*")
    resp.headers.append(
        "Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS"
    )
    resp.headers.append("Access-Control-Allow-Headers", "Content-Type")
    return resp
