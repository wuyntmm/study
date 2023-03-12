function getRandomInt() {
  return Math.floor(Math.random() * (499 - 2 + 1)) + 2;
}

let randomInt = getRandomInt();

console.log(randomInt);


const myDiv = document.createElement('div');
myDiv.className = 'buttons';
myDiv.style.background = 'grey';
myDiv.style.textAlign = 'center';


['Add Friend',`Friend counter: ${randomInt}`, 'Send message', 'Offer a job'].map(buttonName => {
    let button = document.createElement('button');
    button.className = 'btn btn-success';
    button.innerText =  buttonName;
    button.style.margin = '5px';
    myDiv.appendChild(button);
})

document.getElementsByTagName('header')[0].appendChild(myDiv);


document.getElementsByTagName('button')[0].onclick = (event) => {
    event.target.disabled = true;
    event.target.innerText = 'Confirmation is pending';
    document.getElementsByTagName('button')[1].innerText = `Friend counter: ${randomInt + 1}`
};

let messageCheck = 0;
document.getElementsByTagName('button')[2].onclick = (event) => {
    if (messageCheck === 0) {
        event.target.style.background = 'Orange';
        messageCheck = 1;
    } else {
        event.target.style.background = '#198754';
        messageCheck = 0;
    }
};

let jobCheck = 0;
document.getElementsByTagName('button')[3].onclick = (event) => {
    if (jobCheck === 0) {
        document.getElementsByTagName('button')[0].style.visibility = "hidden";
        jobCheck = 1

    } else {
        document.getElementsByTagName('button')[0].style.visibility = "visible";
        jobCheck = 0;
    }
};
