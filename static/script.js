function predict() {
  fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      pregnancies: document.getElementById("preg").value,
      glucose: document.getElementById("glucose").value,
      bp: document.getElementById("bp").value,
      skin: document.getElementById("skin").value,
      insulin: document.getElementById("insulin").value,
      bmi: document.getElementById("bmi").value,
      dpf: document.getElementById("dpf").value,
      age: document.getElementById("age").value,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("result").innerText = data.result;
    });
}
