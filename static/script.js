function sendQuick(text){
    document.getElementById("userInput").value = text;
    sendMessage();
}

function sendMessage(){

    let input = document.getElementById("userInput");
    let message = input.value.trim();

    if(message===""){
        return;
    }

    let chatbox = document.getElementById("chatbox");

    chatbox.innerHTML += `
        <div class="user-message">
            ${message}
        </div>
    `;

    chatbox.scrollTop = chatbox.scrollHeight;

    fetch("/get",{
        method:"POST",
        headers:{
            "Content-Type":"application/x-www-form-urlencoded"
        },
        body:`msg=${encodeURIComponent(message)}`
    })
    .then(response => response.json())
    .then(data => {

        chatbox.innerHTML += `
            <div class="bot-message">
                ${data.response}
            </div>
        `;

        chatbox.scrollTop = chatbox.scrollHeight;
    });

    input.value="";
}

document.getElementById("userInput")
.addEventListener("keypress",function(event){

    if(event.key==="Enter"){
        sendMessage();
    }

});