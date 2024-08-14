cart_items = []
items_array = []
var running_total = 0

fetch(`http://127.0.0.1:8787/buying_page`)
  .then(response => response.json())
  .then(data => {
    results = data["results"]
    console.log(results);

    for (var i = 0; i < results.length; i++) {
      const node = document.createElement("div");
      var row_name = "row_" + i
      node.id = row_name;
      node.className = "product_card"
      document.getElementById("table_tab").appendChild(node);


      // const node1 = document.createElement("div");
      // const textnode1 = document.createTextNode(results[i]["ProductID"]);
      // node1.appendChild(textnode1);
      // document.getElementById(row_name).appendChild(node1);

      const node2 = document.createElement("div");
      const textnode2 = document.createTextNode(results[i]["ProductName"]);
      node2.appendChild(textnode2);
      document.getElementById(row_name).appendChild(node2);

      const node3 = document.createElement("div");
      const textnode3 = document.createTextNode(results[i]["ProductPrice"]);
      node3.appendChild(textnode3);
      document.getElementById(row_name).appendChild(node3);

      const purchase_button = document.createElement("button");
      const purchase_button_text = document.createTextNode("Buy");
      var button_id = "add_" + results[i]["ProductName"]
      purchase_button.id = button_id
      purchase_button.appendChild(purchase_button_text);
      document.getElementById(row_name).appendChild(purchase_button);

      items_array.push(results[i]["ProductName"], results[i]["ProductPrice"])

      let productName = results[i]["ProductName"];
      purchase_button.onclick = function () {
        addToCart(0, productName);
      };
    }



  })
  .catch(error => console.error('Error:', error));


function addToCart(ProductID, ProductName) {
  var name_index = cart_items.findIndex((element) => element == ProductName);
  if (name_index == -1) {
    cart_items.push(ProductName, 1)
  } else {
    cart_items[(name_index + 1)] += 1
  }

  document.getElementById("cart_list").innerHTML = "";
  running_total = 0

  for (var i = 0; i < (cart_items.length); i++) {
    if (i % 2 == 0) {
      console.log("STUFF IS RUNNING!!!")
      console.log("Running total = " + running_total)

      node = document.createElement("div");
      node.id = ("cart_row_" + i)
      document.getElementById("cart_list").appendChild(node)

      const node1 = document.createElement("div");
      const textnode1 = document.createTextNode(cart_items[i]);
      node1.appendChild(textnode1);
      document.getElementById("cart_row_" + i).appendChild(node1);

      const node2 = document.createElement("div");
      const textnode2 = document.createTextNode(cart_items[(i + 1)])
      node2.appendChild(textnode2)
      document.getElementById("cart_row_" + i).appendChild(node2);

      const node3 = document.createElement("div");
      var name_index = (items_array.findIndex((element) => element == cart_items[i])) + 1
      const textnode3 = document.createTextNode(items_array[name_index])
      node3.appendChild(textnode3)
      document.getElementById("cart_row_" + i).appendChild(node3);

      this_item = (items_array[name_index]) * (cart_items[(i + 1)])
      running_total = running_total + this_item
    }

  }
  document.getElementById("cart_price").innerHTML = running_total
}

function add_to_tab() {
  adding_data("Josh", running_total)
}

async function adding_data(userName, amount) {
  // Create URL-encoded form data
  const formData = new URLSearchParams();
  formData.append('name', userName);
  formData.append('amount', amount);

  const response = await fetch('http://127.0.0.1:8787/add_info', {
    method: 'POST',
    body: formData
  });

  if (response.ok) {
    const data = await response.json();
    console.log('Success:', data);
  } else {
    console.error('Error:', response.statusText);
  }
}
  
  
  // async function insertData() {
  //   // Make an HTTP GET request to your Python Worker
  //   fetch('http://127.0.0.1:8787/add_info')
  // }

  // // Call the function to insert data
  // insertData();


function clear_cart() {
  document.getElementById("cart_list").innerHTML = "";
  cart_items = []
  document.getElementById("cart_price").innerHTML = "0";
}




// function aFunction() {
//   console.log("BEER ADDED!!!")
//   console.log(items_bought)
// }

// console.log(items_bought.findIndex((element) => element == "Beer"))

// var ProductName = "Beer"
// var name_index = cart_items.findIndex((element) => element == ProductName);
//   if (name_index == -1) {
//     console.log("not_found")
//     cart_items.push(ProductName, 0)
//   } else {
//     name_index
//     cart_items[(name_index + 1)] += 1
//   }
//   console.log(cart_items)