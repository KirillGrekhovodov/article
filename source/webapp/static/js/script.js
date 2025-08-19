async function makeRequest(url, method = 'GET') {
    let headers = {};
    if (method !== 'GET'){
        const csrfToken = await getCookie('csrftoken');
        headers['X-CSRFToken'] = csrfToken;
    }
    let response = await fetch(url, {
        "method": method,
        "headers": headers,
    })
    if (response.ok) {
        return await response.json();
    } else {
        let error = await response.json()
        throw new Error(error.message)
    }
}

async function onClick(event) {
    event.preventDefault();
    console.log(event.target);
    let a = event.target;
    let url = a.href;
    let response = await makeRequest(url, 'PATCH');
    let articleId = a.dataset['articleId'];
    console.log(articleId);
    // let span = document.createElement("span");
    // span.innerText = response.test;
    // a.parentElement.appendChild(span);
    let p = a.parentElement.getElementsByClassName("testJs")[0];
    p.innerHTML = response.test;
}

function onLoad() {
    let links = document.querySelectorAll('[data-test-js="js"]');
    for (let link of links) {
        link.addEventListener("click", onClick);
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


window.addEventListener("load", onLoad)
