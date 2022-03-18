// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://67f1-94-240-239-230.ngrok.io/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=ngrok.io
// @run-at       document-end
// @require      http://code.jquery.com/jquery-3.4.1.min.js
// ==/UserScript==

const btn = document.createElement('button')
$('#topside')[0].append(btn)
btn.innerText = 'Download Profile Pictures'

const download = () => {
    $('tr').each((i, e) => {
        if (i !== 0) {
            const url = e.children[1].style.backgroundImage.toString().split(`"`)[1]
            var xhr = new XMLHttpRequest();
            xhr.open("GET", url, true);
            xhr.responseType = "blob";
            xhr.onload = function () {
                var urlCreator = window.URL || window.webkitURL;
                var imageUrl = urlCreator.createObjectURL(this.response);
                var tag = document.createElement('a');
                tag.href = imageUrl;
                tag.download = `${i}.png`;
                document.body.appendChild(tag);
                tag.click();
                document.body.removeChild(tag);
            }
            xhr.send();
        }
    })
}

btn.onclick = download