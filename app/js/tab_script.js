i = 0
fetch(`http://127.0.0.1:8787`)
  .then(response => response.json())
  .then(data => {
    console.log(data)
    results = data["results"]
    console.log(results);
    document.getElementById("main_thing")

    for (var i = 0; i < results.length; i++) {

      const node1 = document.createElement("div");
      const textnode1 = document.createTextNode(results[i]["PersonID"]);
      node1.appendChild(textnode1);
      document.getElementById("table_tab").appendChild(node1);

      const node2 = document.createElement("div");
      const textnode2 = document.createTextNode(results[i]["PersonName"]);
      node2.appendChild(textnode2);
      document.getElementById("table_tab").appendChild(node2);

      const node3 = document.createElement("div");
      const textnode3 = document.createTextNode(results[i]["PersonTab"]);
      node3.appendChild(textnode3);
      document.getElementById("table_tab").appendChild(node3);
    }
  })
  .catch(error => console.error('Error:', error));

// async function insertData() {

//   // Make an HTTP GET request to your Python Worker
//   fetch('http://127.0.0.1:8787/add_info')
// }

// // Call the function to insert data
// insertData();