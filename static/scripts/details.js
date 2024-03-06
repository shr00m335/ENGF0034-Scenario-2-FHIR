let token;

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return null;
  }

async function fetch_data() {
    const url = "/patient/data";
    
    const res = await fetch(url, {
        method: "GET",
        headers: {
            "Authorization": "Bearer " + token
        }
    })

    const data = await res.json();

    display_data(data);
}

function display_data(data) {
    console.log(data)
    document.querySelector("#nameLabel").innerHTML = data.name;
    const labels = document.querySelectorAll("div.details > p");
    labels[0].innerHTML += data.bmi ? data.bmi.value[0] + " " + data.bmi.unit : "";
    labels[1].innerHTML += data.height ? data.height.value[0] + " " + data.height.unit : "";
    labels[2].innerHTML += data.weight ? data.weight.value[0] + " " + data.weight.unit : "";
    labels[3].innerHTML += data.hr ? data.hr.value[0] + data.hr.unit : "";
    labels[4].innerHTML += data.rr ? data.rr.value[0] + data.rr.unit : "";
    labels[5].innerHTML += data.ss ? data.ss.value : "";
    labels[6].innerHTML += data.bt ? data.bt.value[0] + data.bt.unit : "";
    labels[7].innerHTML += data.bmip ? data.bmip.value : "";
    labels[8].innerHTML += data.bp ? `${data.bp.value[1]}/${data.bp.value[0]} ${data.bp.unit}` : "";

}

onload = (e) => {
    token = getCookie("token");
    if (token === null) window.location.href = "/";
    fetch_data();
}