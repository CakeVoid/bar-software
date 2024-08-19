async function new_product() {
    var product_name = document.getElementById("product_name").value
    var product_price = document.getElementById("product_price").value
    product_price = product_price.replace("$", "")
    console.log(product_name)
    console.log(product_price)

    // Create URL-encoded form data
    const formData = new URLSearchParams();
    formData.append('product_name', product_name);
    formData.append('product_price', product_price);
  
    const response = await fetch('http://127.0.0.1:8787/add_product', {
      method: 'POST',
      body: formData
    });
  
    if (response.ok) {
      const data = await response.json();
      console.log('Success:', data);
      document.getElementById("product_name").value = ""
      document.getElementById("product_price").value = ""
    } else {
      console.error('Error:', response.statusText);
    }
  }