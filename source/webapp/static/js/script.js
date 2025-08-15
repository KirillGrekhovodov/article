async function makeRequest(url, method='GET'){
    let response = await fetch(url, {"method": method})
    if (response.ok){
        return await response.json();
    }
    else{
        let error = await response.json()
        throw new Error(error.message)
    }
}

async function onClick(event){
    event.preventDefault();
    console.log(event.target);
    let a = event.target;
    let url = a.href;
    let response = await makeRequest(url);
    let articleId = a.dataset['articleId'];
    console.log(articleId);
    // let span = document.createElement("span");
    // span.innerText = response.test;
    // a.parentElement.appendChild(span);
    let p = a.parentElement.getElementsByClassName("testJs")[0];
    p.innerHTML = response.test;
}

function onLoad(){
    let links = document.querySelectorAll('[data-test-js="js"]');
    for (let link of links){
        link.addEventListener("click", onClick);
    }
}

window.addEventListener("load", onLoad)
