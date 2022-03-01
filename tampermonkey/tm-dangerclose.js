// ==UserScript==
// @name         dangerclose
// @namespace    https://github.com
// @version      0.1
// @description  github confirm typing disabler
// @author       me
// @match        https://github.com/*
// @icon         https://www.google.com/s2/favicons?domain=github.com
// @grant        none
// ==/UserScript==



const observer = new MutationObserver((_) => {
    if (document.querySelector('#settings-tab').classList.contains('selected')) {
        if (document.URL.includes('=repositories')) {
            $('.Label--secondary').each((_, el) => {
                if (el.innerText === 'Public') el.style.background = '#451313'
                else el.style.background = '#003008'
            })
        }
        let inputElements = document.querySelectorAll('.form-control.input-block');
        if (inputElements.length > 0) {
            const url = document.URL.split('/')
            inputElements.forEach((inputElement) => {
                if (inputElement != null && !inputElement.className.includes('js-synced-repo-owner-input')) {
                    inputElement.value = url[url.length - 3] + '/' + url[url.length - 2];
                }
            })
            let inputs = document.querySelectorAll('.btn.btn-block.btn-danger');
            inputs.forEach((input) => {
                input.removeAttribute('disabled');
            })
        }
    }
})
const config = {
    childList: true,
    subtree: true
}
observer.observe(document, config);