var names_array = []
var tab_amount = 0
var name_from_db = ""

fetch(`http://127.0.0.1:8787/list_names`)
    .then(response => response.json())
    .then(data => {
        results = data["results"]
        for (var i = 0; i < results.length; i++) {
            person_name = results[i]["PersonName"]
            names_array.push(person_name)

            selector_node = document.createElement("option");
            selector_node.value = (person_name)
            const selector_textnode = document.createTextNode(person_name)
            selector_node.appendChild(selector_textnode)
            document.getElementById("person_selector").appendChild(selector_node)

        }
    })
    .catch(error => console.error('Error:', error));

function see_tab() {
    var name = document.getElementById("person_selector").value
    fetch(`http://127.0.0.1:8787`)
        .then(response => response.json())
        .then(data => {
            results = data["results"]
            document.getElementById("main_thing")

            for (var i = 0; i < results.length; i++) {
                const name_from_db = (results[i]["PersonName"])

                if (name_from_db == name) {
                    tab_amount = ("$" + results[i]["PersonTab"]);
                    document.getElementById("display_tab").innerText = tab_amount
                }

            }
        })
        .catch(error => console.error('Error:', error));
}

async function pay_tab() {
    var name = document.getElementById("person_selector").value
    await fetch(`http://127.0.0.1:8787`)
        .then(response => response.json())
        .then(data => {
            results = data["results"]
            document.getElementById("main_thing")

            for (var i = 0; i < results.length; i++) {
                name_from_db = (results[i]["PersonName"])

                if (name_from_db == name) {
                    tab_amount = (results[i]["PersonTab"]);
                    console.log("in IF")
                    console.log(tab_amount)
                }

            }
        })
        .catch(error => console.error('Error:', error));

    var amount_off_tab = Number.parseFloat(document.getElementById("amount_off_tab").value)

    console.log(amount_off_tab)
    console.log(tab_amount)
    console.log(name)
    if (amount_off_tab <= tab_amount) {
        var new_tab = tab_amount - amount_off_tab

        const formData = new URLSearchParams();
        formData.append('name', name);
        formData.append('amount', new_tab);

        const response =  await fetch('http://127.0.0.1:8787/new_tab', {
            method: 'POST',
            body: formData
        });

        see_tab()
        document.getElementById("amount_off_tab").value = 0

    } else {
        alert("This is more than in tab, try again")
    }
}