function loading(){const data=document.getElementById("data")
if(data!==null){data.style.display='none';}
const spinner=document.getElementById("loadSpinner");spinner.parentElement.style.display='block';spinner.style.display='block';}
(()=>{'use strict'
const forms=document.querySelectorAll('.needs-validation')
Array.from(forms).forEach(form=>{form.addEventListener('submit',event=>{if(!form.checkValidity()){event.preventDefault()
event.stopPropagation()}else{loading();}
form.classList.add('was-validated')},false)})})()
document.addEventListener('DOMContentLoaded',()=>{const animatedTextEl=document.getElementById("animatedText");const problemText="Walking isn’t just movement—it’s a vital sign of health. For older adults, stroke survivors, and individuals with mobility impairments, precise gait tracking is essential. Yet, without continuous monitoring, early warning signs go unnoticed.";let i=0;const speed=50;function typeWriter(){if(i<problemText.length){animatedTextEl.innerHTML+=problemText.charAt(i);i++;setTimeout(typeWriter,speed);}}
typeWriter();});