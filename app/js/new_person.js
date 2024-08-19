async function new_person() {
  console.log("button pressed")
    var person_name = document.getElementById("person_name").value

    // Create URL-encoded form data
    const formData = new URLSearchParams();
    formData.append('person_name', person_name);
  
    const response = await fetch('http://127.0.0.1:8787/add_person', {
      method: 'POST',
      body: formData
    });
  
    if (response.ok) {
      const data = await response.json();
      console.log('Success:', data);
      document.getElementById("person_name").value = ""
    } else {
      console.error('Error:', response.statusText);
    }
  }