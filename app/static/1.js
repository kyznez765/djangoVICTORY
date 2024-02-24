let formbut = document.getElementById('formbut')

formbut.onclick = f1
let vision = false

function f1(){
    let formdiv = document.getElementById('formdiv')
    if (!vision){
        formdiv.hidden = false
    vision = true
    }
    else {
        formdiv.hidden = true
        vision = false
    }
}