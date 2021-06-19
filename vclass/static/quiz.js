console.log("Welcome guys to the quiz")
const url=window.location.href
var qbox=document.getElementById("questions")
var timerbox=document.getElementById("timer")
let timer
let flsc
let flag

//console.log(timerbox.value)
   function fulltimer() {
  flsc= setInterval(function(){
    console.log("flsc")
    if(!IsFullScreen())
    {
    clearInterval(timer)
    clearInterval(flsc)
    document.getElementById("test").style.display="none"
    document.getElementById("blocktest").style.display="block"
    }
  },1000);
}
function IsFullScreen() {
    console.log("checking")
     return !!(document.fullscreenElement || document.mozFullScreenElement || document.webkitFullscreenElement || document.msFullscreenElement)
}

    $(window).on('load', function() {

    console.log("Suuce")
        $('#exampleModal').modal({backdrop: 'static', keyboard: false}) ;
    });
const activateTimer=(time)=>{
    let minutes=time-1
    if(time.toString().length<2)
    {
    document.getElementById("timer").innerHTML= `<b>0${time}:00</b>`;
    }
    else{
    document.getElementById("timer").innerHTML= `<b>${time}:00</b>`;
    }
    let seconds=60
    let displayminutes
    let displayseconds


    timer= setInterval(()=>{
    console.log("timer")
    seconds--
    if(seconds<0)
    {
    seconds=59
    minutes--
    }
    if(minutes.toString().length<2){
        displayminutes='0'+minutes
    }
    else{
    displayminutes=minutes
    }
    if(seconds.toString().length<2){
        displayseconds='0'+seconds
    }
    else{
    displayseconds=seconds
    }

    document.getElementById("timer").innerHTML=`<b>${displayminutes}:${displayseconds}</b>`;
    if(minutes<=0 && seconds<=0)
    {
    clearInterval(timer)
    clearInterval(flsc)
    alert("Time Over!!")
    sendData()
    }
    },1000)
}
function fullscreen() {
element=document.documentElement;
console.log("element");
        if(element.requestFullscreen)
        {
            element.requestFullscreen();
            activateTimer(timing);
            fulltimer();
            }
        else if(element.mozRequestFullScreen)
        {
            element.mozRequestFullScreen();
            fulltimer()}
        else if(element.webkitRequestFullscreen){
            element.webkitRequestFullscreen();
            fulltimer()}
        else if(element.msRequestFullscreen){
            element.msRequestFullscreen();
            fulltimer();}
         else{
         alert("Test not supported in this browser")
         clearInterval(timer)
         clearInterval(flsc)
        document.getElementById("invalid").style.display="block"
         }
    }

$.ajax({
    type:'GET',
    url:`${url}/data`,
    success:function(response){
    console.log(`${url}/data`)
    data=response.data
    ques=response.ques
    timing=response.time
    flag=response.flag
    if(flag){
    for(let i=0;i<ques.length;++i)
    {
    document.getElementById("questions").innerHTML+=`
    <hr>
    <div class="mb-2"><b>${i+1}) ${ques[i]}</b></div>
    `;
    for(let j=0;j<data[i].length;++j)
    {
    document.getElementById("questions").innerHTML+=`
    <div >
    <input type="radio" class="ans" id="${ques[i]}-${data[i][j]}" name="${ques[i]}" value="${data[i][j]}">
    <label for="${ques[i]}">${data[i][j]}</label>
    </div>
    `;
    }
    }}
    else{
        document.getElementById("test").style.display="none";
    document.getElementById("notlive").style.display="block";
    alert("Quiz not live!!!");

    }
       //activateTimer(response.time)
    },

    error:function(error){
    console.log(error)
    }
    })

const quizform=document.getElementById("quiz-form")
const csrf=document.getElementsByName("csrfmiddlewaretoken")



const sendData= () => {
clearInterval(timer)
         clearInterval(flsc)
    const data={}
    const elements=[...document.getElementsByClassName('ans')]
    data['csrfmiddlewaretoken']=csrf[0].value
    elements.forEach(el=>{
    if(el.checked){
        data[el.name]=el.value
    }
    else{
    if(!data[el.name]){
        data[el.name]=null
    }
    }
    })
    const url=window.location.href
    $.ajax({
        type:'post',
        url:`${url}/save`,
        data: data,
        success:function(response){
        console.log(response)
        document.getElementById("test").style.display="none"
        document.getElementById("posttest").style.display="block"
        },
        error:function(error){
        //console.log(error)
        console.log("eerr")
        }
    });
}
function trigger(){
    sendData()
}