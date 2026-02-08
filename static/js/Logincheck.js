document.getElementById("homeButton").addEventListener("click", function(){
  const user = document.getElementById("unameInput").value;
  const pass = document.getElementById("unamepwd").value;

  if (user === "suresh" && pass === "suresh")
     {
    window.location.href = '/home/';
  } else {
    alert("Invalid credentials");
  }
});