console.log('working--- now ')

let paragraph = document.getElementById('note');
quotes()

setInterval(() => {
    quotes()
}, 30000);

let theme = localStorage.getItem('theme');

if(theme == null){
    setTheme('light')
}
else{
    setTheme(theme)
}


let theme_dots = document.getElementsByClassName('theme-dot')

for (var i=0; theme_dots.length > i; i++){
    theme_dots[i].addEventListener('click', function(){
        let mode = this.dataset.mode
        setTheme(mode)
    })
}

function setTheme(mode){
    if(mode == 'light'){
        document.getElementById('theme-style').href = "static/css/default.css"
    }
    else if(mode == 'green'){
        document.getElementById('theme-style').href = "static/css/green.css"
    }
    else if(mode == 'blue'){
        document.getElementById('theme-style').href = "static/css/blue.css"
    }
    else{
        document.getElementById('theme-style').href = "static/css/purple.css"
    }
    localStorage.setItem('theme', mode)
}


async function quotes(){

    quote = await fetch('http://quotes.stormconsultancy.co.uk/random.json')
    data = await quote.json()
    var text = document.createTextNode(data.quote + " by " + data.author)
    var state = document.getElementById('note').innerHTML;
    if(state == null || state == ""){
        paragraph.appendChild(text);
    }
    else{
        document.getElementById('note').innerHTML = null;
        paragraph.appendChild(text);
    }
}

